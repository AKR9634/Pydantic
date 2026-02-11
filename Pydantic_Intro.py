from pydantic import BaseModel
from typing import List, Dict

class patient(BaseModel):

    name:str
    age:int
    weight:float
    height:float
    allergies:List[str]
    contact:Dict[str, str]

def print_data(p1 : patient):

    print(p1.name)
    print(p1.age)
    print("Successful!!!")

patient_data = {"name" : "AKR", "age" : "30", "weight":72.3, "height":1.73, "allergies":["abc1", "abc2"], "contact":{"phone1":"1234"}}

patient1 = patient(**patient_data)

print_data(patient1)
