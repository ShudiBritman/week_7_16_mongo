from fastapi import APIRouter, HTTPException
from dal import *

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)


@router.get("/engineering/high-salary")
async def engineering_high_salary_employees():
    try:
        return get_engineering_high_salary_employees()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/by-age-and-role")
async def employees_by_age_and_role():
    try:
        return get_employees_by_age_and_role()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/top-seniority")
async def top_seniority_employees_excluding_hr():
    try:
        return get_top_seniority_employees_excluding_hr()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/age-or-seniority")
async def employees_by_age_or_seniority():
    try:
        return get_employees_by_age_or_seniority()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/managers/excluding-departments")
async def managers_excluding_departments():
    try:
        return get_managers_excluding_departments()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/by-lastname-and-age")
async def employees_by_lastname_and_age():
    try:
        return get_employees_by_lastname_and_age()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
