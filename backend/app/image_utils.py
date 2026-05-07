from PIL import Image, ImageDraw
import numpy as np


def draw_bbox(image_np, bbox):
    height, width, _ = image_np.shape

    x = int(bbox["x"] * width)
    y = int(bbox["y"] * height)

    w = int(bbox["width"] * width)
    h = int(bbox["height"] * height)

    image = Image.fromarray(image_np)

    draw = ImageDraw.Draw(image)

    draw.rectangle([x, y, x + w, y + h], outline="red", width=3)

    return np.array(image)
