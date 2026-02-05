from fastapi import APIRouter
from dal import *



router = APIRouter('/employees')


router.get("/engineering/high-salary")
def engineering_high_salary_employees():
    return engineering_high_salary_employees()


router.get("/by-age-and-role")
def employees_by_age_and_role():
    return employees_by_age_and_role()