---
date: 2026-07-19
tags: [azure, certification, az-900, cloud, fundamentals]
---

## 1. Cloud Concepts

### 1.1 Cloud Computing

> Cloud computing = on-demand delivery of IT resources over the internet, pay-as-you-go.

**Shared Responsibility Model:**
- **Customer is ALWAYS responsible for:** data, devices, accounts/identities.
- **Cloud provider is ALWAYS responsible for:** physical datacenter, hosts, network fabric.
- The split between depends on IaaS/PaaS/SaaS.
  - **IaaS:** customer manages more (OS, runtime, apps).
  - **PaaS:** customer manages less (just apps/data).
  - **SaaS:** customer manages least (just data/usage).

**Deployment Models:**

| Model | Description | Use Case |
|-------|-------------|----------|
| Public Cloud | Shared infra owned by provider, pay-as-you-go, no CapEx | Most workloads, startups |
| Private Cloud | Dedicated to one org, more control/compliance | Gov, regulated industries |
| Hybrid Cloud | Public + private combined | Burst to cloud, keep sensitive on-prem |

Comparison: **Public = most cost-effective, least control. Private = most control, highest cost. Hybrid = flexibility.**

**Consumption-Based Model:** Pay only for what you use. OpEx, not CapEx.

### 1.2 CapEx vs OpEx

| CapEx | OpEx |
|-------|------|
| Big upfront purchase | Pay-as-you-go |
| Physical assets (servers, datacenters) | Cloud services consumption |
| Depreciates over time | Monthly/usage billing |
| On-prem model | **Azure model** |

### 1.3 Cloud Service Types (IaaS / PaaS / SaaS)

| Model | You Manage | Cloud Manages | Example |
|-------|------------|---------------|---------|
| **IaaS** | OS, runtime, apps, data (most control) | Physical infra, virtualization | Azure VMs |
| **PaaS** | Apps and data only | OS, runtime, platform | Azure App Service, Azure SQL DB |
| **SaaS** | Just your data/usage (least control) | Everything else | Microsoft 365 |

**Serverless:** Subset of PaaS. No server management at all. Code runs on triggers. Pay-per-execution. E.g., Azure Functions, Azure Logic Apps.

### 1.4 Benefits of Cloud Services

| Benefit | What It Means |
|---------|---------------|
| **High Availability** | Keep services running with minimal downtime (SLAs). Achieved via redundancy across AZs/regions. |
| **Scalability** | Add resources to meet demand. **Vertical** = bigger VM. **Horizontal** = more VMs. |
| **Elasticity** | **Auto**-scale out/in based on real-time demand (scale sets, auto-scale rules). |
| **Reliability** | Recover from failures and continue (resiliency via region pairs, redundancy). |
| **Predictability** | Predict costs and performance. Usage-based billing + consistent performance SLAs. |
| **Security & Governance** | Built-in security (DDoS, encryption). Governance tools (Policy, RBAC). Auditing/compliance. |
| **Manageability** | Portal, CLI, PowerShell, IaC templates. Also: cloud provider handles physical maintenance. |

> **Scalability ≠ Elasticity:** Scalability = ability to grow. Elasticity = automatic scaling based on demand.

---

## 2. Core Azure Architectural Components

### 2.1 Physical Infrastructure

| Term | What It Is |
|------|------------|
| **Region** | Geographic area with ≥1 datacenters (e.g., East US). Deploy resources to a region. |
| **Availability Zone** | Physically separate datacenter within a region (own power, cooling, network). Protects against datacenter-level failure. |
| **Region Pair** | Two regions paired for replication/DR, 300+ miles apart. If one fails, other is prioritized for recovery. |
| **Sovereign Region** | Isolated regions for gov/compliance (US Gov, China). Physically and logically isolated. |
| **Datacenter** | Physical building housing servers. Pooled into regions. |

### 2.2 Management Infrastructure

**Hierarchy (top → bottom):**
```
Management Group → Subscription → Resource Group → Resource
```

| Level | Purpose |
|-------|---------|
| **Management Group** | Container above subscriptions. Apply policies/RBAC at scale (inherits downward). Max 6 levels deep. |
| **Subscription** | Billing boundary + access boundary. Resources under one subscription share the same bill. |
| **Resource Group** | Logical container for resources. A resource lives in **exactly one** resource group. Cannot nest. |
| **Resource** | Single manageable item: VM, storage account, VNet, etc. |

---

## 3. Compute Services

### 3.1 Service Choose-Your-Story Table

