# A field validator is a method that lets you add custom validation logic to a specific field(single) in a Pydantic model...

from pydantic import BaseModel, field_validator, Field, EmailStr
from typing import List, Dict, Annotated


class Patient(BaseModel):
    name : str
    age : int
    height : float
    weight : float
    contact : Dict[str, str]
    email : EmailStr

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain!!!")
        
        return value



def show_details(p1 : Patient):
    print("Successfully entered!!!")


patient1 = {"name":"AKR", "age":17, "height":1.73, "weight":57.3, "contact":{"mobile":"324252"}, "email":"jack13423@hdfc.com"}

p1 = Patient(**patient1)

show_details(p1)