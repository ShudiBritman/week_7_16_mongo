from fastapi import APIRouter
from dal import *



router = APIRouter('/employees')


router.get("/engineering/high-salary")
def engineering_high_salary_employees():
    return engineering_high_salary_employees()


