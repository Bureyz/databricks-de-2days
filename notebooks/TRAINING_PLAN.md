# Day 1 – Data Engineering for Machine Learning (5h)

> **Audience:** Experienced Data Engineers new to Databricks
> **Format:** 22% Theory | 43% Demo | 30% Workshops (4 workshops)
> **Approach:** From Fundamentals to Advanced – focus on Databricks-specific features

---

## 📋 Training Checklist

| # | Module | Status | Notebook Demo | Workshop |
|---|-------|--------|---------------|----------|
| 1 | Platform Intro | ⬜ | `demo/01_platform_intro.ipynb` | - |
| 2 | Ingestion Basics | ⬜ | `demo/02_ingestion_basics.ipynb` | W1 (cleanup) |
| 3 | Data Quality | ⬜ | `demo/03_data_quality.ipynb` | - |
| 4 | Delta Lake Basics | ⬜ | `demo/04_delta_lake_basics.ipynb` | - |
| 5 | Delta Optimization | ⬜ | `demo/05_delta_lake_optimization.ipynb` | W2 (cleanup) |
| 6 | Advanced PySpark | ⬜ | `demo/06a_advanced_pyspark.ipynb` | - |
| 7 | Advanced SQL | ⬜ | `demo/06b_advanced_sql.ipynb` | - |
| 8 | Streaming & Incremental | ⬜ | `demo/07_streaming_incremental.ipynb` | - |
| 9 | Medallion Pipeline | ⬜ | `demo/08_medallion_pipeline.ipynb` | W3 → Day 2 |
| 10 | Orchestration | ⬜ | `demo/09_orchestration.ipynb` | - |
| 11 | Governance | ⬜ | `demo/10_governance.ipynb` | W4 → Day 2 |
| 12 | BI & Analytics | ⬜ | `demo/11_bi_analytics.ipynb` | - |
| 13 | AI & ML Integrations | ⬜ | `demo/12_ai_ml_integrations.ipynb` | - |

**Legend:** ⬜ Not started | 🔄 In progress | ✅ Completed

---

## 📁 Notebook Structure

```
notebooks/
├── 00_setup.ipynb                          # Participant environment validation
├── 00_pre_config.ipynb                     # Admin: create catalogs
├── TRAINING_PLAN.md                        # This file
│
├── demo/
│   ├── 01_platform_intro.ipynb
│   ├── 02a_ingestion_basics.ipynb
│   ├── 02b_data_quality.ipynb
│   ├── 03_delta_lake_basics.ipynb
│   ├── 04_delta_optimization.ipynb
│   ├── 05a_advanced_pyspark.ipynb
│   ├── 05b_advanced_sql.ipynb
│   ├── 06_streaming_incremental.ipynb
│   ├── 07_medallion_pipeline.ipynb
│   ├── 08_orchestration.ipynb
│   ├── 09_governance.ipynb
│   ├── 10_bi_analytics.ipynb
│   └── 11_ai_ml_integrations.ipynb
│
├── workshops/
│   ├── W1_ingestion_transformations.ipynb
│   ├── W2_delta_optimization.ipynb
│   ├── W3_lakeflow_pipeline.ipynb
│   └── W4_governance_security.ipynb
│
│   # Solutions are now at the end of each workshop notebook
│
└── bonus/
    ├── A_performance_tuning.ipynb
    ├── B_cicd_pipelines.ipynb
    └── C_federation_sharing.ipynb
```

---

## 📦 Datasets & Workshop Structure

### Dataset Split

| Dataset | Location | Use Case | Tables |
|---------|----------|----------|--------|
| **E-commerce (Demo)** | `dataset/demo/` | Trainer demos | customers, orders, products |
| **AdventureWorks Lite** | `dataset/workshop/` | Participant workshops | Customers, Product, SalesOrder* |

**Demo dataset (e-commerce):**
```
dataset/demo/
├── main/           # Initial data for demos
│   ├── customers/customers.csv
│   ├── orders/orders_batch.json
│   ├── orders/stream/orders_stream_001-003.json
│   └── products/products.csv
└── ingestion/      # Additional data for incremental demos
    ├── customers/customers_new.csv, customers2.csv
    └── orders/stream/orders_stream_004-015.json
```

