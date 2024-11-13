from ultralytics import YOLO
import cv2


def detect_plants(image_input, model_path):
    # Load the model
    model = YOLO(model_path)

    # Perform inference on the input image
    results = model(source=image_input, show=True)
    cv2.waitKey(0)

    # Extract plant names from detection results
    plant_names = []
    for result in results:
        for detection in result.boxes:
            class_id = int(detection.cls)  # Get class ID
            plant_name = model.names[class_id]  # Map class ID to name using model's names attribute
            plant_names.append(plant_name)

    return plant_names
