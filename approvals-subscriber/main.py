from fastapi import FastAPI, Request
import base64

app = FastAPI()

@app.post("/pubsub/push")
async def pubsub_push(request: Request):
    envelope = await request.json()
    if not envelope:
        return {"status": "no message"}

    pubsub_message = envelope["message"]
    data = base64.b64decode(pubsub_message["data"]).decode("utf-8")
    attributes = pubsub_message.get("attributes", {})

    print("📩 Received message:", data, attributes)

    # Later: write to Firestore
    return {"status": "processed"}