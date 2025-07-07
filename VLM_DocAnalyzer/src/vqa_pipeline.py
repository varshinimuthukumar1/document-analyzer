import torch
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering
import os

class BLIPVQAPipeline:
    def __init__(self, model_name='Salesforce/blip-vqa-base', device=None):
        
    def answer_question(self, image_path, question):
        