import json

data = {}
data['label_1'] = 1
data['label_2'] = 2.5
data['label_4'] = [1, 'two']
data['label_3'] = 'value 3'


with open('output.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True)