**Workshop dataset (AdventureWorks Lite):**
```
dataset/workshop/
├── Customers.csv           # 847 rows
├── Address.csv             # Address data
├── Product.csv             # 295 products
├── ProductCategory.csv     # Categories
├── SalesOrderHeader.csv    # Orders
└── SalesOrderDetail.csv    # Order lines
```

---

### 🔧 Workshop Structure

| Workshop | Independence | Setup | Cleanup | Output for Day 2 |
|----------|--------------|-------|---------|------------------|
| **W1** Ingestion | ✅ Independent | Create tables | Drop tables | ❌ |
| **W2** Optimization | ✅ Independent | Pre-create "bad" tables | Drop tables | ❌ |
| **W3** Lakeflow | 🔗 Creates Gold | Setup pipeline | ❌ Keep! | ✅ Gold → ML |
| **W4** Governance | ✅ Independent | Create groups/users | Keep permissions | ✅ Security → ML |

---

### 📋 Workshop Details

**W1: Ingestion & Transformations** (25 min)
```
🔧 SETUP:
- Create schema: {catalog}.w1_{username}
- No pre-existing tables

📝 TASKS:
- Load AdventureWorks CSVs
- Transform: joins, aggregations
- Save as managed Delta tables

🧹 CLEANUP:
- DROP SCHEMA {catalog}.w1_{username} CASCADE
```

---

**W2: Delta Optimization** (25 min)
```
🔧 SETUP (pre-created "problem" tables):
- small_files_table: 500 tiny Parquet files
- unoptimized_table: no clustering, random order
- high_cardinality_partitioned: bad partitioning

📝 TASKS:
- DESCRIBE DETAIL → identify problems
- OPTIMIZE + Z-ORDER / Liquid Clustering
- Compare query performance before/after
- Enable Predictive Optimization

🧹 CLEANUP:
- DROP SCHEMA {catalog}.w2_{username} CASCADE
```

---

**W3: Lakeflow Pipeline** (30 min)
```
🔧 SETUP:
- Create schema: {catalog}.ecommerce_{username}
- Upload stream files to Volume

📝 TASKS:
- Create Bronze → Silver → Gold pipeline
- Use Auto Loader in STREAMING TABLE
- Add Expectations for data quality
- Enable CDC with APPLY CHANGES INTO

❌ NO CLEANUP - tables used in Day 2 ML!

📤 OUTPUT for Day 2:
- gold_customers (clean, validated)
- gold_orders (aggregated)
- gold_products (enriched)
```

---

**W4: Governance & Security** (in Demo 7)
```
🔧 SETUP:
- Create real groups: data_engineers, data_scientists, analysts
- Create test users or use existing participants

📝 TASKS:
- GRANT SELECT on Gold tables to analysts
- Create Row Filter: region-based access
- Create Column Mask: hide PII (email, phone)
- View Lineage in Unity Catalog
- Query System Tables for audit

✅ KEEP - permissions needed for Day 2 ML!

📤 OUTPUT for Day 2:
- Secure Gold layer with RLS/masking
- Groups ready for Feature Store access
```

---

### 🎯 Day 2 Handoff

Day 1 creates these assets for Day 2 (ML):

| Asset | Created in | Used in Day 2 |
|-------|------------|---------------|
| `gold_customers` | W3 | Feature Engineering |
| `gold_orders` | W3 | Feature Store |
| `gold_products` | W3 | ML Training data |
| Row Filters | W4 | Secure Feature access |
| Column Masks | W4 | PII protection in ML |
| Groups | W4 | Feature Store permissions |

---

## ⏱️ Schedule

| Czas | Moduł | Typ | Czas |
|------|-------|-----|------|
| 09:00 - 09:25 | 1. Platform Intro | Teoria + Demo | 25 min |
| 09:25 - 10:10 | 2. Ingestion & Transformations | Teoria + Demo + **W1** | 45 min |
| 10:10 - 10:25 | ☕ Przerwa | - | 15 min |
| 10:25 - 11:25 | 3. Delta Lake & Optimization | Teoria + Demo + **W2** | 60 min |
| 11:25 - 12:15 | 4. Streaming & Incremental | Teoria + Demo | 50 min |
| 12:15 - 13:00 | 🍽️ Lunch | - | 45 min |
| 13:00 - 14:00 | 5. Medallion & Lakeflow | Teoria + Demo + **W3** | 60 min |
| 14:00 - 14:25 | 6. Orchestration | Teoria + Demo | 25 min |
| 14:25 - 14:40 | ☕ Przerwa | - | 15 min |
| 14:40 - 15:05 | 7. Governance & Security | Teoria + Demo + **W4** | 25 min |
| 15:05 - 15:15 | Q&A | - | 10 min |

