from pydantic import BaseModel
from typing import List,Dict,Optional

# Req/Opt feild,default values
# Step 1 Define Schema
class Patient(BaseModel):
    name : str  
    age : int
    weight :float
    married : bool = False
    allergies : Optional[List[str]] = None # two level validation
    contact_details : Dict[str,str] # two level validation

# Step 2 Use Schema
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')  

patient_info = {'name':'nitish','age':30,'weight':65.5,'contact_details':{'email':'abc@gmial.com','phone':'1234567890'}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
