import json
from json import JSONEncoder
from sqrroot_calc.models import Number

# class Number:
#     def _init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

# class NumberEncoder(JSONEncoder):
#         def default(self, o):
#             return o.__dict__

# number = Number()

# numberJSONData = json.dumps(number, cls=NumberEncoder, sort_keys=True, indent=4)
# numberJSON = json.loads(numberJSONData)

class Number:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)