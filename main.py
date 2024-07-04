import json
from pdf2text import TextExtractor
from resume_parser import JSONConverter
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Convert a resume PDF to JSON format.")
    parser.add_argument("input_pdf", help="Path to the input resume PDF.")
    parser.add_argument("output_dir", help="Directory to store the output JSON file.")
    args = parser.parse_args()

    input_pdf_path = args.input_pdf
    output_dir = args.output_dir


    extractor = TextExtractor()
    text = extractor.extract_text_from_pdf(input_pdf_path)

    parser = JSONConverter()
    resume_json = parser.parse_resume_to_json(text)

    output_json_path = os.path.join(output_dir, "resume.json")

    with open(output_json_path, 'w') as json_file:
        json.dump(json.loads(resume_json), json_file, indent=2)

if __name__ == "__main__":
    main()
