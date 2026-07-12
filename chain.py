import os
from pydantic import SecretStr
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        groq_api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(
            model='openai/gpt-oss-120b',
            temperature=0,
            api_key=SecretStr(groq_api_key) if groq_api_key else None
        )
    
    def extract_jobs(self, cleaned_text):
        prompt_extract= PromptTemplate.from_template("""
        ### SCRAPED TEXT FROM WEBSITE:
        {data}
        ### INSTRUCTIONS:

            The scraped text is from a job posting page or careers page of a website.

            Your task is to extract ONLY the primary job posting that the user is currently viewing.

            Ignore all other content, including:
            - Related or recommended jobs
            - Other job listings
            - Navigation menus
            - Headers and footers
            - Company information not related to the current job
            - Advertisements and promotional content

            Return exactly one JSON object with the following keys:
            - "role"
            - "experience"
            - "skills" (as a JSON array of strings)
            - "description"

            If any field is unavailable, return an empty string for that field. If no skills are explicitly listed, infer the most relevant technical or professional skills from the job description.

            Return ONLY valid JSON with no additional text, explanations, or markdown.

            ### VALID JSON (NO PREAMBLE):                             
        """
)

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"data": cleaned_text})
        json_parser = JsonOutputParser()
        try:
            parsed = json_parser.parse(res.content) if isinstance(res.content, str) else res.content
        except OutputParserException:
            raise OutputParserException("Output too big. Unable to parse the jobs.")
        return parsed if isinstance(parsed, list) else [parsed]
    
    def write_email(self, job, links):
        prompt_email= PromptTemplate.from_template("""
        ### JOB DESCRIPTION:
        {job_description}
                                                
        ### INSTRUCTIONS:
        You are Arbaz Aslam, a AI Engineer and a Data Scientist.
        Having Experience in AI Automation, Gen AI, and Agentic AI,
        where you made multiple Automation projects which help
        bussinesses save countless hours of manual work.
        You are applying for the job described above.                                           
        Your job is ko write a cold email to the client 
        regarding the job mentioned above describing the capability
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase my portfolio: {link_list}
        Remember you are Arbaz Aslam, a AI Engineer and a Data Scientist.                                             
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
                                                
        """)

        chain_email = prompt_email | self.llm
        res = chain_email.invoke(
        input={
            "job_description": str(job),
            "link_list": links
        }
        )
        return (res.content)


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))