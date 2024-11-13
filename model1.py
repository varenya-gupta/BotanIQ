from species import detect_plants

# Define the model path and image input
model_input = "m2.pt"
image_input = "C:/Users/STUDENT/Downloads/51gSdI0nbXL._AC_UF1000,1000_QL80_.jpg"  # Replace with your image path

# Detect plants
detected_plants = detect_plants(image_input, model_input)
print("Detected Plants:", detected_plants)
