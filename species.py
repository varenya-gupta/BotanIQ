import os  # For checking if the file exists
from ultralytics import YOLO
import cv2

def detect_plants(image_input, model_path, confidence_threshold=0.6):
    # Check if the input image exists
    if not os.path.exists(image_input):
        print(f"Error: The image file '{image_input}' does not exist.")
        return []

    # Load the model
    model = YOLO(model_path)

    # Perform inference on the input image
    results = model(source=image_input, show=True)
    cv2.waitKey(0)

    # Extract plant names from detection results, filtered by confidence threshold
    plant_names = []
    for result in results:
        for detection in result.boxes:
            # Get the confidence score (probability of correct classification)
            confidence = detection.conf

            # Only accept detections with confidence > threshold
            if confidence > confidence_threshold:
                class_id = int(detection.cls)  # Get class ID
                plant_name = model.names[class_id]  # Map class ID to name using model's names attribute
                plant_names.append((plant_name, confidence))  # Store plant name and confidence
    plants = []
    if plant_names:
        print("Detected plants (Confidence > 50%):")
        for plant, confidence in plant_names:
            if confidence >= 0.6:
                print(f"{plant} with confidence {confidence}")
                plants.append(plant)
            else:
                print("No plants detected with confidence > 50%.")



    return plants

#Example usage:
image_input = r"C:\Users\nalin\Downloads\snake-plant-care-overview-1902772-04-d3990a1d0e1d4202a824e929abb12fc1-349b52d646f04f31962707a703b94298.jpeg"  # Your image file path
model_path = "runs/detect/train3/weights/best.pt"  # Path to the model

#Check and process
print(detect_plants(image_input, model_path))



