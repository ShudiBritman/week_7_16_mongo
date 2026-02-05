from fastapi import FastAPI
from dal import *
import uvicorn
from db import init_db


app = FastAPI()
    
@app.on_event("startup")
async def lifespan():
    init_db()



@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/employees/engineering/high-salary")
async def engineering_high_salary_employees():
    return  get_engineering_high_salary_employees()


@app.get("/employees/by-age-and-role")
async def employees_by_age_and_role():
    return get_employees_by_age_and_role()


@app.get("/employees/top-seniority")
async def top_seniority_employees_excluding_hr():
    return get_top_seniority_employees_excluding_hr()


@app.get("/employees/age-or-seniority")
async def mployees_by_age_or_seniority():
    return get_employees_by_age_or_seniority()


@app.get("/employees/managers/excluding-departments")
async def managers_excluding_departments():
    return get_managers_excluding_departments()

@app.get("/employees/by-lastname-and-age")
async def employees_by_lastname_and_age():
    return get_employees_by_lastname_and_age()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)