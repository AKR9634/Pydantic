# In Pydantic, a Field is used to provide extra information and validation rules for model attributes...

from pydantic import BaseModel, Field
from typing import List, Annotated

class Patient(BaseModel):

    name:str = Field(max_length=7)
    age:int = Field(gt=13, le=80)
    height:Annotated[float, Field(le=3, description="The Height should be in metres!!!", examples=[1.24, 2.34, 5.67])]
    weight:Annotated[float, Field(strict= True, description="The weight should be in kgs!!!", examples=[56, 43.6,67.7])]
    hobby:Annotated[List[str], Field(default=None, max_length=3, description="Only three hobbies to be specified!!!")]


def print_details(p1:Patient):
    print("Data Validation Successful!!!")

patient1 = {"name":"AKR", "age":17, "height":"1.73", "weight":57.3}

p1 = Patient(**patient1)

print_details(p1)

