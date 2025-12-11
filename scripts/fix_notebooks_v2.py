import os

base_dir = "/Users/kzb/Praca/Szkolenia/Altcom/Databricks/Data Enginner TwoDays/notebooks/demo"

renames = {
    "02a_ingestion_basics.ipynb": "02_ingestion_basics.ipynb",
    "02b_data_quality.ipynb": "03_data_quality.ipynb",
    "05a_advanced_pyspark.ipynb": "06a_advanced_pyspark.ipynb",
    "05b_advanced_sql.ipynb": "06b_advanced_sql.ipynb",
    "06_streaming_incremental.ipynb": "07_streaming_incremental.ipynb",
    "07_medallion_pipeline.ipynb": "08_medallion_pipeline.ipynb",
    "08_orchestration.ipynb": "09_orchestration.ipynb",
    "09_governance.ipynb": "10_governance.ipynb",
    "10_bi_analytics.ipynb": "11_bi_analytics.ipynb",
    "11_ai_ml_integrations.ipynb": "12_ai_ml_integrations.ipynb"
}

print("--- Renaming files ---")
for old, new in renames.items():
    old_path = os.path.join(base_dir, old)
    new_path = os.path.join(base_dir, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old} -> {new}")
    else:
        print(f"Skipped (not found): {old}")

print("\n--- Splitting Delta Lake notebook ---")
delta_path = os.path.join(base_dir, "03_delta_lake_optimization.ipynb")

if os.path.exists(delta_path):
    with open(delta_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find split point at "# 6. Optimization"
    split_index = -1
    for i, line in enumerate(lines):
        if "# 6. Optimization" in line:
            # Backtrack to find the start of the cell
            for j in range(i, -1, -1):
                if "<VSCode.Cell" in lines[j]:
                    split_index = j
                    break
            break
    
    if split_index != -1:
        # Part 1: Basics
        part1 = lines[:split_index]
        
        # Part 2: Optimization
        part2_content = lines[split_index:]
        
        # Extract setup cells to prepend to Part 2
        setup_lines = []
        setup_start = -1
        setup_end = -1
        
        # Find cell with %run ../00_setup
        for i, line in enumerate(lines):
            if "%run ../00_setup" in line:
                for j in range(i, -1, -1):
                    if "<VSCode.Cell" in lines[j]:
                        setup_start = j
                        break
                for j in range(i, len(lines)):
                    if "</VSCode.Cell>" in lines[j]:
                        setup_end = j + 1
                        break
                break
        
        if setup_start != -1 and setup_end != -1:
            setup_lines.extend(lines[setup_start:setup_end])
            
        # Find cell with imports
        config_start = -1
        config_end = -1
        for i, line in enumerate(lines):
            if "from pyspark.sql import functions" in line:
                for j in range(i, -1, -1):
                    if "<VSCode.Cell" in lines[j]:
                        config_start = j
                        break
                for j in range(i, len(lines)):
                    if "</VSCode.Cell>" in lines[j]:
                        config_end = j + 1
                        break
                break
        
        if config_start != -1 and config_end != -1:
            setup_lines.extend(lines[config_start:config_end])
            
        part2 = setup_lines + part2_content
        
        with open(os.path.join(base_dir, "04_delta_lake_basics.ipynb"), "w", encoding="utf-8") as f:
            f.writelines(part1)
        print("Created: 04_delta_lake_basics.ipynb")
            
        with open(os.path.join(base_dir, "05_delta_lake_optimization.ipynb"), "w", encoding="utf-8") as f:
            f.writelines(part2)
        print("Created: 05_delta_lake_optimization.ipynb")
            
        os.remove(delta_path)
        print("Removed old file: 03_delta_lake_optimization.ipynb")
    else:
        print("Error: Split point '# 6. Optimization' not found")
else:
    print("Error: 03_delta_lake_optimization.ipynb not found")