**Total:** 5h netto + 1h 15min przerw = 6h 15min

---

## 📚 Module Details

### 1. Introduction to Databricks Platform (25 min)

| Typ | Czas | Treść |
|-----|------|-------|
| 📖 Teoria | 10 min | Lakehouse architecture, what's different |
| 🖥️ Demo | 15 min | Workspace, UC Volumes, Serverless, AI Assistant |

**Topics:**
- Lakehouse = Data Lake + Data Warehouse (unified)
- Unity Catalog: Catalog → Schema → Table/Volume
- Unity Catalog Volumes (replaces DBFS)
- Serverless Compute vs Classic Clusters
- SQL Warehouse vs Compute Cluster
- Photon engine
- Databricks Assistant (AI code generation)

---

### 2. Data Ingestion & Transformations (45 min)

| Typ | Czas | Treść |
|-----|------|-------|
| 📖 Teoria | 5 min | Quick review |
| 🖥️ Demo | 15 min | Databricks-specific features |
| 🔧 **Workshop 1** | 25 min | Load & transform AdventureWorks data |

> 🔄 **W1 Structure:** Setup → Tasks → Cleanup (independent)

**Topics:**
- Loading CSV, JSON, Parquet
- PySpark: select, filter, join, groupBy, aggregations
- `rescuedDataColumn`, `badRecordsPath` options
- **Variant type** for semi-structured JSON
- display() and data profiling

**Delta Table Creation – Two Approaches:**
| Approach | Command | Governance |
|----------|---------|------------|
| **Managed (UC)** | `df.write.saveAsTable("catalog.schema.table")` | ✅ Full |
| **External** | `df.write.format("delta").save("/path")` | ❌ None |

⚠️ **Common Mistakes:**
- Not handling schema drift
- Ignoring NULL values early
- Using path-based tables in production

---

### 3. Delta Lake & Optimization (60 min)

| Typ | Czas | Treść |
|-----|------|-------|
| 📖 Teoria | 15 min | Delta internals, CDC/CDF, optimization |
| 🖥️ Demo | 20 min | CRUD, Time Travel, CDF, optimization |
| 🔧 **Workshop 2** | 25 min | Optimize pre-created "problem" tables |

> 🔄 **W2 Structure:** Pre-created bad tables → Diagnose → Fix → Cleanup (independent)

**Topics:**
- Delta Lake: ACID, Time Travel, RESTORE
- MERGE, UPDATE, DELETE
- Schema evolution and constraints
- CTAS (CREATE TABLE AS SELECT)
- Small File Problem & OPTIMIZE
- Z-ORDER vs Liquid Clustering
- Data Skipping & Statistics
- Auto Optimize & Predictive Optimization

**CDC vs CDF:**
| Term | What it is |
|------|------------|
| **CDC** | Change Data Capture – capturing changes FROM source systems |
| **CDF** | Change Data Feed – reading changes FROM Delta table |

```sql
-- Enable CDF
ALTER TABLE my_table SET TBLPROPERTIES (delta.enableChangeDataFeed = true);

-- Read changes
SELECT * FROM table_changes('my_table', 2)
```

---

**🗂️ Small File Problem:**

Problem: Wiele małych plików (< 128 MB) = wolne odczyty, wysokie koszty metadata.

| Stan | Wpływ |
|------|-------|
| 1000 plików × 1 MB | ❌ Slow reads, high overhead |
| 10 plików × 100 MB | ✅ Optimal performance |

**Rozwiązanie: OPTIMIZE**
```sql
-- Compact small files into larger ones
OPTIMIZE my_catalog.my_schema.my_table;

-- With predicate (optimize specific partitions)
OPTIMIZE my_table WHERE date >= '2024-01-01';

-- Check table size/files
DESCRIBE DETAIL my_table;
```

---

**📊 Data Skipping & Statistics:**

Delta automatycznie zbiera **min/max statistics** dla pierwszych 32 kolumn.
Pozwala to **pominąć** pliki które na pewno nie zawierają szukanych danych.

```sql
-- Query wykorzystuje data skipping
SELECT * FROM orders WHERE order_date = '2024-12-01';
-- Delta sprawdza min/max w każdym pliku → pomija nieistotne
```

