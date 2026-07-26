---
date: 2026-07-19
tags: [azure, certification, az-900, index]
---

# AZ-900 Study Notes — Index

## Exam Facts

| Item | Detail |
|:--|:--|
| Name | Microsoft Azure Fundamentals (AZ-900) |
| Cost | $99 USD |
| Format | 40-60 questions, multiple choice / scenarios |
| Time | 45 minutes |
| Passing | 700 / 1000 |

## Domain Breakdown

| # | Domain | Weight | Document |
|:--|:--|:--|:--|
| 1 | Cloud Concepts | 25-30% | [[az-900-01-cloud-concepts]] |
| 2 | Azure Architecture | — | [[az-900-02-architecture]] |
| 3 | Compute Services | — | [[az-900-03-compute]] |
| 4 | Networking | — | [[az-900-04-networking]] |
| 5 | Storage | — | [[az-900-05-storage]] |
| 6 | Identity & Security | — | [[az-900-06-identity-security]] |
| 7 | Management & Governance | 30-35% | [[az-900-07-management-governance]] |

> Domains 2-6 together make up "Azure Architecture and Services" (35-40% combined).

## Study Order (Recommended)

1. [[az-900-01-cloud-concepts]] — Foundations. Shortest. Start here.
2. [[az-900-02-architecture]] — Regions, hierarchy. Quick read, frequently tested.
3. [[az-900-03-compute]] — VMs, containers, functions, app hosting decisions.
4. [[az-900-04-networking]] — VNets, VPN vs ExpressRoute, load balancing, NSGs.
5. [[az-900-05-storage]] — Blob, Files, redundancy, access tiers, migration.
6. [[az-900-06-identity-security]] — Entra ID, RBAC, Zero Trust, Defender.
7. [[az-900-07-management-governance]] — Policy, cost, monitoring, deployment tools. Most content-dense — save for last.

## High-Yield Distinctions (Print This Page)

These pairs are confused by nearly every candidate. The exam targets them deliberately.

| Pair | Short Answer |
|:--|:--|
| Scalability vs Elasticity | Scalability = can grow. Elasticity = grows **automatically** on demand. |
| VPN Gateway vs ExpressRoute | VPN = encrypted over **public internet**. ER = **private dedicated** fiber. |
| Azure Policy vs RBAC | Policy = what resources are allowed. RBAC = who can do what. |
| Resource Lock vs RBAC | Lock = prevents delete/modify (overrides RBAC). RBAC = controls access. |
| NSG vs Azure Firewall | NSG = per-subnet/per-NIC (L3/L4). Firewall = centralized (L3-L7). |
| Load Balancer vs Application Gateway | LB = TCP/UDP (L4). AG = HTTP/HTTPS + WAF (L7). |
| Pricing Calculator vs TCO Calculator | Pricing = cloud cost estimate. TCO = on-prem vs cloud comparison. |
| Azure Monitor vs Advisor vs Service Health | Monitor = data. Advisor = advice. Service Health = status. |
| Entra ID vs Entra Domain Services | Entra ID = cloud identity. DS = managed LDAP/Kerberos for legacy apps. |
| Defender for Cloud vs Sentinel | Defender = posture + protection. Sentinel = SIEM/SOAR threat detection. |
| Hot vs Cool vs Cold vs Archive | Difference: storage cost + min retention days + retrieval cost/speed. |
| Blob vs Files vs Queue vs Table | Objects vs SMB shares vs messages vs NoSQL. |
| Availability Set vs Availability Zone | Set = within-a-datacenter (fault domains). Zone = across-datacenters. |

## Quick Scenario Map

| If the question mentions... | The answer is likely... |
|:--|:--|
| "Lift and shift" | Azure VMs |
| "Web app, no OS management" | Azure App Service |
| "Event-driven, pay per execution" | Azure Functions |
| "No-code workflow, 200+ connectors" | Azure Logic Apps |
| "Private connection, not internet" | ExpressRoute |
| "Prevent accidental deletion" | Resource Lock (CanNotDelete) |
| "Enforce allowed regions / require tags" | Azure Policy |
| "Filter traffic by IP and port on a subnet" | NSG |
| "Auto-scale identical VMs" | VM Scale Sets |
| "Store secrets, keys, certificates" | Key Vault |
| "Cache content at edge locations" | CDN |
| "Large data, slow network" | Data Box |
| "Orchestrate containers at scale" | AKS |
| "Managed file shares via SMB" | Azure Files |
| "App performance monitoring" | Application Insights |
| "Manage on-prem / multi-cloud from Azure" | Azure Arc |
| "Never trust, always verify" | Zero Trust |
| "Layered security" | Defense in Depth |
| "Managed LDAP/Kerberos in cloud" | Entra Domain Services |
| "Guest users from other orgs" | B2B |
| "Customer sign-up/sign-in" | B2C |
| "Discover and classify sensitive data" | Microsoft Purview |
| "Query all resources across subscriptions" | Azure Resource Graph |
| "Email alert when spending exceeds budget" | Cost Management + Billing |
| "Infrastructure as Code" | ARM Templates / Bicep |
| "Free personalized recommendations" | Azure Advisor |

## Acronym Cheatsheet

| Acronym | Meaning |
|:--|:--|
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
| LRS / ZRS / GRS / RA-GRS / GZRS | Storage redundancy types |
| TCO | Total Cost of Ownership |
| SIEM | Security Information & Event Management |
| SOAR | Security Orchestration, Automation & Response |
| KQL | Kusto Query Language |
| IaC | Infrastructure as Code |
| ARM | Azure Resource Manager |
| APM | Application Performance Monitoring |
| CSPM | Cloud Security Posture Management |
| WAF | Web Application Firewall |
| AZ | Availability Zone |
| HSM | Hardware Security Module |