| Service | Type | Use When… |
|---------|------|-----------|
| **Azure Virtual Machines** | IaaS | Full OS control, lift-and-shift, custom software |
| **VM Scale Sets** | IaaS | Identical VMs that autoscale (horizontal) |
| **Availability Sets** | IaaS | Protect VMs within a datacenter (fault + update domains) |
| **Azure App Service** | PaaS | Web apps, APIs, mobile backends — no OS management |
| **Azure Functions** | PaaS (Serverless) | Event-driven code, pay-per-execution, short-lived tasks |
| **Azure Logic Apps** | PaaS (Serverless) | Workflow automation with 200+ connectors, no code |
| **Azure Container Instances (ACI)** | PaaS | Run a single container quickly, no orchestration needed |
| **Azure Kubernetes Service (AKS)** | PaaS | Orchestrate many containers at scale |
| **Azure Virtual Desktop** | PaaS/IaaS | Deliver full Windows desktops/apps from cloud |
| **Azure Batch** | PaaS | Large-scale parallel batch computing (auto-manages VMs) |

### 3.2 Compute Scenarios (Exam Tips)

| Scenario | Best Fit |
|----------|----------|
| Lift-and-shift on-prem app | Azure VMs |
| Web app, no server management | Azure App Service |
| Image processing triggered by upload | Azure Functions |
| Run Docker containers at scale | AKS |
| Single container, quick test | ACI |
| Scale out/in based on CPU | VM Scale Sets |
| Deliver desktops to remote employees | Azure Virtual Desktop |
| Run HPC/batch processing jobs | Azure Batch |

### 3.3 VM Resources Required

A VM always needs:
- **OS Disk** (persistent storage for the OS)
- **vNIC** (virtual network interface card)
- **VNet + Subnet** (network connectivity)
- (Optional) Data disks, public IP, NSG

---

## 4. Networking

### 4.1 Networking Services

| Service | Layer | Purpose |
|---------|-------|---------|
| **Virtual Network (VNet)** | — | Private network in Azure. Resources communicate securely. |
| **Subnet** | — | Segment within a VNet to isolate/group resources. |
| **VNet Peering** | — | Connect two VNets directly (low latency, no gateway). |
| **VPN Gateway** | — | Encrypted tunnel over public internet (Site-to-Site, Point-to-Site). |
| **ExpressRoute** | — | **Private, dedicated** connection to Azure (NOT public internet). Higher reliability, bandwidth. |
| **Azure DNS** | — | Host and resolve domain names in Azure. |
| **Azure Load Balancer** | L4 (TCP/UDP) | Distribute traffic across VMs within a region. |
| **Application Gateway** | L7 (HTTP/HTTPS) | Web traffic load balancing + WAF (Web Application Firewall). |
| **Azure CDN** | — | Cache content at edge locations closer to users. |
| **Network Security Group (NSG)** | L3/L4 | Filter traffic to/from Azure resources (allow/deny rules). |
| **Azure Firewall** | L3–L7 | Managed, cloud-native firewall-as-a-service. |

### 4.2 Public vs Private Endpoints

| Type | What It Does |
|------|--------------|
| **Public Endpoint** | Accessible from the internet. All traffic over public IP. |
| **Private Endpoint** | A private IP in your VNet connects to a service. Traffic stays on Azure backbone. |
| **Service Endpoint** | Extends VNet private address space to Azure services over Azure backbone. Simpler than private endpoint. |

### 4.3 VPN Gateway vs ExpressRoute

| | VPN Gateway | ExpressRoute |
|--|-------------|--------------|
| Connection | Public internet (encrypted) | Private, dedicated line |
| Speed | Up to ~10 Gbps | Up to 100 Gbps |
| Latency | Variable | Consistent, low |
| Reliability | Depends on internet | High (SLA-backed) |
| Cost | Lower | Higher |

---

## 5. Storage

### 5.1 Storage Services

| Service | Purpose |
|---------|---------|
| **Blob Storage** | Unstructured object data (images, backups, logs, videos). "Everything is a blob." Three types: Block, Append, Page. |
| **Azure Files** | Managed file shares (SMB/NFS). Lift-and-shift on-prem file shares. |
| **Queue Storage** | Message queue for decoupling app components. Store millions of messages. |
| **Table Storage** | NoSQL key-value store for structured, non-relational data. |

### 5.2 Storage Account Types

| Type | For |
|------|-----|
| **General-purpose v2 (GPv2)** | Standard choice. Blobs, Files, Queues, Tables. All tiers. |
| **Blob Storage** | Specialized for block blobs only. |
| **File Storage** | Premium file shares only (SSD-backed). |