| Statystyka | Opis |
|------------|------|
| `numRecords` | Liczba wierszy w pliku |
| `minValues` | Minimum dla każdej kolumny |
| `maxValues` | Maximum dla każdej kolumny |
| `nullCount` | Liczba NULLi |

**Optymalizacja statystyk:**
```sql
-- Compute stats for specific columns
ANALYZE TABLE my_table COMPUTE STATISTICS FOR COLUMNS col1, col2;

-- Increase columns with stats (default 32)
ALTER TABLE my_table SET TBLPROPERTIES ('delta.dataSkippingNumIndexedCols' = 50);
```

---

**🔀 Z-ORDER (legacy approach):**

Kolokacja danych wg wybranych kolumn → lepszy data skipping.

```sql
-- Z-ORDER by frequently filtered columns
OPTIMIZE my_table ZORDER BY (customer_id, order_date);
```

| Pros | Cons |
|------|------|
| ✅ Effective data skipping | ❌ Wymaga ręcznego OPTIMIZE |
| ✅ Multiple columns | ❌ Write amplification |
| ✅ Works on existing tables | ❌ Static – nie adaptuje się |

---

**💧 Liquid Clustering (recommended 2024+):**

Nowa metoda organizacji danych – **replaces partitioning + Z-ORDER**.

```sql
-- Create table with liquid clustering
CREATE TABLE my_table (
  id INT,
  customer_id STRING,
  order_date DATE,
  amount DECIMAL(10,2)
) CLUSTER BY (customer_id, order_date);

-- Change clustering keys (no rewrite!)
ALTER TABLE my_table CLUSTER BY (region, order_date);

-- Trigger clustering
OPTIMIZE my_table;
```

**Z-ORDER vs Liquid Clustering:**
| Feature | Z-ORDER | Liquid Clustering |
|---------|---------|-------------------|
| Setup | Manual OPTIMIZE | `CLUSTER BY` w DDL |
| Key changes | Full rewrite | ✅ Instant (metadata only) |
| Incremental | ❌ Rewrites all data | ✅ Only unclustered data |
| Partitioning | Needed separately | ✅ Replaces partitioning |
| Write amplification | High | Low |
| Automatic | ❌ Manual | ✅ With Predictive Opt |
| Min Databricks | Any | DBR 13.3+ |

⚠️ **Kiedy używać Z-ORDER:**
- Legacy tables
- DBR < 13.3
- Potrzebujesz zachować partitioning

✅ **Kiedy używać Liquid Clustering:**
- Nowe tabele
- DBR 13.3+
- Chcesz prostoty i automatyzacji

---

**⚡ Auto Optimize & Predictive Optimization:**

| Feature | Opis | Scope |
|---------|------|-------|
| **Auto Optimize** | Automatic file compaction on write | Table-level |
| **Optimized Writes** | Coalesce small files before write | Table-level |
| **Predictive Optimization** | Auto OPTIMIZE + VACUUM (managed) | Schema/Catalog |

```sql
-- Enable Auto Optimize (table level)
ALTER TABLE my_table SET TBLPROPERTIES (
  'delta.autoOptimize.optimizeWrite' = true,
  'delta.autoOptimize.autoCompact' = true
);

-- Enable Predictive Optimization (Unity Catalog)
ALTER SCHEMA my_schema SET PREDICTIVE OPTIMIZATION = INHERIT;
ALTER TABLE my_table SET PREDICTIVE OPTIMIZATION = ENABLE;
```

**Predictive Optimization features:**
| Action | Automatic? | Benefit |
|--------|------------|---------|
| OPTIMIZE | ✅ | No manual scheduling |
| VACUUM | ✅ | Automatic cleanup |
| ANALYZE | ✅ | Fresh statistics |

---

**🔧 Optimization Best Practices:**

| Scenario | Recommendation |
|----------|----------------|
| New tables | Liquid Clustering + Predictive Opt |
| High-cardinality filters | Liquid Clustering |
| Low-cardinality filters | Partitioning |
| Legacy tables | Z-ORDER + Auto Optimize |
| Frequent small writes | Optimized Writes = true |

**Other Optimization Features:**
- **Deletion Vectors** – soft deletes (faster DELETE/UPDATE)
- **UniForm** – Delta readable as Iceberg/Hudi
- **Photon** – vectorized query engine

