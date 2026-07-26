---
date: 2026-07-19
tags: [azure, certification, az-900, storage]
---

# AZ-900: Storage Services (35-40% of Exam, Part 4)

---

## 1. Storage Account Overview

A **storage account** is a container that groups Azure Storage services together. All Azure Storage data is stored in a storage account.

- Must have a globally unique name.
- Types: **General-purpose v2 (GPv2)**, Blob Storage, File Storage.
- GPv2 is the standard choice — supports Blobs, Files, Queues, Tables, all access tiers, and all redundancy options.

---

## 2. Azure Storage Services

| Service | Description | Typical Use |
|:--|:--|:--|
| **Blob Storage** | Unstructured object storage. "Everything is a blob." Three blob types: **Block** (text, binary), **Append** (logs), **Page** (random r/w, used for VM disks). | Images, videos, backups, logs, static website hosting |
| **Azure Files** | Fully managed SMB/NFS file shares. Accessible from cloud or on-prem (via SMB protocol). | Lift-and-shift file servers, shared config files |
| **Queue Storage** | Message queue for async communication between app components. Stores millions of messages, each up to 64 KB. | Decoupling microservices, background job processing |
| **Table Storage** | NoSQL key-value store for structured non-relational data. Schema-less. | User data, device info, metadata |

> **Blob vs File vs Queue vs Table:** Unstructured objects vs managed file shares vs message queuing vs NoSQL table. Know which one to pick based on the use case.

### Additional Storage Types (Azure Managed Disks)

| Disk Type | Purpose |
|:--|:--|
| **Managed Disks** | Azure manages the storage account. You choose disk type: Ultra SSD, Premium SSD, Standard SSD, Standard HDD. |
| **Unmanaged Disks** | You manage the storage account and page blobs yourself. Legacy — managed is preferred. |

**Managed Disk Redundancy:**
- Non-shared managed disks default to LRS.
- Shared managed disks support ZRS.

### Storage Account Types (Performance)

| Type | Backed By | For |
|:--|:--|:--|
| **Standard GPv2** | HDD/SSD mix | Most workloads, all tiers |
| **Premium Block Blobs** | SSD | High transaction rates, low latency (IoT, analytics) |
| **Premium Page Blobs** | SSD | I/O-intensive, VM disks |
| **Premium File Shares** | SSD | Enterprise SMB/NFS shares, high IOPS |

> Premium accounts only support LRS or ZRS (no GRS). Higher storage cost, lower transaction cost.

### Azure Data Lake Storage Gen2 (ADLS)

- Built on Blob Storage with a **hierarchical namespace** (folders/directories).
- Same data accessible via Blob API and ADLS Gen2 API (HDFS-compatible).
- POSIX-style ACLs for fine-grained access control.
- Designed for big data analytics: Databricks, Synapse, HDInsight.

### Blob Lifecycle Management

Automated rules to transition or delete blobs based on age.

| Action | Example |
|:--|:--|
| **Move to Cool** | After 30 days of no modification |
| **Move to Cold** | After 90 days in Cool |
| **Move to Archive** | After 180 days in Cold |
| **Delete blob** | After 365 days |
| **Delete versions/snapshots** | After N days |

- Rules evaluated daily. Applied at the storage account level (GPv2 only).
- Reduces costs by automatically moving idle data to cheaper tiers.

---

## 3. Access Tiers (Blob Storage Only)

Tiers are set at the storage account level (default) or per blob. Available for **GPv2** and **Blob Storage** accounts only.

| Tier | Access Pattern | Storage Cost | Access/Retrieval Cost | Min Duration |
|:--|:--|:--|:--|:--|
| **Hot** | Frequent access | Highest | Lowest | None |
| **Cool** | Infrequent (≥30 days) | Lower than hot | Higher than hot | 30 days |
| **Cold** | Rarely accessed (≥90 days) | Lower than cool | Higher than cool | 90 days |
| **Archive** | Almost never (≥180 days) | Lowest | Highest + hours to rehydrate | 180 days |

> **Rehydration** = moving a blob from Archive to Hot/Cool to read it. Takes hours. Cool/Cold access is immediate (online tiers). Archive is offline.

**Use case rule:** Hot = active data. Cool = short-term backup, older data still accessed occasionally. Cold = long-term backup. Archive = compliance/regulatory archives.

---

## 4. Redundancy Options

All storage accounts have data replicated for durability. Replication is configured at the storage account level.

| Option | Data Copies | Protects Against | Notes |
|:--|:--|:--|:--|
| **LRS** (Locally Redundant) | 3 copies in same datacenter | Node/rack failure | Cheapest. Does NOT survive datacenter failure. |
| **ZRS** (Zone-Redundant) | 3 copies across AZs in same region | Datacenter failure | Only available in regions with AZ support. |
| **GRS** (Geo-Redundant) | LRS in primary + LRS in secondary region | Region failure | Secondary is read-only after Microsoft-initiated failover. |
| **GZRS** (Geo-Zone-Redundant) | ZRS in primary + LRS in secondary | Datacenter + region failure | Combines ZRS durability + geo-replication. |
| **RA-GRS** (Read-Access GRS) | Same as GRS but can read from secondary anytime | Region failure | Allows read access to secondary without failover. |

**Failover behavior:**
- LRS/ZRS: No failover (single region).
- GRS/GZRS/RA-GRS: Secondary region is available for read (RA-GRS always, GRS after failover). Microsoft controls failover. You can also initiate a customer-managed failover.

---

## 5. File Movement Tools

| Tool | Description |
|:--|:--|
| **AzCopy** | Command-line utility to copy blobs or files to/from storage accounts. Fast, scriptable, supports parallelism. Works on Windows, Linux, Mac. |
| **Azure Storage Explorer** | Graphical (GUI) tool to manage storage accounts. Browse, upload, download, and manage blobs, files, queues, tables. Cross-platform. |
| **Azure File Sync** | Synchronizes on-premises Windows file server with Azure Files. Enables cloud tiering (frequently accessed files cached locally; infrequent files stored in cloud). Bidirectional sync. |

---

## 6. Data Migration Options

| Tool | Description |
|:--|:--|
| **Azure Migrate** | Central hub for discovery, assessment, and migration of on-premises workloads to Azure. Covers servers, databases, web apps, virtual desktops, and data. Provides migration guidance and cost estimates. |
| **Azure Data Box** | Physical, ruggedized appliance shipped to your datacenter. You load data onto it and ship it back to Microsoft for upload. **Use when network is too slow or unreliable** (typically >40 TB of data). |
| **Data Box Disk** | Smaller SSD-based device (up to 40 TB per disk, 5 disks max = 200 TB). |
| **Data Box Heavy** | Large wheeled appliance (1 PB capacity). |

> **Decision rule:** Small data + fast network = AzCopy / portal upload. Large data + fast network = Azure Migrate. Large data + slow network = Data Box.

---
## 7. Self-Test Questions

1. A company needs a cheap place to store regulatory documents they access once a year. Which access tier? **Answer:** Archive tier
2. An app needs to store user profile photos. Which storage service? **Answer:** Blob Storage
3. A company needs to replace an on-premises file server so that multiple VMs can access shared files via SMB. Which service? **Answer:** Azure Files
4. You need to protect storage against an entire Azure region going offline. Which redundancy option? **Answer:** GRS, GZRS, or RA-GRS
5. A company has 200 TB of data and a slow 10 Mbps internet connection. How should they migrate? **Answer:** Azure Data Box Heavy