### 5.3 Access Tiers

| Tier | Access Frequency | Storage Cost | Access Cost | Min Retention |
|------|-----------------|--------------|-------------|---------------|
| **Hot** | Frequent | Highest | Lowest | — |
| **Cool** | Infrequent (≥30 days) | Lower | Higher | 30 days |
| **Cold** | Rarely (≥90 days) | Even lower | Higher | 90 days |
| **Archive** | Almost never (≥180 days) | Lowest | Highest (+ rehydration delay) | 180 days |

> **Rehydration:** Archive → Hot/Cool to read data takes hours. Cool/Cold is immediate.

### 5.4 Redundancy Options

| Option | Meaning | Durability |
|--------|---------|------------|
| **LRS** | 3 copies in one datacenter | Cheapest, least durable |
| **ZRS** | 3 copies across AZs in one region | Datacenter failure protection |
| **GRS** | LRS in primary + LRS in secondary region | Region failure protection (secondary read-only after failover) |
| **RA-GRS** | GRS + read access to secondary | Same as GRS but you can read from secondary anytime |
| **GZRS** | ZRS in primary + LRS in secondary | Combines ZRS + region-level protection |

> LRS < ZRS < GRS < GZRS in durability.

### 5.5 File Movement & Migration

| Tool | Use |
|------|-----|
| **AzCopy** | CLI tool to copy blobs/files to/from storage accounts. Fast, scriptable. |
| **Azure Storage Explorer** | GUI to manage storage accounts (upload, download, browse). |
| **Azure File Sync** | Sync on-prem file server with Azure Files (cloud tiering). |
| **Azure Migrate** | Discovery, assessment, and migration of on-prem workloads to Azure. |
| **Azure Data Box** | Physical appliance to transfer large data (>40TB) offline when network is too slow. |

---

## 6. Identity & Security

### 6.1 Identity Services

| Service | Purpose |
|---------|---------|
| **Microsoft Entra ID** (formerly Azure AD) | Cloud identity and access management. Users, groups, SSO, MFA, Conditional Access. |
| **Microsoft Entra Domain Services** (formerly Azure AD DS) | Managed domain services (LDAP, Kerberos, NTLM, Group Policy). For lift-and-shift of legacy apps from on-prem AD to cloud. |
| **External Identities** (B2B / B2C) | **B2B:** Invite guest users from other orgs. **B2C:** Customer-facing sign-up/sign-in (branded). |

### 6.2 Authentication & Authorization

| Concept | Meaning |
|---------|---------|
| **Authentication (AuthN)** | Proving who you are (username + password, MFA, biometrics). |
| **Authorization (AuthZ)** | What you're allowed to do after you're authenticated. |
| **RBAC** (Role-Based Access Control) | Grant access by assigning roles. Built-in roles: Owner, Contributor, Reader. Apply at scope (MG → Sub → RG → Resource). |
| **MFA** (Multi-Factor Authentication) | Two or more verification methods: something you know (password) + something you have (phone) + something you are (biometric). |
| **SSO** (Single Sign-On) | Sign in once, access many apps. |
| **Passwordless** | Remove password entirely. Use Windows Hello, FIDO2 keys, Microsoft Authenticator app. |
| **Conditional Access** | Grant/block access based on signals: location, device state, risk level, application. "If X then Y." |
| **Zero Trust** | "Never trust, always verify." Assume breach. Least privilege access. Verify explicitly. |

### 6.3 Defense-in-Depth Model

Layered security from outside → in:

```
Data ──────── innermost layer (encryption, masking)
  ↕
Application ─ (secure dev, vuln scanning)
  ↕
Compute ───── (patch VMs, endpoint protection)
  ↕
Network ───── (NSGs, firewalls, segmentation)
  ↕
Perimeter ─── (DDoS protection, edge filtering)
  ↕
Physical ──── outermost layer (datacenter security, locks, cameras)
```

**Principle:** If one layer fails, the next one still protects. No single point of failure in security.

### 6.4 Security Services

| Service | Purpose |
|---------|---------|
| **Microsoft Defender for Cloud** | CSPM (Cloud Security Posture Management) + CWP (Cloud Workload Protection). Security score, recommendations. |
| **Microsoft Sentinel** | Cloud-native **SIEM + SOAR**. Collect, detect, respond to threats at scale. |
| **Azure Key Vault** | Securely store secrets, keys, certificates. Audit access. Hardware Security Module (HSM) option. |
| **Azure DDoS Protection** | Protect against volumetric, protocol, and application-layer DDoS attacks. |
| **Microsoft Purview** | Data governance, compliance, and risk management. Discover, classify, and protect data across hybrid/multi-cloud. |

