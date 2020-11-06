
from faker import Faker

def getProfile():
    fake = Faker()
    return fake.profile()

from employee_api.models import Employee
from employee_api import db
import os
def seedData():
    for seed_num in range(10):
        data = getProfile()
        print(os.environ.get('DATABASE_URL'))
        print(data['name'],data['job'])
        employee = Employee(
            data['name'],\
            data['sex'],\
            data['address'],\
            data['job'],\
            data['mail'])

        db.session.add(employee)
        db.session.commit()
        
seedData()
