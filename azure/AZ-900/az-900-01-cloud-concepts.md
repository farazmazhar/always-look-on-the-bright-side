---
date: 2026-07-19
tags: [azure, certification, az-900, cloud-concepts]
---

# AZ-900: Cloud Concepts (25-30% of Exam)

---

## 1. What Is Cloud Computing?

**Definition:** On-demand delivery of IT resources (compute, storage, networking) over the internet with pay-as-you-go pricing. You rent instead of buy.

**Key idea:** Instead of owning physical datacenters and servers, you access them from a cloud provider when you need them. It is a shift from **CapEx to OpEx**.

---

## 2. Shared Responsibility Model

Who is responsible for what changes depending on the service model. This is the one of the most tested concepts on AZ-900.

| Always Customer | Always Cloud Provider | Depends on Model |
|:--|:--|:--|
| Data & information | Physical datacenter (building, power, cooling) | OS (IaaS only) |
| Devices (PCs, phones) | Physical network (cables, switches) | Runtime / middleware (IaaS + PaaS) |
| Accounts & identities | Physical hosts (servers, racks) | Applications |

**Rule of thumb:**
- **IaaS:** Customer manages OS up. Provider manages physical infra and virtualization.
- **PaaS:** Customer manages apps + data only. Provider manages everything else.
- **SaaS:** Customer manages data/usage only. Provider manages the entire stack.

> **Exam tip:** "The customer is always responsible for their data" is a question that appears frequently.

---

## 3. Cloud Deployment Models

| Model | Who Uses the Cloud? | Key Characteristics | Use Cases |
|:--|:--|:--|:--|
| **Public Cloud** | Anyone (shared infra) | Pay-as-you-go, no CapEx, most cost-effective, least control | Startups, SaaS apps, dev/test |
| **Private Cloud** | Single org (dedicated) | Full control, higher cost, on-prem or hosted, compliance | Government, banking, regulated industries |
| **Hybrid Cloud** | Both (public + private) | Flexibility, burst to public, keep sensitive on-prem | Legacy migration, seasonal workloads |

**Additional model — Multi-cloud:** Using services from multiple cloud providers (e.g., Azure + AWS). Not directly tested but useful context.

**Multi-Tenancy:**
- **Multi-tenant:** Multiple customers share the same physical infrastructure. Data is logically isolated. Most Azure PaaS services are multi-tenant (App Service, SQL Database, Storage).
- **Single-tenant:** Dedicated physical resources for one customer. Needed for compliance/regulatory reasons. E.g., Dedicated Host, Isolated VMs, SQL Managed Instance.

---

## 4. CapEx vs OpEx

| | CapEx (Capital Expenditure) | OpEx (Operational Expenditure) |
|:--|:--|:--|
| **When paid** | Upfront, one-time | Ongoing, monthly |
| **What** | Physical servers, datacenters, buildings | Cloud service consumption |
| **Accounting** | Asset that depreciates | Operating expense |
| **Model** | Traditional on-prem | **Azure / Cloud model** |
| **Risk** | Over-provisioning wastes money | Pay only for what you use |

**Consumption-based model:** Pay for what you use, when you use it. No upfront commitment. This is the essence of OpEx in the cloud.

---

## 5. Service Models: IaaS, PaaS, SaaS

| | IaaS | PaaS | SaaS |
|:--|:--|:--|:--|
| **You manage** | OS, runtime, apps, data | Apps, data | Data / usage |
| **Cloud manages** | Physical infra, virtualization | OS, runtime, platform | Everything |
| **Control** | Most | Medium | Least |
| **Flexibility** | Highest | Medium | Lowest |
| **Example** | Azure Virtual Machines | Azure App Service, Azure SQL Database | Microsoft 365, Teams |
| **Use when** | Need full OS control, lift-and-shift | Building apps without managing infra | Ready-to-use software |

**Serverless:** A subset of PaaS. You write code, cloud handles everything else. Pay-per-execution (you don't pay when idle). Examples: Azure Functions, Azure Logic Apps.

| Scenario | Best fit |
|:--|:--|
| Migrate a legacy on-prem app as-is (lift-and-shift) | IaaS (VMs) |
| Build a new web app, don't want to manage servers | PaaS (App Service) |
| Just need email/Office, no IT overhead | SaaS (Microsoft 365) |

---

## 6. Cloud Pricing Models

| Model | Description |
|:--|:--|
| **Pay-as-you-go** | Pay per second/minute of usage. No commitment. Highest per-unit cost but most flexible. |
| **Reserved Instances** | 1 or 3-year commitment. Up to 72% discount vs pay-as-you-go. Best for predictable workloads. |
| **Savings Plans** | Commit to a fixed hourly spend (not specific resources). Up to 65% discount. More flexible than RI. |
| **Spot VMs** | Use unused Azure capacity. Up to 90% discount. Can be evicted any time. Good for interruptible workloads. |

---

## 7. Benefits of Cloud Services

These 7 benefits are tested directly. Know each term and what it means.

| Benefit | Meaning | Azure Example |
|:--|:--|:--|
| **High Availability** | Service stays up with minimal downtime, backed by SLA | Deploy across Availability Zones |
| **Scalability** | Add resources to meet growing demand. **Vertical** = bigger VM. **Horizontal** = more VMs. | VM Scale Sets (horizontal) |
| **Elasticity** | **Auto**-scale in/out based on real-time demand (spikes) | Auto-scale rules tied to CPU/memory |
| **Reliability** | Recover from failures and keep operating (resiliency) | Region pairs, GRS storage |
| **Predictability** | Predict costs (usage billing) and performance (SLA-backed) | Pricing Calculator, consistent SLAs |
| **Security & Governance** | Built-in tools for compliance, auditing, protection | Azure Policy, DDoS Protection, Defender |
| **Manageability** | Manage via Portal, CLI, PowerShell, IaC. Provider handles physical maintenance. | ARM templates, Cloud Shell |

> **Critical distinction:** Scalability is the **ability** to grow. Elasticity is **automatic** scaling based on demand. The exam tests this difference.

**Sustainability (newer addition):** Cloud is more energy-efficient than on-prem. Microsoft targets carbon-negative by 2030. Using cloud reduces your carbon footprint through shared, efficient infrastructure.

---

## 8. Azure Service Lifecycle

| Phase | Meaning |
|:--|:--|
| **Private Preview** | Invite-only. Limited customers test the feature. No SLA. May have bugs. Not for production. Feedback shapes development. |
| **Public Preview** | Open to all customers. No SLA. May have limited regions. Not recommended for production but supported by Azure support. Feature may change. |
| **General Availability (GA)** | Fully released. SLA-backed. Supported for production. Available in all announced regions. Stable API. |

> **Exam tip:** Preview features have no SLA and are not recommended for production workloads. Most exam questions assume GA services unless stated otherwise.

---
## 9. Self-Test Questions

1. A company wants to move its on-prem servers to Azure without changing the OS or apps. Which service model? **Answer:** IaaS
2. Who is responsible for data security in a SaaS application? **Answer:** The customer
3. What is the difference between scalability and elasticity? **Answer:** Scalability = ability to grow; Elasticity = automatic growth with demand
4. A startup has unpredictable workloads. Which pricing model makes the most sense? **Answer:** Pay-as-you-go
5. A company wants a dedicated cloud for regulatory compliance. Which deployment model? **Answer:** Private cloud
