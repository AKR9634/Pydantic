# A Computed Field is a field that:
    # * is not stored.
    # * is calculated from other fields.
    # * is not included when you serialize the model (model_dump()).


# A Model Validator validates the entire model**, not just one field.
# Use it when: 1. You need to compare multiple fields  2. Validation depends on more than one value


from pydantic import BaseModel, model_validator, Field, EmailStr, computed_field
from typing import List, Dict, Annotated


class Patient(BaseModel):
    name : str
    age : int
    height : float
    weight : float
    contact : Dict[str, str]
    email : EmailStr

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)

        return bmi


def show_details(p1 : Patient):
    print("Successfully entered!!!")
    print(f"The bmi of the patient is {p1.bmi}")


patient1 = {"name":"AKR", "age":67, "height":1.73, "weight":57.3, "contact":{"emergency":"324252"}, "email":"jack13423@hdfc.com"}

p1 = Patient(**patient1)

show_details(p1)