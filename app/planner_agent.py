from dotenv import load_dotenv
import json,re
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0,api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = PromptTemplate.from_template("""
Convert the user request into a structured slide plan.

Return ONLY valid JSON.

Rules:
- Do not include explanations
- Do not include markdown
- Output must start with {{ and end with }}

Example format:

{{
 "slides":[
   {{
     "type":"title",
     "title":"Example Title",
     "subtitle":"Example Subtitle"
   }},
   {{
     "type":"bullet",
     "title":"Key Points",
     "points":["point1","point2"]
   }}
 ]
}}

User request:
{input}
Charts must use this format:

"data": {{
 "2020": 3,
 "2021": 6,
 "2022": 10
}}
""")

def create_slide_plan(user_input):

    chain = prompt | llm

    result = chain.invoke({"input": user_input})
    if not result.content:
        raise ValueError("Empty LLM response")
    print("LLM RESPONSE:")
    print(result.content)
    return extract_json(result.content)

def extract_json(text):

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in model output")

    return json.loads(match.group())