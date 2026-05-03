from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict


class Patient(BaseModel):

    name: str
    email : EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]  # ✅ removed extra brackets
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_vaildator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Invalid email domain')
        return value

    @field_validator('name',mode='after')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else: 
            raise ValueError("Age should be in between 0 and 100")
                

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')


patient_info = {
    'name': 'nitish',
    'email': 'abc@hdfc.com',
    'age': '30',
    'weight': 65.5,
    'married': True,        
    'allergies': ['dust'],  
    'contact_details': { 'phone': '1234567890'}
}

patient1 = Patient(**patient_info)  # validation -> type coercion
update_patient_data(patient1)