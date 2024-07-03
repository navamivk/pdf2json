from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
        raise ValueError("OpenAI API key in environment variables")

client = OpenAI(
  api_key=openai_api_key,  
)

class ResumeParser:
    @staticmethod
    def parse_resume_to_json(text):

        # OpenAI API Prompt
        response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                        "role": "system",
                        "content": """ Extract the following resume details into JSON format with the following fields:
                        {{
                            "personal_info": {{
                                "name": "",
                                "title": "",
                                "email": "",
                                "phone": "",
                                "location": ""
                                "github_url": "",
                                "linkedin_url": ""
                                "portfolio_website_url": "",
                                "summary/objective": ""

                            }},
                            "education": [
                                {{
                                    "institution": "",
                                    "degree": "",
                                    "field_of_study": "",
                                    "duration": "",
                                    "grade": ""
                                }}
                            ],
                            "work_experience": [
                                {{
                                    "job_title": "",
                                    "company": "",
                                    "location": "",
                                    "duration": "",
                                    "job_summary": "",
                                }}
                            ],
                            "skills": [""],
                            "projects": [
                                {{
                                    "name": "",
                                    "description": "",
                                    "technologies_used": []
                                }}
                            ],
                            "certifications": [
                                {{
                                    "name": "",
                                    "issuing_organization": "",
                                    "issue_date": "",
                                    "expiration_date": ""
                                }}
                            ],
                            "extra_curriculars": [
                                {{
                                    "name": "",
                                    "position": "",
                                    "duration": "",
                                    "description": ""
                                }}
                            ],
                            "relevant_coursework": [""],
                            
                        }}"""
                        },
                        {
                        "role": "user",
                        "content": text
                        }
                    ],
                    temperature=0.5,
                    max_tokens=64,
                    top_p=1
                    )
        
        return response.choices[0].message.strip()
