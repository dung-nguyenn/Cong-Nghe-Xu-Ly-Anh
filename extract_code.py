import json

with open('Rice_Leaf_Detection.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

with open('train.py', 'w', encoding='utf-8') as f:
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            f.write(source + '\n\n')
