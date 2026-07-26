---
date: 2026-07-19
tags: [azure, certification, az-900, architecture]
---

# AZ-900: Azure Architecture (35-40% of Exam, Part 1)

---

## 1. Azure Physical Infrastructure

### Regions

A **region** is a geographic area containing one or more datacenters networked together with low latency.

- When you deploy a resource, you pick a region (e.g., East US, West Europe).
- Not all services are available in all regions.
- Some services are **non-regional** (e.g., Microsoft Entra ID, Azure DNS) — they're global.

### Availability Zones

**Availability Zones (AZs)** are physically separate datacenters within a region, each with independent power, cooling, and networking.

- A region typically has **3 AZs**.
- Purpose: protect against a **single datacenter failure**.
- Services that support AZs: VMs, managed disks, load balancers, SQL DB.
- **Zonal services:** You pin a resource to a specific AZ (e.g., VM in AZ-1).
- **Zone-redundant services:** Platform replicates automatically across AZs (e.g., ZRS storage).

### Region Pairs

A **region pair** is two regions in the same geography, at least **300 miles apart**, paired for disaster recovery.

- If a region fails, its pair gets priority for recovery.
- Data replicates between region pairs for GRS/RA-GRS storage.
- Examples: East US / West US, North Europe / West Europe.
- Planned Azure updates roll out to one region in a pair at a time.

### Sovereign Regions

Isolated instances of Azure for compliance/legal reasons. Physically and logically isolated from the public Azure cloud.

| Sovereign Region | Purpose |
|:--|:--|
| **US Gov** (Virginia, Texas, Arizona) | US government agencies |
| **China** (21Vianet operated) | Chinese market compliance |

> Not part of region pairs with public regions. Separate compliance frameworks.

### Datacenters

Physical buildings containing servers. Grouped into regions. You never choose a specific datacenter — you choose a region or availability zone.

---

## 2. Azure Management Infrastructure

### Hierarchy (Top to Bottom)

```
Management Group
  └─ Subscription
      └─ Resource Group
          └─ Resource
```

### Management Groups

- Container above subscriptions.
- Apply **Azure Policy** and **RBAC** at scale — inherits downward to all subscriptions.
- Supports up to **6 levels** of nesting.
- Root management group is created automatically for each directory.

### Subscriptions

- **Billing boundary:** All resources in a subscription share one bill.
- **Access boundary:** Separate subscriptions can have separate access policies.
- Every subscription is associated with a **Microsoft Entra ID** tenant.
- Types: Free, Pay-As-You-Go, Enterprise Agreement, Student, CSP.

### Resource Groups

- Logical container that holds related resources for an Azure solution.
- A resource can exist in only **one** resource group.
- Resource groups **cannot be nested**.
- Deleting a resource group deletes all resources within it.
- Resources in the same group can span different regions.
- Tags applied to a resource group do **not** automatically apply to its resources.

### Resources

- Individual manageable items: VMs, storage accounts, VNets, databases, etc.
- Each resource has a unique name in its namespace, a region, and a resource group.

---

## 3. Azure Accounts

To use Azure, you need an **Azure subscription** connected to a **Microsoft Entra ID** tenant.

- **Microsoft Entra ID tenant:** The identity provider. One directory can have multiple subscriptions.
- **Azure account:** Your login identity (user@domain.com) in the Entra ID tenant.
- **Subscription:** The billing container.

---

## 4. Visual Summary

| Concept | What It Is | Protects Against |
|:--|:--|:--|
| Resource Group | Logical grouping | — (organization only) |
| Availability Set | VMs spread across fault/update domains | Hardware failure in datacenter |
| Availability Zone | Physically separate datacenter | Datacenter failure |
| Region Pair | Paired regions 300+ miles apart | Region-wide disaster |
| Sovereign Region | Isolated Azure for gov/compliance | Regulatory non-compliance |

---
## 5. Self-Test Questions

1. A company needs to ensure an application survives a single datacenter going offline. What should they use? **Answer:** Availability Zones
2. You need to apply a security policy to 20 subscriptions at once. What is the most efficient method? **Answer:** Create a Management Group above them, apply policy there
3. A resource group contains a VM in East US and a storage account in West Europe. Is this valid? **Answer:** Yes — resources in the same resource group can be in different regions
4. What is the minimum distance between region pairs? **Answer:** 300 miles
5. A company needs Azure in China for regulatory reasons. What type of region should they use? **Answer:** Sovereign Region
