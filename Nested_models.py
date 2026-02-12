# Why nested models are used?
#    * Better organization of related data (e.g. vitals, address, insurance).
#    * Reusability: Use Vitals in multiple models (e.g. Patient, MedicalRecord).
#    * Readability: Easier for developers and API consumers to understand.
#    * Validation: Nested models are validated automatically, no extra work needed.


from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    pincode:str


class Student(BaseModel):
    name:str
    age:int
    address:Address


a1 = {"street":"ABC", "city":"DEF", "pincode":"246149"}
address1 = Address(**a1)

s1 = {"name":"AKR", "age":17, "address":address1}
student1 = Student(**s1)

# To serialize .i.e. converting a model instance into a dictionary, JSON string, or other format.
temp = student1.model_dump_json()
print(temp)

print(type(temp))
