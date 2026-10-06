from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def generate_caption(image):
    """
    Generate a caption for the uploaded image.
    """
    if image is None:
        return "Please upload an image."

    #image = image.open("cat.jpg").convert("RGB")
    image = image.convert("RGB")

    input = processor(images=image, return_tensors="pt").to(device)

    output = model.generate(input)
    
    caption = processor.decode(
    output[0],
    skip_special_tokens=True
    )
    return caption