```sql
-- Enable deletion vectors
ALTER TABLE my_table SET TBLPROPERTIES ('delta.enableDeletionVectors' = true);

-- Enable UniForm for Iceberg compatibility
ALTER TABLE my_table SET TBLPROPERTIES ('delta.universalFormat.enabledFormats' = 'iceberg');
```

⚠️ **Common Mistakes:**
- VACUUM with retention < 7 days → breaks time travel
- Partitioning on high-cardinality columns → too many small files
- Not enabling CDF for incremental pipelines
- Using Z-ORDER on new tables → use Liquid Clustering
- Manual OPTIMIZE on tables with Predictive Optimization → redundant
- Forgetting to run ANALYZE TABLE → stale statistics

---

### 4. Streaming & Incremental Loading (50 min)

| Typ | Czas | Treść |
|-----|------|-------|
| 📖 Teoria | 15 min | Auto Loader, COPY INTO, CTAS, Streaming |
| 🖥️ Demo | 35 min | cloudFiles, COPY INTO, schema evolution, triggers |

> ℹ️ **No separate workshop** - streaming concepts used in W3 Lakeflow Pipeline

**Topics:**
- Structured Streaming: readStream / writeStream
- Checkpointing, exactly-once semantics
- Trigger modes: AvailableNow, ProcessingTime, Continuous
- **Watermarking** – handling late arriving data
- Output Modes: append, update, complete
- State Management

**🔥 Trigger Modes (kluczowe!):**
| Trigger Mode | Opis | Use Case |
|--------------|------|----------|
| `trigger(processingTime='10 seconds')` | Micro-batch co X sekund | Real-time dashboards |
| `trigger(once=True)` | ⚠️ DEPRECATED | Migrated pipelines |
| `trigger(availableNow=True)` | Process all → stop | **Scheduled batch jobs** |
| `trigger(continuous='1 second')` | True streaming (~1ms latency) | Ultra-low latency |

```python
# Przykłady użycia
# Batch-style processing (recommended for jobs)
df.writeStream.trigger(availableNow=True).start()

# Continuous micro-batches
df.writeStream.trigger(processingTime='30 seconds').start()

# Low-latency continuous (experimental)
df.writeStream.trigger(continuous='1 second').start()
```

**📤 Output Modes:**
| Mode | Opis | Use Case |
|------|------|----------|
| `append` | Only new rows | Event logs, raw data |
| `update` | Changed rows only | Aggregations (stateful) |
| `complete` | Full result table | Small aggregations |

**🔖 Checkpointing:**
```python
df.writeStream \
  .option("checkpointLocation", "/path/to/checkpoint") \
  .start()
```
- **Exactly-once semantics** – recovery from failures
- Przechowuje: offset, state, metadata
- **WYMAGANE** dla produkcyjnych streamów!

**⏰ Watermarking (Late Data):**
```python
df.withWatermark("event_time", "10 minutes") \
  .groupBy(window("event_time", "5 minutes")) \
  .count()
```
- Definiuje jak długo czekamy na spóźnione dane
- **Bez watermark** = unbounded state = OOM!
- Typowe wartości: 10 min – 24 hours

**📊 State Management:**
- Streaming aggregations, joins = stateful
- State stored in checkpoint
- **RocksDB** state store dla dużych state'ów
- Monitoruj: `spark.sql.streaming.stateOperator.numRowsTotal`

**Ingestion Methods:**
| Method | Use Case | Incremental | Schema Evolution | Streaming |
|--------|----------|-------------|------------------|-----------|
| **CTAS** | One-time table creation | ❌ | ❌ | ❌ |
| **COPY INTO** | Batch file loading | ✅ (idempotent) | ❌ | ❌ |
| **Auto Loader** | Continuous ingestion | ✅ | ✅ | ✅ |

**Auto Loader vs COPY INTO:**
| Feature | Auto Loader | COPY INTO |
|---------|-------------|-----------|
| File discovery | Incremental (notification/listing) | Full listing |
| Billions of files | ✅ Optimized | ❌ Slow |
| Schema inference | ✅ + evolution | ✅ (no evolution) |
| Streaming | ✅ Native | ❌ Batch only |
| Checkpoint | ✅ Required | ❌ Uses table metadata |

