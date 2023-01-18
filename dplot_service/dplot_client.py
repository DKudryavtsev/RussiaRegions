import sys
import pandas as pd
import requests
import json

# Data readout
if len(sys.argv) != 5:
    raise TypeError(
        "Syntax should be:\n"
        "dplot_client.py file.csv regions_col feature_col port"
        )
file, regions, feature, port = sys.argv[1:]
df = pd.read_csv(file)
data = json.dumps(
    {'region': df[regions].to_list(), str(feature): df[feature].to_list()})
   
# POST request to the local server, the endpoint 'plot'
url = 'http://localhost:' + str(port) + '/plot'
r = requests.post(url, json=data)
    
# Response processing
print('Status code: {}'.format(r.status_code))
if r.status_code == 200:
    print('Data have been sent')
else:
    print(r.text)