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

# c = collection.find()
# pprint(list(c))
pprint(get_employees_by_age_and_role())