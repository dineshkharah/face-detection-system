from fastapi import WebSocket
from PIL import Image
import numpy as np
import io

from app.face_detection import detect_face
from app.image_utils import draw_bbox


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_bytes()

        image = Image.open(io.BytesIO(data)).convert("RGB")

        image_np = np.array(image)

        bbox = detect_face(image_np)

        if bbox:
            processed_image = draw_bbox(image_np, bbox)

            output = Image.fromarray(processed_image)

            buffer = io.BytesIO()

            output.save(buffer, format="JPEG")

            await websocket.send_bytes(buffer.getvalue())

        else:
            await websocket.send_bytes(data)
