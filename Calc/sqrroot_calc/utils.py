import json
from json import JSONEncoder
from .models import Number
import cmath

class Number:
    def _init__(self, a, b, c, root1, root2):
        self.a = a
        self.b = b
        self.c = c
        # self.root1 = root1
        # self.root2 = root2
        # discrement = (b**2) - (4 * a*c)
        # root1 = (-b-cmath.sqrt(discrement))/(2 * a)
        # root2 = (-b + cmath.sqrt(discrement))/(2 * a)

    def toJSON(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)

# class NumberEncoder(JSONEncoder):
#         def default(self, obj):
#             return obj.__dict__

# number = Number.root1

# numberJSONData = json.dumps(number, cls=NumberEncoder, sort_keys=True, indent=4)
# numberJSON = json.loads(numberJSONData)

# class Number:
#     def toJSON(self):
#         return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
