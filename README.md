# Discord-Webhook-Proxy
> Simply Discord Proxy

Converting from Flask to FastAPI: [Another Discord Webhook Proxy](https://devforum.roblox.com/t/another-discord-webhook-proxy/2154490)

## Installation
```
$ pip install -r requirements.txt
```

## Run it
```
$ uvicorn main:app
```

## Usage
Original: `https://discord.com/api/webhooks/<id>/<token>`  
Proxy: `https://<your domain>/api/webhooks/<id>/<token>`
