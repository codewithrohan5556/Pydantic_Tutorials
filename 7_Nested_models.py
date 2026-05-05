# Better organization of related data (eg. vitals,address,insurance)
# Reusability: use vitals in multiple models(e.g Patient,Medical Record)
# Readability : Easier for developers and API consumers to understand
# Validation : Nested models are validated automatically no extra work needed

from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name: str
    gender : str
    age: int
    address : Address 

address_dict = {'city' : 'bangalore', 'state' : 'karnataka', 'pin' : '560001'}

address1 = {'name' : 'nitish', 'gender' : 'male', 'age' : 25, 'address' : address_dict}

patient_dict = {'name' : 'nitish', 'gender' : 'male', 'age' : 25, 'address' : address_dict}

patient1 = Patient(**patient_dict)
print(patient1.address)