⚠️ **Common Mistakes:**
- Using COPY INTO for continuous ingestion → use Auto Loader
- Forgetting checkpoint location → job can't recover
- No watermark = unbounded state growth → OOM
- Using `complete` mode with large datasets → memory issues
- `trigger(once=True)` deprecated → use `availableNow=True`
- Not monitoring streaming metrics → silent failures

---

### 5. Medallion Architecture & Lakeflow Pipelines (60 min)

| Typ | Czas | Treść |
|-----|------|-------|
| 📖 Teoria | 15 min | Medallion, Lakeflow Pipelines, Expectations |
| 🖥️ Demo | 15 min | Pipeline creation, Expectations, CDC |
| 🔧 **Workshop 3** | 30 min | Build Bronze→Silver→Gold pipeline |

> 🎯 **W3 Output → Day 2:** Gold tables (customers, orders, products) used for ML Feature Engineering
> ❌ **NO CLEANUP** - tables preserved for Day 2!

**Topics:**
- Bronze → Silver → Gold pattern
- **Lakeflow Declarative Pipelines** (formerly DLT)
- STREAMING TABLE vs MATERIALIZED VIEW
- **Expectations** for data quality validation
- **APPLY CHANGES INTO** – CDC with SCD Type 1/2
- Serverless Pipelines
- Pipeline Modes & Development workflow

---

**🏗️ Medallion Architecture:**

| Layer | Purpose | Data Quality | Example |
|-------|---------|--------------|---------|
| **Bronze** | Raw ingestion | As-is | `raw_orders` |
| **Silver** | Cleaned, validated | Deduplicated, typed | `clean_orders` |
| **Gold** | Business aggregates | Curated | `daily_sales` |

---

**📊 STREAMING TABLE vs MATERIALIZED VIEW:**

| Feature | STREAMING TABLE | MATERIALIZED VIEW |
|---------|-----------------|-------------------|
| Source | Streaming (append-only) | Batch or streaming |
| Processing | Incremental | Full or incremental |
| Use case | Raw data ingestion | Aggregations, joins |
| Updates | Append only | Can handle updates |
| State | Maintains checkpoint | Recomputed |

```sql
-- STREAMING TABLE - for Bronze layer (append-only sources)
CREATE OR REFRESH STREAMING TABLE bronze_orders
AS SELECT * FROM cloud_files('/data/orders', 'json');

-- MATERIALIZED VIEW - for Silver/Gold (can handle updates)
CREATE OR REFRESH MATERIALIZED VIEW silver_orders
AS SELECT *, current_timestamp() AS processed_at
FROM LIVE.bronze_orders
WHERE order_id IS NOT NULL;
```

---

**🔄 Pipeline Modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| **Triggered** | Run once, process available data, stop | Scheduled batch jobs |
| **Continuous** | Run forever, process as data arrives | Real-time pipelines |

**Development vs Production:**

| Setting | Development | Production |
|---------|-------------|------------|
| Cluster | Reused (faster iteration) | Fresh per run |
| Errors | Full stack traces | Cleaned logs |
| Tables | Can be reset | Protected |
| Cost | Lower (shared cluster) | Higher (dedicated) |

---

**✅ Lakeflow Expectations (Data Quality):**
```sql
CREATE OR REFRESH STREAMING TABLE silver_orders (
  -- Log warning, keep row
  CONSTRAINT valid_quantity EXPECT (quantity > 0),
  
  -- Drop invalid rows
  CONSTRAINT valid_price EXPECT (unit_price > 0) ON VIOLATION DROP ROW,
  
  -- Fail pipeline on violation
  CONSTRAINT valid_customer EXPECT (customer_id IS NOT NULL) ON VIOLATION FAIL UPDATE
)
AS SELECT * FROM LIVE.bronze_orders;
```

| Type | Behavior | Metrics |
|------|----------|---------|
| `EXPECT` | Log & pass | ✅ Tracked |
| `ON VIOLATION DROP ROW` | Remove bad rows | ✅ Tracked |
| `ON VIOLATION FAIL UPDATE` | Stop pipeline | ❌ Blocks |

**Viewing Expectations metrics:**
```sql
-- Query event log for expectations
SELECT * FROM event_log(TABLE(my_pipeline))
WHERE event_type = 'flow_progress'
```

---

**🔀 APPLY CHANGES INTO (CDC):**

Handles Change Data Capture with automatic SCD Type 1 or Type 2.

