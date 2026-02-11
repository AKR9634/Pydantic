# Pydantic
This repository contains the code i learnt through my Pydantic learning process....



How?

1. Define a Pydantic model that represents the ideal schema of the data. This includes the expected fields, their types, and any validation constraints (e.g. gt=0 for positive numbers).

2. Instantiate the model with raw input data (usually a dictionary or JSON-like structure). Pydantic will automatically validate the data and coerce it into the correct Python types (if possible). If the data doesn't meet the model's requirements. Pydantic raises a ValidationError.

3. Pass the validated model object to functions or use it throughout your codebase. This ensures that every part of your program works with clean, type-safe and logically valid data.


# Pydnatc is a Python library which helps in type/data validation since Python is a dynamic typed language...

# def insert_patient_data(name:str, age:int):

#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print("Inserted successfully!!!")
#     else:
#         raise TypeError("Incorrect data type!!!")
    
# insert_patient_data("akr", 30)

# The above approach is very hectic and needs a lot of code...
