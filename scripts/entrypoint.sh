#!/bin/bash
gunicorn octoincore.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000