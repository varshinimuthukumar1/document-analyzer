import argparse
from vqa_pipeline import BLIPVQAPipeline

def main():
    parser = argparse.ArgumentParser(description='BLIP VQA CLI')
    parser.add_argument('--image', type=str, required=True, help='Path to the image file')
    parser.add_argument('--question', type=str, required=True, help='Question about the image')
    args = parser.parse_args()

    vqa = BLIPVQAPipeline()
    answer = vqa.answer_question(args.image, args.question)
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main() 