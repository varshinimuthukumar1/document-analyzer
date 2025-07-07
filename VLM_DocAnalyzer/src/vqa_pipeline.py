import torch
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering
import os

class BLIPVQAPipeline:
    def __init__(self, model_name='Salesforce/blip-vqa-base', device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForQuestionAnswering.from_pretrained(model_name).to(self.device)

    def answer_question(self, image_path, question):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
        image = Image.open(image_path).convert('RGB')
        inputs = self.processor(image, question, return_tensors="pt").to(self.device)
        out = self.model.generate(**inputs)
        answer = self.processor.decode(out[0], skip_special_tokens=True)
        return answer 