---
date: 2026-07-19
tags: [azure, certification, az-900, compute]
---

# AZ-900: Compute Services (35-40% of Exam, Part 2)

---

## 1. Compute Type Comparison

| | VMs (IaaS) | Containers | Functions (Serverless) |
|:--|:--|:--|:--|
| **Control** | Full OS control | App + dependencies | Code only |
| **Management** | You patch/update OS | You manage app | Cloud manages everything |
| **Scaling** | Manual or scale sets | Orchestrator (AKS) | Automatic |
| **Billing** | Per second of VM runtime | Per second of container runtime | Per execution + resource usage |
| **Startup** | Minutes | Seconds | Milliseconds |
| **Use when** | Full control, custom OS | Portable, microservices | Event-driven, short tasks |

---

## 2. Virtual Machines (VMs)

**Service model:** IaaS

Azure VMs give you full control over the OS. You install software, configure settings, and manage patches (unless using automatic guest patching).

**Required resources for a VM:**
- **OS Disk** (managed disk for the operating system)
- **Virtual Network (VNet) + Subnet** (network connectivity)
- **vNIC** (virtual network interface card, attaches the VM to the VNet)
- **Optional:** Data disks, Public IP address, NSG for filtering traffic

### VM Scaling and Resiliency Options

| Feature | What It Does |
|:--|:--|
| **VM Scale Sets** | Deploy and manage a group of **identical**, load-balanced VMs. Auto-scale in/out based on demand (CPU, memory, schedule). |
| **Availability Sets** | Protects VMs **within a datacenter**. Spreads VMs across **Fault Domains** (separate racks, different power/network) and **Update Domains** (separate groups rebooted in sequence during planned maintenance). SLA: 99.95% when ≥2 VMs. |
| **Availability Zones** | Protects against **datacenter failure**. VMs spread across physically separate datacenters in a region. SLA: 99.99% when ≥2 VMs across zones. |

> **Availability Set vs Availability Zone:** Set = protect from hardware failure in same datacenter. Zone = protect from entire datacenter going offline.

### Azure Virtual Desktop

- Delivers a full Windows desktop experience from the cloud.
- Users connect via any device (Windows, Mac, iOS, Android, browser).
- Benefit: centralized management, security (data stays in cloud), session-based pricing.
- Service model: Combination of IaaS (for the host VMs) and managed service.

---

## 3. Containers

Containers package an app and its dependencies into a single lightweight unit. They share the host OS kernel, making them faster to start and more portable than VMs.

| Service | Description | Use When |
|:--|:--|:--|
| **Azure Container Instances (ACI)** | Run a single container without managing servers. Fastest way to run a container in Azure. No orchestration. | Quick tests, simple tasks, burst workloads |
| **Azure Kubernetes Service (AKS)** | Managed Kubernetes service. Orchestrate containers at scale with auto-scaling, rolling updates, service discovery. | Production container workloads, microservices |
| **Azure Container Apps** | Serverless containers. Built on Kubernetes but abstracts it away. Auto-scales, supports Dapr, event-driven. | Modern apps, event-driven containers |

---

## 4. App Service (PaaS)

Azure App Service is a fully managed platform for hosting web applications, REST APIs, and mobile backends.

- **No OS management** — Azure handles patching, load balancing, auto-scaling.
- Supports multiple languages: .NET, Java, Node.js, Python, PHP, Ruby.
- **App Service Plan:** Defines the underlying compute resources (VM tier, scale count, region).
- Deploy via Git, GitHub Actions, Azure DevOps, FTP, or ZIP.
- **Auto-scaling** available (based on schedule or metrics).

---

## 5. Serverless Compute

Serverless means: you write the code, the cloud handles everything else. You **never** see or manage a server. **Pay per execution** — no charges when idle.

| Service | Description |
|:--|:--|
| **Azure Functions** | Run code in response to triggers (HTTP request, timer, blob upload, queue message). Supports multiple languages. Stateless by default; Durable Functions for stateful. |
| **Azure Logic Apps** | Build workflows visually with 200+ connectors. No code required. Trigger-based (e.g., "When an email arrives, save attachment to Blob Storage"). |

**Functions vs Logic Apps:**
- Functions = code-first, more control. Logic Apps = designer-first, less control, faster workflow building.

---

## 6. Azure Batch

Runs large-scale parallel and HPC (High-Performance Computing) batch jobs in Azure.

- Creates and manages a pool of VMs automatically.
- Installs applications and stages data.
- Runs jobs, scales nodes, handles failures and re-queues.
- Use when you need to run the same task across thousands of VMs (rendering, financial modeling, genomic analysis).

---

## 7. App Hosting Options — Quick Decision Map