```sql
-- SCD Type 1 (overwrite)
APPLY CHANGES INTO LIVE.silver_customers
FROM STREAM(LIVE.bronze_customers_cdc)
KEYS (customer_id)
APPLY AS DELETE WHEN operation = 'DELETE'
SEQUENCE BY timestamp
COLUMNS * EXCEPT (operation, timestamp);

-- SCD Type 2 (history tracking)
APPLY CHANGES INTO LIVE.silver_customers
FROM STREAM(LIVE.bronze_customers_cdc)
KEYS (customer_id)
APPLY AS DELETE WHEN operation = 'DELETE'
SEQUENCE BY timestamp
COLUMNS * EXCEPT (operation, timestamp)
STORED AS SCD TYPE 2;
```

| SCD Type | Behavior | Columns Added |
|----------|----------|---------------|
| **Type 1** | Overwrite existing | None |
| **Type 2** | Keep history | `__START_AT`, `__END_AT` |

---

**⚙️ Pipeline Settings:**

```python
# Pipeline configuration (JSON)
{
  "name": "my_pipeline",
  "target": "my_catalog.my_schema",  # Where tables are created
  "continuous": false,                # Triggered mode
  "development": true,                # Dev mode
  "channel": "CURRENT",               # or "PREVIEW" for new features
  "photon": true,                     # Use Photon engine
  "serverless": true,                 # Serverless compute
  "configuration": {
    "spark.sql.shuffle.partitions": "auto"
  }
}
```

---

**📈 Pipeline Monitoring & Event Log:**

```sql
-- Access event log
SELECT * FROM event_log(TABLE(my_catalog.my_schema.my_pipeline));

-- Check data quality metrics
SELECT 
  details:flow_progress:data_quality:expectations
FROM event_log(TABLE(my_pipeline))
WHERE event_type = 'flow_progress';

-- Check pipeline performance
SELECT 
  timestamp,
  details:flow_progress:metrics:num_output_rows
FROM event_log(TABLE(my_pipeline));
```

**Key metrics to monitor:**
| Metric | Description |
|--------|-------------|
| `num_output_rows` | Rows processed |
| `expectations` | Data quality pass/fail |
| `flow_definition` | Table dependencies |
| `cluster_resources` | Compute utilization |

---

**🔄 Full Refresh vs Incremental:**

| Action | When to use |
|--------|-------------|
| **Incremental** (default) | Normal operations |
| **Full Refresh** | Schema changes, reprocessing |
| **Refresh Selection** | Specific tables only |

```sql
-- Force full refresh in SQL
CREATE OR REFRESH MATERIALIZED VIEW my_view
AS SELECT ...

-- In UI: Pipeline Settings → Full Refresh
```

⚠️ **Common Mistakes:**
- Too much logic in Bronze → keep it simple, just land data
- Not using Expectations → data quality issues go unnoticed
- Overcomplicating Silver transforms → aim for single responsibility
- Using STREAMING TABLE for data that updates → use MATERIALIZED VIEW
- Not setting SEQUENCE BY in CDC → out-of-order processing
- Ignoring event log → missing performance issues

---

### 6. Orchestration (25 min)

| Typ | Czas | Treść |
|-----|------|-------|
| 📖 Teoria | 5 min | Lakeflow Jobs |
| 🖥️ Demo | 20 min | Multi-task job, triggers |

**Topics:**
- **Lakeflow Jobs** (formerly Workflows)
- Task values for passing data between tasks
- Serverless Jobs
- Triggers: scheduled, file arrival, API
- Cost optimization: Job clusters vs All-Purpose

⚠️ **Common Mistakes:**
- Using All-Purpose clusters for jobs
- No retry policy

---

### 7. Governance & Security (25 min)

| Typ | Czas | Treść |
|-----|------|-------|
| 📖 Teoria | 5 min | Unity Catalog security |
| 🖥️ Demo | 10 min | Row Filters, Column Masks, Lineage |
| 🔧 **Workshop 4** | 10 min | Apply security to Gold tables |

> 🎯 **W4 Output → Day 2:** Secure Gold layer with RLS/masking for ML
> ✅ **KEEP** - permissions used for Feature Store access!

**Topics:**
- GRANT / REVOKE permissions
- **Row Filters** – native RLS
- **Column Masks** – native masking (PII for ML!)
- **System Tables** – audit, lineage, billing
- **Lakehouse Monitoring** – data quality & drift detection
- Git Folders for CI/CD

