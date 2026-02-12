# A Model Validator validates the entire model**, not just one field.
# Use it when: 1. You need to compare multiple fields  2. Validation depends on more than one value


from pydantic import BaseModel, model_validator, Field, EmailStr
from typing import List, Dict, Annotated


class Patient(BaseModel):
    name : str
    age : int
    height : float
    weight : float
    contact : Dict[str, str]
    email : EmailStr

    
    @model_validator(mode = "after")
    def check_age_contact(self):

        if self.age > 60 and 'emergency' not in self.contact:
            raise ValueError("Age above 60 and no emergency contact available!!!")
        return self


def show_details(p1 : Patient):
    print("Successfully entered!!!")


patient1 = {"name":"AKR", "age":67, "height":1.73, "weight":57.3, "contact":{"emergency":"324252"}, "email":"jack13423@hdfc.com"}

p1 = Patient(**patient1)

show_details(p1)