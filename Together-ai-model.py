from together import Together

client = Together(api_key="61e81c4489100adb5b8058155bd0c8c1325f33645a9269f703acfca6a8e94f8e")
prompt_file_path = "z txt files/prompt.txt"  # Replace with your file path
input_file_path = "z txt files/input.txt"

# Read the content of the prompt file with utf-8 encoding
with open(prompt_file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Read the content of the input file with utf-8 encoding
with open(input_file_path, "r", encoding="utf-8") as file:
    file_input = file.read()

# Get the response from the model
response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[{"role": "user", "content": f"{file_content} \n\n {file_input}"}],
)

# Function to save the response to a text file
def save_response_to_txt(file_path, response_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response_content)

# Save the response content to a text file
save_response_to_txt('z txt files/output.txt', response.choices[0].message.content)

# Optionally, print the response for debugging
print(response.choices[0].message.content)