**W4 Tasks:**
```sql
-- Create groups (or use existing)
CREATE GROUP IF NOT EXISTS data_scientists;
CREATE GROUP IF NOT EXISTS analysts;

-- Grant access to Gold tables
GRANT SELECT ON gold_customers TO analysts;
GRANT SELECT ON gold_orders TO data_scientists;

-- Create Row Filter (region-based access)
CREATE FUNCTION region_filter(region STRING)
RETURNS BOOLEAN
RETURN region = current_user_region();

ALTER TABLE gold_customers SET ROW FILTER region_filter ON (region);

-- Create Column Mask (hide PII)
CREATE FUNCTION mask_email(email STRING)
RETURNS STRING
RETURN CASE WHEN is_member('data_scientists') THEN email ELSE '***@***.com' END;

ALTER TABLE gold_customers ALTER COLUMN email SET MASK mask_email;
```

⚠️ **Common Mistakes:**
- Exposing PII in Gold layer → use Column Masks
- No lineage tracking → enable System Tables
- Row Filters without testing → verify with different users

---

## 🎯 Output dla Day 2 (ML)

Po Day 1 uczestnicy mają:
- ✅ Czyste dane w **Gold layer** (ML-ready features)
- ✅ Pipeline z **Expectations** (validated data quality)
- ✅ **CDF enabled** for incremental feature refresh
- ✅ **Lineage** od źródła do Gold
- ✅ **Job** odświeżający dane automatycznie
- ✅ **Column Masks** dla PII (GDPR-ready)

---

## 📚 Bonus Materials (self-paced)

### A. Performance Tuning Deep Dive
- Spark UI walkthrough
- Adaptive Query Execution (AQE)
- Broadcast joins vs shuffle
- Caching strategies

### B. CI/CD for Data Pipelines
- Git Folders integration
- Databricks Asset Bundles (DABs)
- Testing notebooks with pytest
- GitHub Actions / Azure DevOps integration

### C. Data Federation & Sharing
- **Lakehouse Federation:** Query external databases
- **Lakeflow Connect:** Managed ingestion from SaaS/DBs
- **Delta Sharing:** Cross-org data sharing

---

## 🔄 Migration Guide

| From | To (Databricks) |
|------|-----------------|
| Airflow | Lakeflow Jobs |
| dbt | Lakeflow Pipelines / dbt on Databricks |
| Iceberg | Delta + UniForm |
| AWS Glue | Lakeflow Connect |
| Kafka | Auto Loader + Streaming |
| Great Expectations | Lakeflow Expectations |
| Federated queries (Presto/Trino) | Lakehouse Federation |
| Data sharing (SFTP, APIs) | Delta Sharing |
| Debezium CDC | CDF + APPLY CHANGES INTO |

---

## 📊 Time Summary

| Moduł | Teoria | Demo | Workshop | Razem |
|-------|--------|------|----------|-------|
| 1. Platform Intro | 10 | 15 | - | 25 |
| 2. Ingestion & Transform | 5 | 15 | 25 (W1) | 45 |
| 3. Delta & Optimization | 15 | 20 | 25 (W2) | 60 |
| 4. Streaming | 15 | 35 | - | 50 |
| 5. Medallion & Lakeflow | 15 | 15 | 30 (W3) | 60 |
| 6. Orchestration | 5 | 20 | - | 25 |
| 7. Governance | 5 | 10 | 10 (W4) | 25 |
| Q&A | - | - | - | 10 |
| **TOTAL** | **70** | **130** | **90** | **300** |

| Typ | Czas | % |
|-----|------|---|
| 📖 Teoria | 70 min | 23% |
| 🖥️ Demo | 130 min | 43% |
| 🔧 Workshop | 90 min | 30% |
| Q&A | 10 min | 3% |

**Workshop Structure:**
| Workshop | Time | Cleanup | Output → Day 2 |
|----------|------|---------|----------------|
| W1: Ingestion | 25 min | ✅ Yes | ❌ |
| W2: Optimization | 25 min | ✅ Yes | ❌ |
| W3: Lakeflow | 30 min | ❌ No | ✅ Gold tables |
| W4: Governance | 10 min | ❌ No | ✅ Permissions |

---

## ✏️ Notes

*Use this section for training-specific notes, changes, or participant feedback.*

---

**Last updated:** 2025-12-06
