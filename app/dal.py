from connection import MongoConnection
from pprint import pprint
import os


collection = MongoConnection().get_collection()

def get_engineering_high_salary_employees():
    query = {'salary':{'$gt': 65000}, 'job_role.title':'Engineer'}
    projection = {'employee_id':1, 'name':1, 'salary':1, '_id':0}
    cursor = list(collection.find(query, projection))
    return cursor


def get_employees_by_age_and_role():
    query = {'age':{'$gte':30, '$lte':45}, 'job_role.title':{'$in':['Engineer', 'Specialist']}}
    cursor = list(collection.find(query))
    return cursor



def get_top_seniority_employees_excluding_hr():
    query = {'job_role.title':{'$nin':['HR']}}
    cursor = list(collection.find(query).limit(7).sort({'years_at_company':-1}))
    return cursor



def get_employees_by_age_or_seniority():
    query = {'$or':[{'age': {'$gt':50}}, {'years_at_company':{'$lt':3}}]}
    projection = {'employee_id':1, 'name':1, 'age':1, 'years_at_company':1, '_id':0}
    cursor = list(collection.find(query, projection))
    return cursor



def get_managers_excluding_departments():
    query = {'job_role.title':'Manager', 'job_role.department':{'$nin':['Sales', 'Marketing']}}
    cursor = list(collection.find(query))
    return cursor



def get_employees_by_lastname_and_age():
    #query = {'name':{'$or':[{'$regex':'Wright'}, {'$regex':'Nelson'}]}, 'age':{'$lt':35}}
    query = {'$or':[{'name':{'$regex':'Wright$'}}, {'name':{'$regex':'Nelson$'}}], 'age':{'$lt':35}}
    projection = {'name':1, 'age':1, 'job_role.department':1, '_id':0}
    cursor = list(collection.find(query, projection))
    return cursor