---

## 7. Management & Governance

### 7.1 The Big Three (Most-Tested)

| Tool | What It Does | Analogy |
|------|--------------|---------|
| **Azure Policy** | Enforce rules about *what* resources can be created and how they must be configured. | "Only deploy in allowed regions." |
| **RBAC** | Control *who* can do *what* on which resources. | "Alice can read this storage account." |
| **Resource Locks** | Prevent accidental delete or change of resources, regardless of RBAC. | "Nobody can delete this production DB." |

**Resource Lock Types:**
- **CanNotDelete:** Can still read and modify, but can't delete.
- **ReadOnly:** Can only read. Cannot modify or delete.

> **Policy = what is allowed. RBAC = who is allowed. Locks = prevent accidents (overrides RBAC for delete/change).**

### 7.2 Cost Management

| Tool | Purpose |
|------|---------|
| **Pricing Calculator** | Estimate costs **before** deploying. |
| **TCO Calculator** | Compare on-premises costs vs Azure (Total Cost of Ownership). Generates report of savings. |
| **Cost Management + Billing** | Track, analyze, and budget **actual** spend. Set budgets and alerts. |
| **Tags** | Metadata (key-value pairs) on resources. Used for cost reporting, organization, automation. |

**Factors affecting costs:**
- Resource type, region, bandwidth (outbound data), licensing, reserved vs pay-as-you-go.

### 7.3 Governance & Compliance

| Tool | Purpose |
|------|---------|
| **Azure Policy** | Enforce organizational standards (allowed regions, SKU sizes, require tags). |
| **Microsoft Purview** | Data governance, lineage, classification, compliance reporting. |
| **Resource Locks** | Prevent delete/modify. |
| **Azure Blueprints** | Orchestrate deployment of policies, RBAC, and ARM templates together (governance-as-code). |

### 7.4 Deployment & Management Tools

| Tool | Type | Description |
|------|------|-------------|
| **Azure Portal** | GUI | Web-based management interface. |
| **Azure Cloud Shell** | Browser CLI | Bash + PowerShell via browser. No local install needed. |
| **Azure CLI** | CLI | Cross-platform command-line tool (`az` commands). |
| **Azure PowerShell** | CLI | PowerShell cmdlets for Azure (`Az` module). |
| **ARM Templates** | IaC (JSON) | Declarative JSON to deploy resources. Idempotent. |
| **Bicep** | IaC (DSL) | Simpler, cleaner DSL that transpiles to ARM. |
| **Azure Arc** | Hybrid Mgmt | Manage on-prem, multi-cloud, and edge resources from Azure control plane. Extends Azure governance anywhere. |
| **Azure Resource Manager (ARM)** | Deployment Layer | The deployment and management service for Azure. All tools above interact with ARM via REST API. |

### 7.5 Monitoring Tools

| Tool | Purpose |
|------|---------|
| **Azure Monitor** | Central hub for collecting, analyzing, and acting on telemetry across Azure + on-prem. |
| **Log Analytics** | Query log data with KQL (Kusto Query Language). Workspace-based. |
| **Application Insights** | APM (Application Performance Monitoring). Monitor live apps, detect anomalies, diagnose issues. |
| **Azure Monitor Alerts** | Trigger actions (email, webhook, auto-scale) based on metrics or logs. |
| **Azure Advisor** | Personalized recommendations for: **Cost**, **Security**, **Reliability**, **Operational Excellence**, **Performance**. Actionable, free. |
| **Azure Service Health** | Status of Azure services affecting you. Three views: specific resources, specific regions, global incidents. |

### 7.6 Other Key Tools

| Tool | Purpose |
|------|---------|
| **Service Level Agreement (SLA)** | Microsoft's commitment for uptime/connectivity. 99.9% for most services. |
| **Azure Resource Graph** | Query across all subscriptions at scale (like SQL for Azure resources). |
| **Azure Marketplace** | Storefront to find, try, and deploy third-party software and services on Azure. |

---

## 8. Acronym Quick List