| Your Requirement | Use |
|:--|:--|
| Lift-and-shift legacy app, need full OS control | Azure VMs |
| Web app, API, don't want to manage OS | Azure App Service |
| Microservices, portable across environments | AKS (Kubernetes) |
| Simple container, no orchestration needed | ACI |
| Event-driven, short-running code, pay-per-use | Azure Functions |
| Visual workflow with SaaS connectors | Azure Logic Apps |
| Large-scale parallel compute jobs | Azure Batch |
| Deliver Windows desktops to remote users | Azure Virtual Desktop |
| Identical VMs that must auto-scale | VM Scale Sets |

---

## 8. AI, Machine Learning, and IoT/Edge Services

These are mentioned in the official syllabus. Expect to recognize the names and purposes.

| Service | Purpose |
|:--|:--|
| **Azure Machine Learning** | Platform for training and deploying ML models (PaaS). |
| **Azure Cognitive Services** | Pre-built AI APIs: vision, speech, language, decision. |
| **Azure Bot Service** | Build intelligent chatbots. |
| **Azure IoT Hub** | Managed service to connect, monitor, and manage billions of IoT devices. Bidirectional communication. |
| **Azure IoT Central** | SaaS-based IoT app platform. Build IoT solutions without deep cloud expertise. |
| **Azure Sphere** | End-to-end IoT security: secured MCU/OS + cloud service. |
| **Azure IoT Edge** | Run cloud workloads (AI, analytics) on IoT devices locally. |

---

## 9. VM Series, Dedicated Hosts, Isolated VMs

### VM Series (SKU Families)

| Series | Category | Use Case |
|:--|:--|:--|
| **A-series** | Entry-level | Dev/test, low traffic |
| **B-series** | Burstable | Idle most of the time, burst occasionally (web servers, small DBs) |
| **D-series** | General purpose | Balanced CPU-to-memory. Most common workload type. |
| **E-series** | Memory optimized | High memory-to-CPU. SAP HANA, in-memory databases. |
| **F-series** | Compute optimized | High CPU-to-memory. Batch, web servers, gaming. |
| **H-series** | HPC | High-performance compute. Simulations, modeling. |
| **L-series** | Storage optimized | High disk throughput. Big data, NoSQL. |
| **M-series** | Large memory | Up to ~12 TB RAM. Very large databases. |
| **N-series** | GPU | Graphics, deep learning, visualization. |

### Azure Dedicated Host

- A **physical server** dedicated entirely to your organization (not shared).
- You control maintenance windows.
- Useful for: compliance, regulatory requirements, BYOL licensing.
- Billed per host regardless of how many VMs you run.

### Isolated VM Sizes

- Specific VM sizes (e.g., M128s, E64is_v3) that get an **entire physical server** to themselves.
- Same benefit as Dedicated Host but managed as individual VM sizes.

> **Dedicated Host vs Isolated VM:** Dedicated Host = rent the whole server, place VMs on it. Isolated VM = specific VM size guarantees the whole server is yours.

---

## 10. Database Services

Azure offers multiple managed database options. Know what each is for.

| Service | Type | Description | Use Case |
|:--|:--|:--|:--|
| **Azure SQL Database** | PaaS (relational) | Fully managed SQL Server in the cloud. Auto-patching, backups, scaling. Single database or elastic pool. | Modern cloud apps needing SQL Server without managing servers |
| **Azure SQL Managed Instance** | PaaS (relational) | Full SQL Server instance compatibility with near-100% feature parity. VNet-based. Supports SQL Agent, cross-db queries, CLR. | Lift-and-shift of on-prem SQL Server with minimal changes |
| **Azure Cosmos DB** | PaaS (NoSQL) | Globally distributed, multi-model NoSQL database with single-digit-millisecond latency. Supports SQL, MongoDB, Cassandra, Gremlin, Table APIs. 99.999% SLA. Selectable consistency levels (strong, bounded staleness, session, eventual, consistent prefix). | Global-scale apps, IoT, gaming, real-time personalization |
| **Azure Database for MySQL** | PaaS (relational) | Managed MySQL community edition. Built-in HA, auto-backup, scaling. | LAMP stack apps, WordPress, existing MySQL workloads |
| **Azure Database for PostgreSQL** | PaaS (relational) | Managed PostgreSQL. Supports Hyperscale (Citus) for distributed queries across nodes. | Geo-spatial apps, analytics, existing PostgreSQL workloads |
| **Azure Database for MariaDB** | PaaS (relational) | Managed MariaDB community edition. | MySQL-compatible workloads (MariaDB fork) |

**SQL Database vs Managed Instance:**
- SQL Database: simplified, not 100% SQL Server compatible, multi-tenant.
- Managed Instance: near-full SQL Server surface area, VNet-isolated (your own instance).

**Cosmos DB key exam points:**
- Multi-model (document, key-value, graph, column-family)
- Global distribution — replicate to any Azure region
- Five consistency levels (trade-off between performance and consistency)
- Serverless and provisioned throughput modes

---

## 11. Big Data & Analytics Services

