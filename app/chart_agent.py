from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import json
import re

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt = PromptTemplate.from_template("""
You receive a slide plan.

Add chart data if a slide type is "chart".

Return JSON only.

Slide plan:
{input}
""")

def extract_json(text):

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found")

    return json.loads(match.group())


def create_chart_plan(plan):

    chain = prompt | llm

    result = chain.invoke({"input": json.dumps(plan)})

    return extract_json(result.content)