| Acronym | Full Form |
|---------|-----------|
| IaaS | Infrastructure as a Service |
| PaaS | Platform as a Service |
| SaaS | Software as a Service |
| CapEx | Capital Expenditure |
| OpEx | Operational Expenditure |
| SLA | Service Level Agreement |
| VNet | Virtual Network |
| NSG | Network Security Group |
| RBAC | Role-Based Access Control |
| MFA | Multi-Factor Authentication |
| SSO | Single Sign-On |
| AKS | Azure Kubernetes Service |
| ACI | Azure Container Instances |
| CDN | Content Delivery Network |
| LRS | Locally Redundant Storage |
| ZRS | Zone-Redundant Storage |
| GRS | Geo-Redundant Storage |
| RA-GRS | Read-Access Geo-Redundant Storage |
| GZRS | Geo-Zone-Redundant Storage |
| TCO | Total Cost of Ownership |
| SIEM | Security Information and Event Management |
| SOAR | Security Orchestration, Automation, and Response |
| KQL | Kusto Query Language |
| IaC | Infrastructure as Code |
| ARM | Azure Resource Manager |
| APM | Application Performance Monitoring |
| CSPM | Cloud Security Posture Management |
| WAF | Web Application Firewall |
| AZ | Availability Zone |
| DR | Disaster Recovery |
| AD | Active Directory |
| MS Entra ID | Microsoft Entra ID (formerly Azure AD) |

---

## 9. Exam Traps & High-Yield Distinctions

1. **Scalability vs Elasticity:** Scalability = can grow. Elasticity = auto-grows with demand.
2. **VPN Gateway vs ExpressRoute:** VPN = public internet. ER = private, dedicated line.
3. **Azure Policy vs RBAC vs Resource Locks:** Policy = what resources allowed. RBAC = who can access. Locks = prevent delete/change.
4. **NSG vs Azure Firewall:** NSG = resource-level filtering (L3/L4). Firewall = managed service, wider scope (L3–L7).
5. **Load Balancer (L4) vs Application Gateway (L7):** LB = TCP/UDP traffic. AG = HTTP/HTTPS + WAF.
6. **Pricing Calculator vs TCO Calculator:** Pricing = estimate new cloud cost. TCO = compare on-prem vs cloud.
7. **Azure Monitor vs Azure Advisor vs Service Health:** Monitor = telemetry. Advisor = recommendations. Service Health = outage status.
8. **Entra ID vs Entra Domain Services:** Entra ID = cloud identity. Domain Services = managed domain (LDAP/Kerberos/NTLM for legacy apps).
9. **Defender for Cloud vs Sentinel:** Defender = posture + protection. Sentinel = SIEM/SOAR (threat hunting).
10. **Hot vs Cool vs Cold vs Archive:** The difference is access frequency + storage cost + min retention.
11. **Blob Storage vs Azure Files vs Queue vs Table:** Unstructured files vs SMB/NFS shares vs message queue vs NoSQL table.
12. **Sovereign Regions:** Only for US Gov and China. Physically and logically isolated from other regions.

---

## 10. Quick Scenario Map

| If the question says… | Think… |
|-----------------------|--------|
| "Lift and shift" legacy app | Azure VMs |
| "Web app, no server management" | Azure App Service |
| "Run code on a schedule / trigger" | Azure Functions |
| "Connecting on-prem to Azure over internet" | VPN Gateway |
| "Dedicated, private connection to Azure" | ExpressRoute |
| "Prevent accidental deletion of resources" | Resource Locks (CanNotDelete) |
| "Enforce allowed regions for resources" | Azure Policy |
| "Only allow access from specific IP range" | NSG |
| "Automatically scale VMs based on CPU" | VM Scale Sets |
| "Store secrets, keys, certificates" | Azure Key Vault |
| "Cache content close to users" | CDN |
| "Large data migration, slow network" | Azure Data Box |
| "Query logs across all subscriptions" | Azure Resource Graph |
| "App performance monitoring" | Application Insights |
| "Estimate costs before deploying" | Pricing Calculator |
| "Compare on-prem costs with cloud" | TCO Calculator |
| "Single pane of glass for on-prem/multi-cloud" | Azure Arc |
| "Never trust, always verify" | Zero Trust |
| "Layered security approach" | Defense in Depth |
| "Managed domain services for legacy apps" | Entra Domain Services |
| "Invite guest users from other orgs" | B2B (External Identities) |
| "Customer-facing sign-up/sign-in" | B2C (External Identities) |
| "Data governance and classification" | Microsoft Purview |
| "Disaster recovery across regions" | GRS / GZRS / Region Pairs |
| "Protect VMs from hardware failure in same datacenter" | Availability Sets |
| "Protect against datacenter failure" | Availability Zones |
| "Run batch jobs at scale" | Azure Batch |
| "No-code workflow automation" | Azure Logic Apps |
