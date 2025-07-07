# VLM_DocAnalyzer: BLIP Visual Question Answering

This project demonstrates a simple Visual Language Model (VLM) pipeline using BLIP for answering questions about images.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Download a sample image:**
   Place an image (e.g., `sample.jpg`) in the `data/` directory.

## Usage

Run the CLI to answer a question about an image:

```bash
python src/main.py --image data/sample.jpg --question "What is in the picture?"
```

## Project Structure

- `src/vqa_pipeline.py`: Core BLIP VQA logic
- `src/main.py`: CLI entry point
- `data/`: Place your test images here
- `requirements.txt`: Dependencies

## Model

- Uses [Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base) from HuggingFace Transformers 