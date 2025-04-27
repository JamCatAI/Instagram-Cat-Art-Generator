import requests
import base64
import os

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def generate_art(input_image_path, prompt):
    with open(input_image_path, "rb") as image_file:
        image_data = image_file.read()

    payload = {
        "inputs": prompt,
        "options": {"use_gpu": True},
        "parameters": {"image": base64.b64encode(image_data).decode('utf-8')}
    }

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    generated_image_data = base64.b64decode(result['generated_image_base64'])

    output_path = f"generated_art/{os.path.basename(input_image_path)}"
    with open(output_path, "wb") as f:
        f.write(generated_image_data)

    return output_path
