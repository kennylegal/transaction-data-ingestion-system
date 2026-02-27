# Real-Time Wallet & Trading Ingestion System

A **production-grade real-time ingestion platform** for a digital wallet / trading system, built with **PostgreSQL, Debezium, and Apache Kafka**.  
This project demonstrates the full **ingestion phase**: from database changes to streaming events, schema evolution, reliability, observability, and event-driven architecture.

---

## 🔥 Project Overview

This system simulates a fintech environment where users can:

- Register and complete KYC verification
- Deposit, withdraw, and transfer funds
- Execute trades
- Trigger fraud detection and alerts

Instead of building UI, this project focuses on **how data flows in real time from operational databases to consumers**.

Key features:

- Change Data Capture (CDC) using **Debezium**
- Log-based ingestion with **PostgreSQL WAL**
- Event streaming with **Apache Kafka**
- Schema management using **Confluent Schema Registry**
- Fault-tolerant, observable, production-ready design
- Outbox pattern implementation for event-driven architecture

---

## 🏗 Architecture

```text
          ┌───────────┐
          │   Users   │
          └─────┬─────┘
                │
          ┌─────▼─────┐
          │ PostgreSQL│
          │ (OLTP DB) │
          └─────┬─────┘
                │ WAL
          ┌─────▼─────┐
          │ Debezium  │
          │ Connector │
          └─────┬─────┘
                │
        ┌───────▼────────┐
        │ Apache Kafka   │
        │  Topics        │
        └───────┬────────┘
  ┌───────────────┴───────────────┐
  │ Consumers / Services           │
  │ - Fraud Detection              │
  │ - Portfolio / Risk Engine      │
  │ - Analytics / Dashboard        │
  │ - Notifications / Alerts       │
  │ - Data Warehouse Loader        │
  └────────────────────────────────┘
```

---

## 📂 Database Tables

| Table            | Purpose                                       | Debezium Capture | Topic | Consumers |
|-----------------|-----------------------------------------------|----------------|-------|-----------|
| `users`         | User master data & KYC                        | ✅ Yes         | users | Analytics, Identity Service, Notification |
| `wallets`       | User balances (state table)                   | Optional       | wallets | Dashboard, Monitoring |
| `transactions`  | User deposits, withdrawals, transfers         | ✅ Yes         | transactions | Fraud Detection, Analytics, Ledger Builder |
| `trades`        | Executed trades                               | ✅ Yes         | trades | Risk Engine, Portfolio Service, Analytics |
| `fraud_flags`   | Fraud detection results                        | ✅ Yes         | fraud_flags | Compliance, Notification Service, Analytics |

> ⚡ **Tip:** For production-grade systems, consider using an **`outbox_events` table** for capturing all business events instead of streaming every table.

---

## ⚡ Key Concepts Demonstrated

1. **Change Data Capture (CDC)**  
   - Captures INSERT, UPDATE, DELETE in real time.  
   - Avoids full table polling.

2. **Log-Based Ingestion (WAL)**  
   - Reads PostgreSQL Write-Ahead Log (WAL) for exact, ordered changes.  
   - Ensures low-latency, high-fidelity event streaming.

3. **Debezium Connector**  
   - Streams WAL changes into Kafka topics.  
   - Supports snapshot + streaming phases.

4. **Kafka Event Streaming**  
   - Topics, partitions, keys, consumer groups.  
   - At-least-once or exactly-once semantics.  
   - Fault-tolerant and scalable.

5. **Schema Management**  
   - Avro/Protobuf integration.  
   - Schema Registry for backward/forward compatibility.  
   - Handles schema evolution without breaking consumers.

6. **Reliability & Observability**  
   - Dead-letter topics for failed messages.  
   - Idempotent consumers.  
   - Lag monitoring and replication slot monitoring.  
   - Prometheus + Grafana metrics.

7. **Advanced Patterns**  
   - Outbox pattern to prevent dual writes.  
   - Event-driven architecture for derived services like fraud detection.

---

## 🛠 Technology Stack

| Layer                 | Technology                                     |
|-----------------------|-----------------------------------------------|
| Database              | PostgreSQL                                    |
| CDC Engine            | Debezium                                      |
| Event Streaming       | Apache Kafka                                  |
| Schema Management     | Confluent Schema Registry                     |
| Metrics & Observability | Prometheus, Grafana                          |
| Containerization      | Docker, Docker Compose                         |
| Programming Language  | Python (Kafka consumers, analytics)           |

---

## ⚙ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/wallet-trading-ingestion.git
cd wallet-trading-ingestion
```

### 2. Run Docker Compose
```bash
docker-compose up -d
```
This spins up:

- PostgreSQL with WAL logical replication enabled
- Kafka & Zookeeper
- Debezium connectors
- Schema registry

### 3. Configure Debezium Connectors
- Connect to `users`, `transactions`, `trades` tables.
- Optional: `wallets`, `fraud_flags`.

### 4. Run Consumers
- Python consumers to process topics:
  - Fraud detection
  - Portfolio calculation
  - Dashboard analytics

---

## 🏃 Example Flow

1. Insert transaction:
```sql
INSERT INTO transactions (user_id, type, amount, status) VALUES (1, 'deposit', 50000, 'completed');
```

2. WAL records change → Debezium streams → Kafka topic `transactions`

3. Consumers process:
- Fraud detection evaluates risk
- Portfolio updates balance
- Notification triggers alert
- Data warehouse ingests for analytics

---

## 📈 Observability

- Monitor **Kafka consumer lag**
- Monitor **replication slot lag**
- WAL disk usage & retention
- Debezium connector status
- Prometheus metrics visualized in Grafana

---

## 🧠 Learning Outcomes

After completing this project, you will understand:

- Full lifecycle of ingestion phase
- Snapshot vs streaming in Debezium
- WAL & logical decoding mechanics
- How to design event-driven systems
- How to handle schema evolution
- Reliability, retries, idempotency, and fault tolerance
- Monitoring, alerting, and operational challenges

---

## 📌 Future Improvements

- Add multiple currencies & forex conversion
- Implement exactly-once semantics end-to-end
- Simulate high-frequency trades (10k+ TPS)
- Build real-time fraud scoring ML service
- Add data masking & security compliance for PII

---

## 📜 References

- [Debezium Documentation](https://debezium.io/documentation/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [PostgreSQL WAL & Logical Replication](https://www.postgresql.org/docs/current/wal-intro.html)
- Confluent Schema Registry Documentation

---

## 📝 License

MIT License

