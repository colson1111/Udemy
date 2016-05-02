# Lecture 26 - JSON with Python

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

json_obj = """
{     "zoo_animal": "Lion",
      "food": ["Meat", "Veggies", "Honey"],
      "fur": "Golden",
      "clothes": null,
      "diet": [{"zoo_animal": "Gazelle", "food":"grass","fur":"brown"}]
}
"""

import json

# open json object
data = json.loads(json_obj)
data

# save json object
json.dumps(data)

dframe = DataFrame(data['diet'])
dframe


