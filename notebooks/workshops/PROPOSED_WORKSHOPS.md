# Proposed Additional Workshops

Based on the existing curriculum, here are 5 additional workshops to deepen the Data Engineering knowledge:

## 1. Streaming & Incremental Processing
**Objective:** Master real-time data processing patterns.
**Topics:**
- Structured Streaming basics (Sources, Sinks, Triggers).
- Advanced Auto Loader (Schema Evolution, Rescue Data).
- Handling late data with Watermarking.
- Stream-Stream Joins.
**Scenario:** Build a real-time dashboard for order status updates.

## 2. Data Quality & Testing
**Objective:** Ensure reliability of data pipelines.
**Topics:**
- Unit testing PySpark transformations (using `pytest`).
- Implementing Data Quality checks (Great Expectations or DLT Expectations).
- Monitoring and Alerting on quality failures.
**Scenario:** Build a robust pipeline that quarantines bad data instead of failing.

## 3. Orchestration with Databricks Workflows
**Objective:** Move from interactive notebooks to production jobs.
**Topics:**
- Creating Multi-Task Jobs.
- Passing parameters between tasks (Task Values).
- Error handling and retries.
- Git integration (CI/CD basics).
**Scenario:** Orchestrate the entire Medallion pipeline (Ingest -> Transform -> Aggregation) as a scheduled job.

## 4. Advanced Performance Tuning
**Objective:** Optimize Spark jobs for scale.
**Topics:**
- Understanding the Spark UI (DAGs, Stages, Tasks).
- Handling Data Skew (Salting).
- Join Strategies (Broadcast vs Shuffle).
- Caching and Persistence strategies.
**Scenario:** Debug and optimize a slow-running query on a large dataset.

## 5. ML Integration for Data Engineers
**Objective:** Bridge the gap between DE and ML.
**Topics:**
- Feature Store basics (Creating and writing to feature tables).
- Using MLflow models as UDFs for inference.
- Batch inference pipelines.
**Scenario:** Enrich the customer table with a "Churn Prediction Score" using a pre-trained model.
