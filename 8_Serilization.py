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

temp = patient1.model_dump()
# temp = patient1.model_dump(include=['name','age'])
# temp = patient1.model_dump(exclude=['name','age'])
# temp = patient1.model_dump(exclude={'address':['state']})

print(temp)
print(type(temp))

# Convert to JSON
import json
json_str = patient1.model_dump_json()
print(json_str)
print(type(json_str))