| Service | Description | Use Case |
|:--|:--|:--|
| **Azure Synapse Analytics** | Unified analytics platform: dedicated SQL pools (data warehousing), serverless SQL, Apache Spark pools, and data integration pipelines. Formerly SQL Data Warehouse. | Enterprise data warehousing, large-scale analytics, BI |
| **Azure Databricks** | Apache Spark-based analytics platform optimized for Azure. Collaborative notebooks, built-in ML integration, Delta Lake for reliable data lakes. | Data engineering, data science, ML training |
| **Azure HDInsight** | Managed open-source analytics clusters: Hadoop, Spark, Kafka, HBase, Storm, Hive LLAP. Lift and shift existing Hadoop workloads. | Lift-and-shift Hadoop, open-source analytics |
| **Azure Data Factory** | Cloud-based ETL/ELT and data integration service. Build data-driven pipelines visually or in code. 100+ built-in connectors. | Data movement, pipeline orchestration, hybrid data integration |
| **Azure Stream Analytics** | Real-time stream processing engine. SQL-like query language. Process millions of events per second from IoT devices, apps, clickstreams. | Real-time dashboards, anomaly detection, IoT telemetry |
| **Azure Data Explorer** | Fast, fully managed service for real-time analysis of large volumes of streaming data. Uses KQL (Kusto Query Language). | Log/time-series analytics, IoT telemetry, app analytics |
| **Azure Analysis Services** | Enterprise-grade analytics engine as a service. Semantic data models for BI tools (Power BI, Excel). Tabular models. | Corporate BI, semantic modeling |

---

## 12. AI & Machine Learning Services

| Service | Description |
|:--|:--|
| **Azure Machine Learning** | Platform for the full ML lifecycle: data prep, training, evaluation, deployment, MLOps. Supports notebooks, AutoML, designer (drag-and-drop), and code-first SDK. |
| **Azure Cognitive Services** | Pre-built AI APIs — no ML expertise needed. Categories: **Vision** (OCR, face detection, image analysis), **Speech** (STT, TTS, translation), **Language** (NLU, QnA Maker, sentiment), **Decision** (anomaly detection, content moderator, personalizer). |
| **Azure OpenAI Service** | Access GPT-4, GPT-3.5, DALL-E, and Whisper models via Azure. Enterprise-grade security, RBAC, private networking, and compliance. |
| **Azure AI Studio** | Unified platform to build generative AI apps. Prompt orchestration, RAG (retrieval augmented generation), model deployment, and evaluation. |
| **Azure Cognitive Search** | AI-powered cloud search service. Full-text search with built-in AI enrichment: OCR, entity recognition, key phrase extraction, image analysis. Formerly Azure Search. |
| **Azure Bot Service** | Build intelligent chatbots. Integrates with Teams, Slack, web, Facebook. Powered by Bot Framework. Supports language understanding (LUIS / CLU). |
| **Azure AI Document Intelligence** | Extract text, key-value pairs, tables, and structures from documents using ML. Pre-built models for invoices, receipts, IDs, W-2s. Custom model training. Formerly Form Recognizer. |
| **Azure AI Vision** | Analyze images and video: object detection, face recognition, OCR, spatial analysis, image captioning. |
| **Azure AI Speech** | Real-time speech-to-text, text-to-speech, speech translation, speaker recognition. Custom voice models. |
| **Azure AI Language** | Natural language understanding: entity recognition, sentiment analysis, summarization, question answering, conversational language understanding (CLU). |

---

## 13. Key Distinctions

| Comparison | Short Answer |
|:--|:--|
| Cognitive Services vs Machine Learning | Cognitive Services = pre-built APIs, no training. ML = build and train custom models. |
| Synapse vs Databricks | Synapse = unified warehouse + Spark + pipelines. Databricks = Spark-first with collaborative notebooks, strong ML integration. |
| Data Factory vs Stream Analytics | Data Factory = batch ETL/orchestration. Stream Analytics = real-time stream processing. |
| OpenAI Service vs Cognitive Services | OpenAI = GPT/DALL-E generative models. Cognitive Services = task-specific AI (vision, speech, language). |
| HDInsight vs Databricks | HDInsight = managed open-source clusters (bring your own config). Databricks = optimized Spark platform with additional tooling. |
| Cognitive Search vs Data Explorer | Cognitive Search = AI-enriched full-text search for apps. Data Explorer = KQL-based analytics on large streaming datasets. |

---
## 14. Self-Test Questions

1. You need to run the same application on 100 identical VMs that scale automatically. Which service? **Answer:** VM Scale Sets
2. Which compute option gives you the most control over the operating system? **Answer:** Azure Virtual Machines (IaaS)
3. What is the difference between Availability Sets and Availability Zones? **Answer:** Sets = protect within one datacenter (fault/update domains); Zones = protect across separate datacenters
4. A developer wants to run a piece of code every time a file is uploaded to blob storage. Which service? **Answer:** Azure Functions (Blob trigger)
5. You need to orchestrate containers at scale with auto-healing and service discovery. Which service? **Answer:** AKS
