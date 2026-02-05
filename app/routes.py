from fastapi import APIRouter
from dal import *



router = APIRouter()


router.get("/employees/engineering/high-salary")
async def engineering_high_salary_employees():
    return engineering_high_salary_employees()


router.get("/employees/by-age-and-role")
async def employees_by_age_and_role():
    return employees_by_age_and_role()


router.get("/employees/top-seniority")
async def top_seniority_employees_excluding_hr():
    return get_top_seniority_employees_excluding_hr()


router.get("/employees/age-or-seniority")
async def mployees_by_age_or_seniority():
    return get_employees_by_age_or_seniority()


router.get("/employees/managers/excluding-departments")
async def managers_excluding_departments():
    return get_managers_excluding_departments()

router.get("/employees/by-lastname-and-age")
async def employees_by_lastname_and_age():
    return get_employees_by_lastname_and_age()