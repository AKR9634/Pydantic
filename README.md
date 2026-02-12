# 📘 Pydantic Learning Repository

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-green)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

This repository contains the code I learned throughout my **Pydantic learning process**.

It demonstrates how Pydantic helps in **data validation, type enforcement, and schema definition** in Python.

---

## 🚀 Why Pydantic?

Python is a **dynamically typed language**, which means it does not strictly enforce data types at runtime.

**Pydantic** solves this problem by providing:

* ✔️ Data validation
* ✔️ Type coercion
* ✔️ Clear schema definition
* ✔️ Automatic error handling

---

## 📌 How Pydantic Works

### 1️⃣ Define a Model

Define a Pydantic model that represents the ideal schema of the data.

This includes:

* Expected fields
* Their types
* Validation constraints (e.g., `gt=0` for positive numbers)

---

### 2️⃣ Instantiate the Model with Raw Data

Pass raw input data (dictionary or JSON-like structure) into the model.

Pydantic will:

* Automatically validate the data
* Convert it into correct Python types (if possible)
* Raise a `ValidationError` if the data doesn't meet requirements

---

### 3️⃣ Use the Validated Model

Pass the validated model object throughout your codebase.

This ensures:

* Clean data
* Type-safe data
* Logically valid data

---

## 🔍 Traditional Approach (Without Pydantic)

Without Pydantic, validation can become verbose and repetitive:

```python
def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted successfully!!!")
    else:
        raise TypeError("Incorrect data type!!!")

insert_patient_data("akr", 30)
```

⚠️ The above approach is very hectic and requires a lot of manual validation code.

---

## 🎯 Purpose of This Repository

This repository showcases:

* My learning journey with Pydantic
* Practical validation examples
* Cleaner and more scalable data handling techniques

---

## ⭐ If You Find This Helpful

Feel free to:

* Star ⭐ the repository
* Fork 🍴 it
* Explore and experiment

---

💡 *Learning never stops — keep building!*
