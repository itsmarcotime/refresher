# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#sample json
userJSON = '{"first_name": "Marco", "last_name": "Mata", "age": 30}'

# parse to dict
user = json.loads(userJSON)
# print(user['first_name'])

# print(user)

car ={'make': 'ford', 'model': 'mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)