import torch
from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load the model and processor
processor = DonutProcessor.from_pretrained("huggingface/donut-base")
model = VisionEncoderDecoderModel.from_pretrained("huggingface/donut-base")

def extract_text(image_path):
    # Load image
    image = Image.open(image_path).convert("RGB")

    # Preprocess image
    pixel_values = processor(image, return_tensors="pt").pixel_values

    # Generate predictions
    with torch.no_grad():
        outputs = model.generate(pixel_values)

    # Decode predictions
    decoded_output = processor.decode(outputs[0], skip_special_tokens=True)

    return decoded_output
