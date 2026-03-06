from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

def validate_plan(plan):

    for slide in plan["slides"]:

        if slide["type"] == "bullet":

            if len(slide["points"]) > 6:
                slide["points"] = slide["points"][:6]

        if slide["type"] == "chart":

            if len(slide["data"]) < 2:
                raise ValueError("Chart needs at least 2 points")

    return plan