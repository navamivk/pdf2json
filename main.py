import json
from pdf2text import TextExtractor
from resume_parser import ResumeParser

def main():
    pdf_path = "navami_vipith_resume.pdf"
    output_json_path = "resume.json"

    extractor = TextExtractor()
    text = extractor.extract_text_from_pdf(pdf_path)

    parser = ResumeParser()
    resume_json = parser.parse_resume_to_json(text)

    with open(output_json_path, 'w') as json_file:
        json.dump(json.loads(resume_json), json_file, indent=4)

if __name__ == "__main__":
    main()
