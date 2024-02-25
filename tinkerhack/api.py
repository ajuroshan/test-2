from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def process_form_data(name: str, email: str, feedback: str):
    # Here you can process the form data as needed, such as saving it to a database
    return {"name": name, "email": email, "feedback": feedback}

@app.post("/api/submit_form")
async def submit_form(request: Request):
    form_data = await request.form()
    name = form_data.get("name")
    email = form_data.get("email")
    feedback = form_data.get("feedback")
    form_result = process_form_data(name, email, feedback)
    print(form_result)
    return JSONResponse(content=form_result)
