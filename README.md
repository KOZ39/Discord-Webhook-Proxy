# Discord-Webhook-Proxy
> Simply Discord Proxy

Implement [Another Discord Webhook Proxy](https://devforum.roblox.com/t/another-discord-webhook-proxy/2154490) with [FastAPI](https://fastapi.tiangolo.com/)

## Requirements
- Python 3.10+

## Running
```bash
git clone https://github.com/KOZ39/Discord-Webhook-Proxy.git
cd discord-webhook-proxy
pip install -r requirements.txt
```

```bash
uvicorn main:app
# or
uvicorn main:app --port <port>
```

## Usage
Change `https://discord.com/api/webhooks/<id>/<token>` to `https://<your domain>/api/webhooks/<id>/<token>`
