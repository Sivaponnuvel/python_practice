# 🔹 Question 1
# 👉 Create a dictionary with:
# name
# age
# city
# 👉 Convert it to JSON
# 👉 Print it

import json
person = {'name':'Siva','age': 23,'city':'Chennai'}
a = json.dumps(person)
print(a)


# 🔹 Question 2
# 👉 Take a JSON string
# 👉 Convert it into Python dictionary
# 👉 Print each value separately

import json
user = '{"name": "Siva", "age": 23, "city": "Chennai"}'
a = json.loads(user)
print(f"Name: {a['name']}")
print(f"Age: {a['age']}")
print(f"City: {a['city']}")