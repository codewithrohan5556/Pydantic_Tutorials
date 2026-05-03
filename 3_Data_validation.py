from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

# Writing Production grade codes
# Step 1 Define Schema
class Patient(BaseModel):
    # name : str = Field(max_length=50)  
    name : Annotated[str,Field(max_length=50,title='Name',description='Name of the patient',examples=['nitish'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt=0,lt=120)
    # weight :float = Field(gt=0,description='weight in kg') # to attach meta data
    weight : Annotated[float,Field(gt=0,strict=True,description='weight in kg',default=None)]
    # married : bool = False
    married : Annotated[bool,Field(default=None,description='Is the patient married or not')]
    # allergies : Optional[List[str]] = Field(max_length=5) 
    allergies : Annotated[Optional[List[str]],Field(max_length=5,default=None)]
    contact_details : Dict[str,str] 

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
    print(patient.email)
    print(patient.linkedin_url)
    print('updated')  

patient_info = {'name':'nitish','email':'abc@gmail.com','linkedin_url':'https://www.linkedin.com/in/nitish-kumar-07b5b31b5/','age':30,'weight':65.5,'contact_details':{'phone':'1234567890'}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
