from connection import MongoConnection
from utils import serialize_docs


def get_collection():
    return MongoConnection().get_collection()


def get_engineering_high_salary_employees():
    collection = get_collection()
    query = {'salary': {'$gt': 65000}, 'job_role.title': 'Engineer'}
    projection = {'employee_id': 1, 'name': 1, 'salary': 1, '_id': 0}
    cursor = list(collection.find(query, projection))
    return serialize_docs(cursor)


def get_employees_by_age_and_role():
    collection = get_collection()
    query = {
        'age': {'$gte': 30, '$lte': 45},
        'job_role.title': {'$in': ['Engineer', 'Specialist']}
    }
    cursor = list(collection.find(query))
    return serialize_docs(cursor)


def get_top_seniority_employees_excluding_hr():
    collection = get_collection()
    query = {'job_role.title': {'$ne':'HR'}}
    cursor = collection.find(query).sort('years_at_company', -1).limit(7)
    return serialize_docs(list(cursor))


def get_employees_by_age_or_seniority():
    collection = get_collection()
    query = {'$or': [{'age': {'$gt': 50}}, {'years_at_company': {'$lt': 3}}]}
    projection = {
        'employee_id': 1,
        'name': 1,
        'age': 1,
        'years_at_company': 1,
        '_id': 0
    }
    cursor = list(collection.find(query, projection))
    return serialize_docs(cursor)


def get_managers_excluding_departments():
    collection = get_collection()
    query = {
        'job_role.title': 'Manager',
        'job_role.department': {'$nin': ['Sales', 'Marketing']}
    }
    cursor = list(collection.find(query))
    return serialize_docs(cursor)


def get_employees_by_lastname_and_age():
    collection = get_collection()
    query = {
        '$or': [
            {'name': {'$regex': 'Wright$'}},
            {'name': {'$regex': 'Nelson$'}}
        ],
        'age': {'$lt': 35}
    }
    projection = {
        'name': 1,
        'age': 1,
        'job_role.department': 1,
        '_id': 0
    }
    cursor = list(collection.find(query, projection))
    return serialize_docs(cursor)
