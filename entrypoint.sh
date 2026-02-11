#!/bin/bash
set -e

if [ -z "$BOT_TOKEN" ]; then
  echo "ERROR: BOT_TOKEN not found!"
  exit 1
fi

ngrok config add-authtoken $NGROK_AUTHTOKEN --log=stdout || true

ngrok http 8000 &
NGROK_PID=$!

for i in {1..10}; do
  NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | jq -r '.tunnels[0].public_url')
  if [ -n "$NGROK_URL" ]; then
    break
  fi
  sleep 1
done

if [ -z "$NGROK_URL" ]; then
  echo "ERROR: Ngrok tunnel not found!"
  kill $NGROK_PID
  exit 1
fi

echo "Ngrok tunnel URL: $NGROK_URL"

curl -s -F "url=${NGROK_URL}/tg-webhook" \
     https://api.telegram.org/bot${BOT_TOKEN}/setWebhook

echo "Bot initialized!"

uvicorn server.main:app --host 0.0.0.0 --port 8000