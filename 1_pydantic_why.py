# Type Validation

def insert_patient_data(name:str,age:int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('inserted into database')
    else:
        raise TypeError("Incorret datatype")

def update_patient_data(name:str,age:int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError("Incorret datatype")

insert_patient_data('nitish',32)
update_patient_data('nitish',32)

# Data Validation

def insert_patient_data(name:str,age:int):

    if type(name) == str and type(age) == int:
        if age<0:
            raise ValueError("Age cannot be negative")
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError("Incorret datatype")

def update_patient_data(name:str,age:int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError("Incorret datatype")

insert_patient_data('nitish',32)
update_patient_data('nitish',32)




