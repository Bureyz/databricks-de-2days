import json
import os

def fix_setup():
    filepath = "notebooks/00_setup.ipynb"
    with open(filepath, 'r') as f:
        nb = json.load(f)
    
    # Find the cell
    found = False
    for cell in nb['cells']:
        source = "".join(cell['source'])
        if "STEP 5: Export Variables" in source:
            new_source = [
                "# =============================================================================\n",
                "# STEP 5: Export Variables (Summary)\n",
                "# =============================================================================\n",
                "\n",
                "# Create aliases for workshops (backward compatibility)\n",
                "catalog = CATALOG\n",
                "schema = DEFAULT_SCHEMA\n",
                "volume_path = DATASET_BASE_PATH\n",
                "\n",
                "print(\"=\" * 60)\n",
                "print(\"TRAINING ENVIRONMENT READY\")\n",
                "print(\"=\" * 60)\n",
                "print()\n",
                "print(f\"User:              {raw_user}\")\n",
                "print(f\"CATALOG:           {CATALOG}\")\n",
                "print(f\"BRONZE_SCHEMA:     {BRONZE_SCHEMA}\")\n",
                "print(f\"SILVER_SCHEMA:     {SILVER_SCHEMA}\")\n",
                "print(f\"GOLD_SCHEMA:       {GOLD_SCHEMA}\")\n",
                "print(f\"DATASET_BASE_PATH: {DATASET_BASE_PATH}\")\n",
                "print()\n",
                "print(\"--- Workshop Aliases ---\")\n",
                "print(f\"catalog:           {catalog}\")\n",
                "print(f\"schema:            {schema}\")\n",
                "print(f\"volume_path:       {volume_path}\")\n",
                "print(\"=\" * 60)\n"
            ]
            cell['source'] = new_source
            found = True
            break
    
    if found:
        with open(filepath, 'w') as f:
            json.dump(nb, f, indent=1)
        print(f"Fixed {filepath}")
    else:
        print(f"Could not find cell in {filepath}")

def fix_w3():
    filepath = "notebooks/workshops/W3_lakeflow_pipeline.ipynb"
    with open(filepath, 'r') as f:
        nb = json.load(f)
    
    # Find the cell with source_path definition
    found = False
    for cell in nb['cells']:
        source = "".join(cell['source'])
        if "TODO: PASTE THE PATH" in source or "source_path =" in source:
            # We look for the cell that defines source_path
            if "import dlt" in source:
                new_source = [
                    "import dlt\n",
                    "from pyspark.sql.functions import *\n",
                    "\n",
                    "# Path to the workshop source data (defined in the setup cell above)\n",
                    "source_path = f\"{volume_path}/lakeflow_workshop_source\"\n",
                    "\n",
                    "# ==========================================\n",
                    "# BRONZE LAYER\n",
                    "# ==========================================\n",
                    "\n",
                    "# TODO: Define bronze_customers\n",
                    "# @dlt.table\n",
                    "# def bronze_customers():\n",
                    "#   return (\n",
                    "#     spark.readStream.format(\"cloudFiles\")\n",
                    "#       .option(\"cloudFiles.format\", \"csv\")\n",
                    "#       .load(f\"{source_path}/Customers\")\n",
                    "#   )\n",
                    "\n",
                    "# TODO: Define bronze_products\n",
                    "\n",
                    "# TODO: Define bronze_sales (SalesOrderDetail)\n",
                    "\n",
                    "\n",
                    "# ==========================================\n",
                    "# SILVER LAYER\n",
                    "# ==========================================\n",
                    "\n",
                    "# TODO: Define silver_customers (Expect EmailAddress IS NOT NULL)\n",
                    "\n",
                    "# TODO: Define silver_products (Expect Name IS NOT NULL)\n",
                    "\n",
                    "# TODO: Define silver_sales (Expect OrderQty > 0)\n",
                    "\n",
                    "\n",
                    "# ==========================================\n",
                    "# GOLD LAYER\n",
                    "# ==========================================\n",
                    "\n",
                    "# TODO: Create dim_product (SCD Type 1)\n",
                    "# dlt.create_streaming_table(\"dim_product\")\n",
                    "# dlt.apply_changes(...)\n",
                    "\n",
                    "# TODO: Create dim_customer (SCD Type 2)\n",
                    "# dlt.create_streaming_table(\"dim_customer\")\n",
                    "# dlt.apply_changes(..., stored_as_scd_type = 2)\n",
                    "\n",
                    "# TODO: Create fact_sales\n",
                    "# @dlt.table\n",
                    "# def fact_sales():\n",
                    "#     # Read silver_sales\n",
                    "#     # Join with dim_product (current records only)\n",
                    "#     pass\n"
                ]
                cell['source'] = new_source
                found = True
                break
    
    if found:
        with open(filepath, 'w') as f:
            json.dump(nb, f, indent=1)
        print(f"Fixed {filepath}")
    else:
        print(f"Could not find cell in {filepath}")

if __name__ == "__main__":
    fix_setup()
    fix_w3()
