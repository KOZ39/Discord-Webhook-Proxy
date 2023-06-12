import asyncio

import aiohttp
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address, default_limits=["5000/minute"])
app = FastAPI(docs_url=None, redoc_url=None)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


internal_rate_limiter = {}
async def remove_from_internal_rate_limiter(key: str) -> None:
  await asyncio.sleep(2)
  internal_rate_limiter.pop(key, None)


@app.post("/api/webhooks/{id}/{token}")
async def proxy(
    id: int,
    token: str,
    request: Request,
    background_tasks: BackgroundTasks
):
    key = f"{id}/{token}"

    if key in internal_rate_limiter.keys():
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    internal_rate_limiter[key] = None
    background_tasks.add_task(remove_from_internal_rate_limiter, key)

    data = await request.json()
    async with aiohttp.ClientSession() as session:
        async with session.post(f"https://discord.com/api/webhooks/{id}/{token}", json=data) as resp:
            status_code = 200 if resp.status == 204 else resp.status
            content = await resp.json(content_type=None) or {}

    return JSONResponse(content=content, status_code=status_code)
