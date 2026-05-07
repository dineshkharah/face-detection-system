import mediapipe as mp

mp_face_detection = mp.solutions.face_detection

face_detector = mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5
)


def detect_face(image_np):
    results = face_detector.process(image_np)

    if results.detections:
        detection = results.detections[0]

        bbox = detection.location_data.relative_bounding_box

        return {
            "x": bbox.xmin,
            "y": bbox.ymin,
            "width": bbox.width,
            "height": bbox.height,
        }

    return None
