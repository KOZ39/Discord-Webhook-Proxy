# Discord-Webhook-Proxy
> Simply Discord Proxy

Converting from Flask to FastAPI: [Another Discord Webhook Proxy](https://devforum.roblox.com/t/another-discord-webhook-proxy/2154490)

## Requirements
- Python 3.8+

## Installation
```
$ git clone https://github.com/KOZ39/Discord-Webhook-Proxy.git
$ cd discord-webhook-proxy
$ pip install -r requirements.txt
```

## Usage
> **Warning**: In order for the application to function properly, an SSL certificate and a web server like Nginx are required. Please make sure to configure SSL properly and set up a reverse proxy with Nginx or a similar web server.

```
$ uvicorn main:app
```
or
```
$ uvicorn main:app --port <port>
```

Change `https://discord.com/api/webhooks/<id>/<token>` to `https://<your domain>/api/webhooks/<id>/<token>`
