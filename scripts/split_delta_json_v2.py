import json
import os
import copy

base_dir = "/Users/kzb/Praca/Szkolenia/Altcom/Databricks/Data Enginner TwoDays/notebooks/demo"
source_path = os.path.join(base_dir, "03_delta_lake_optimization.ipynb")
target_basics = os.path.join(base_dir, "03_delta_lake_basic.ipynb")
target_opt = os.path.join(base_dir, "04_delta_lake_optimization.ipynb")

if not os.path.exists(source_path):
    print(f"Error: Source file {source_path} does not exist.")
    exit(1)

with open(source_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

cells = notebook['cells']
split_index = -1

# Find the split point
for i, cell in enumerate(cells):
    source = cell.get('source', [])
    # Source is a list of strings
    source_text = "".join(source)
    if "# 6. Optimization" in source_text:
        split_index = i
        break

if split_index == -1:
    print("Error: Could not find split point '# 6. Optimization'")
    # Print first few cells to debug
    for i in range(min(5, len(cells))):
        print(f"Cell {i}: {cells[i].get('source', [])}")
    exit(1)

print(f"Found split point at cell index {split_index}")

# Identify setup cells (imports, config)
setup_cells = []
for i in range(split_index):
    cell = cells[i]
    source_text = "".join(cell.get('source', []))
    # Copy cells that look like setup/config
    if "%run" in source_text or "import" in source_text or "spark.conf.set" in source_text or "CATALOG" in source_text:
        setup_cells.append(cell)

print(f"Identified {len(setup_cells)} setup cells to copy to the second notebook.")

# Create Part 1: Basics
notebook_basics = copy.deepcopy(notebook)
notebook_basics['cells'] = cells[:split_index]

# Create Part 2: Optimization
notebook_opt = copy.deepcopy(notebook)
# Prepend setup cells to the optimization part
notebook_opt['cells'] = setup_cells + cells[split_index:]

# Save files
with open(target_basics, 'w', encoding='utf-8') as f:
    json.dump(notebook_basics, f, indent=2)
print(f"Created {target_basics}")

with open(target_opt, 'w', encoding='utf-8') as f:
    json.dump(notebook_opt, f, indent=2)
print(f"Created {target_opt}")

# Verify file creation and delete original
if os.path.exists(target_basics) and os.path.exists(target_opt):
    print("Success: Both files created.")
    os.remove(source_path)
    print(f"Removed original file: {source_path}")
else:
    print("Error: Failed to create output files.")
