RUN using below command
uv run uvicorn app.main:app --reload

PREREQ:
Need Gemini API Key 
Set it using $env:GOOGLE_API_KEY="AIXXXXXXXXXXXXXXXXXXX"

Once Up go to http://localhost:8000/docs and execute the endpoint POST: /generate
