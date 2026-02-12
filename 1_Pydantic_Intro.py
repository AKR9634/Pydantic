from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class patient(BaseModel):

    name:str
    age:int
    weight:float
    height:float
    allergies:List[str]
    contact:Dict[str, str]
    hobby:Optional[bool] = None
    email:EmailStr
    linkedin:AnyUrl

def print_data(p1 : patient):

    print(p1.name)
    print(p1.age)
    print(p1.hobby)
    print("Successful!!!")

patient_data = {"name" : "AKR", "age" : "30", "weight":72.3, "height":1.73, "allergies":["abc1", "abc2"], "contact":{"phone1":"1234"}, "email":"jack123@gmail.com", "linkedin":"http://linkedin.com/3213"}

patient1 = patient(**patient_data)

print_data(patient1)
