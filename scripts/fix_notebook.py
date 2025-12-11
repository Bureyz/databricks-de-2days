import json

notebook_path = '/Users/kzb/Praca/Szkolenia/Altcom/Databricks/Data Engineer OneDay/notebooks/demo/07_governance.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

print(f"Total cells before: {len(nb['cells'])}")

# Keep only the first 110 cells
nb['cells'] = nb['cells'][:110]

print(f"Total cells after: {len(nb['cells'])}")

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=2)
