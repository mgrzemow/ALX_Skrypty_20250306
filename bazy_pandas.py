import pprint
import pandas as pd
import json

from sqlalchemy import create_engine

# https://docs.sqlalchemy.org/en/20/core/engines.html

engine = create_engine('sqlite:///baza.db')
df = pd.read_sql('select * from osoby', engine)
x = df.head(13).to_json(orient='values')
pprint.pprint(json.loads(x))
