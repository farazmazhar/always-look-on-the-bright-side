---
date: 2026-07-19
tags: [azure, certification, az-900, networking]
---

# AZ-900: Networking Services (35-40% of Exam, Part 3)

---

## 1. Virtual Network (VNet)

A **VNet** is your own isolated network in the Azure cloud. It is the fundamental building block for private networking.

- Resources in a VNet can communicate with each other, the internet, and on-prem networks.
- Each VNet has a private IP address space (e.g., 10.0.0.0/16).
- **Subnets** segment the VNet into smaller networks. Resources are placed in subnets.
- VNets are scoped to a **single region** but can span all availability zones.

---

## 2. VNet Connectivity

| Feature | What It Does | Use Case |
|:--|:--|:--|
| **VNet Peering** | Directly connect two VNets. Traffic uses Azure backbone, low latency. Can be across regions (global peering). | Connect VNets in different regions or subscriptions |
| **VPN Gateway** | Encrypted tunnel over the **public internet**. Site-to-Site (on-prem to Azure) or Point-to-Site (single device to Azure). | Low-cost hybrid connectivity |
| **ExpressRoute** | Private, **dedicated** connection that does NOT use the public internet. Higher reliability, bandwidth (up to 100 Gbps), and predictable latency. | Enterprise-grade hybrid, regulated industries |
| **Azure DNS** | Host domain names and resolve DNS queries within Azure. | Manage DNS records for your resources |

### VPN Gateway vs ExpressRoute (Exam Favorite)

| | VPN Gateway | ExpressRoute |
|:--|:--|:--|
| **Connection type** | Encrypted tunnel over public internet | Private, dedicated fiber |
| **Speed** | Up to ~10 Gbps | Up to 100 Gbps |
| **Latency** | Variable (internet-dependent) | Consistent, low |
| **Reliability** | Depends on ISP / internet conditions | Enterprise-grade SLA |
| **Cost** | Lower | Higher |
| **Setup time** | Minutes to hours | Weeks (requires physical provisioning) |

---

## 3. Load Balancing & Traffic Distribution

| Service | Layer | Purpose | Key Features |
|:--|:--|:--|:--|
| **Azure Load Balancer** | L4 (TCP/UDP) | Distribute traffic across VMs within a region | High availability, health probes, port forwarding |
| **Azure Application Gateway** | L7 (HTTP/HTTPS) | Web traffic load balancing + Web Application Firewall (WAF) | URL-based routing, SSL termination, session affinity |
| **Azure Traffic Manager** | DNS-level | Global DNS-based traffic routing to different endpoints | Geographic, priority, weighted, performance routing |
| **Azure Front Door** | L7 (HTTP/HTTPS) | Global entry point for web apps | SSL offload, URL routing, caching, WAF, DDoS protection |

> **Key distinction:** Load Balancer = regional L4. Application Gateway = regional L7 + WAF. Traffic Manager = DNS-based global. Front Door = L7 global with WAF + CDN capabilities.

---

## 4. Network Security

| Service | Purpose |
|:--|:--|
| **Network Security Group (NSG)** | Filter traffic to/from Azure resources in a VNet. Rules allow or deny based on: source/destination IP, port, protocol. Attached to subnet or vNIC. Stateful. |
| **Azure Firewall** | Fully managed, cloud-native firewall as a service. Works at L3-L7. Centralized policy, built-in high availability, integrates with threat intelligence. |
| **Azure DDoS Protection** | Protect against distributed denial-of-service attacks. Basic tier is free and automatically enabled. Standard tier adds adaptive tuning, cost protection, and metrics. |

### NSG vs Azure Firewall

| | NSG | Azure Firewall |
|:--|:--|:--|
| **Scope** | Single subnet or vNIC | Entire VNet / multiple VNets |
| **Filtering** | IP, port, protocol (L3/L4) | L3-L7, including FQDN-based rules |
| **Management** | Individual rules | Centralized policy |
| **State** | Stateful | Stateful |
| **Cost** | Free | Billed per hour + data processed |

---

## 5. Public vs Private Endpoints

| Endpoint Type | Traffic Path | Use |
|:--|:--|:--|
| **Public Endpoint** | Over the public internet to the service's public IP | Default for most services |
| **Service Endpoint** | Through Azure backbone (VNet → Azure service). Service becomes reachable from VNet private address space. | Restrict service access to specific VNet/subnet |
| **Private Endpoint** | A private IP address in your VNet acts as the entry point to the service. All traffic stays on Azure backbone. Most secure option. | Access PaaS services privately, compliance |

> **Private Endpoint > Service Endpoint > Public Endpoint** in terms of security and isolation. Private Endpoint brings the service *into* your VNet.

---

## 6. Azure CDN

**Content Delivery Network (CDN):** Caches static content at edge locations (Points of Presence — PoPs) close to users worldwide.

- Reduces latency by serving content from the nearest edge node.
- Use for: static websites, images, videos, software downloads.
- Also supports DDoS protection and WAF integration.
- Popular CDN partners: Edgio, Akamai.

---

## 7. VNet IP Address Behavior

A VM's IP addresses behave differently when stopped or deallocated.

| State | Dynamic Public IP | Static Public IP | Dynamic Private IP | Static Private IP |
|:--|:--|:--|:--|:--|
| **Running** | Assigned | Assigned | Assigned | Assigned |
| **Stopped (deallocated)** | **Released** (lost) | **Retained** | May change | **Retained** |
| **Stopped (OS-level)** | Retained | Retained | Retained | Retained |

> **Key point:** Stop a VM from the portal/CLI = deallocate = dynamic public IP is **lost**. Stop from within the OS = billing continues, IPs retained. Use **static** public IP to keep the same address across stop/start.

### Public IP SKUs

| Feature | Basic SKU | Standard SKU |
|:--|:--|:--|
| **Allocation** | Dynamic or Static | Always Static |
| **Inbound security** | Open by default | Closed by default (NSG required) |
| **Availability Zones** | Not supported | Zone-redundant |
| **Load Balancer** | Basic LB only | Standard LB only |

---

## 8. Networking Scenario Map

| Scenario | Solution |
|:--|:--|
| Connect two VNets in the same region with low latency | VNet Peering |
| Connect on-premises office to Azure over the internet | VPN Gateway (Site-to-Site) |
| Connect a single remote developer to Azure | VPN Gateway (Point-to-Site) |
| Enterprise needs a private, high-bandwidth connection to Azure | ExpressRoute |
| Need to filter traffic to a specific VM (allow only port 443) | NSG (attached to subnet or vNIC) |
| Need centralized firewall rules for all traffic in a VNet | Azure Firewall |
| Distribute web traffic across VMs with URL-based routing | Application Gateway |
| Route users to the closest deployment based on geography | Traffic Manager |
| Cache website assets closer to users worldwide | Azure CDN |
| Access a SQL Database privately from within a VNet | Private Endpoint |

---

## 9. Messaging & Event Services

### Azure Service Bus

A fully managed **enterprise message broker** with queues and publish-subscribe topics.

| Feature | Description |
|:--|:--|
| **Queues** | Point-to-point messaging. One sender, one receiver. Messages are pulled and processed once (FIFO with sessions). |
| **Topics & Subscriptions** | Publish-subscribe. One sender, multiple receivers. Each subscription gets a copy. Rules/filters on subscriptions. |
| **Dead-letter queue** | Messages that cannot be delivered or processed are moved here for later inspection. |
| **Transactions** | Supports atomic send/receive across multiple queues/topics. |
| **Sessions** | Guaranteed FIFO ordering for related messages. |

> Use Service Bus when you need: guaranteed delivery, duplicate detection, ordered processing, or complex pub-sub with filtering.

### Azure Event Hubs

A **big data streaming platform** and event ingestion service. Can receive and process millions of events per second.

| Feature | Description |
|:--|:--|
| **Partitions** | Events are distributed across partitions for parallel consumption. Up to 32 partitions per hub. |
| **Consumer groups** | Multiple independent consumers can read the same stream at their own pace. |
| **Capture** | Auto-save streaming data to Blob Storage or ADLS Gen2 for batch processing. |
| **Protocol support** | AMQP, HTTPS, Apache Kafka (Kafka-compatible endpoint). |

> Use Event Hubs when you need: high-throughput event streaming, telemetry ingestion, log streaming, or Kafka workloads.

### Azure Event Grid

A **fully managed event routing service**. Uses the pub-sub model — publishers emit events, subscribers receive them.

| Feature | Description |
|:--|:--|
| **Events** | Lightweight notifications: "blob created", "resource group changed", "VM restarted". |
| **Topics** | System topics (built-in Azure events) or custom topics (your app events). |
| **Subscriptions** | Filter and route events to handlers: Functions, Logic Apps, Webhooks, Service Bus, Event Hubs, Storage Queue. |
| **Serverless** | No infrastructure to manage. Pay per event. |

> Use Event Grid for: reactive event-driven architectures — "when X happens, trigger Y".

### Azure Notification Hubs

A **push notification engine** for mobile apps. Send notifications to iOS, Android, Windows, Kindle.

| Feature | Description |
|:--|:--|
| **Platform support** | APNS (Apple), FCM (Android), WNS (Windows), Baidu, MPNS. |
| **Tags** | Target specific users/devices using tag expressions. |
| **Templates** | Platform-neutral message templates; the hub fills in platform-specific payload. |
| **Scale** | Millions of devices, low latency. |

> Use for: mobile push notifications — breaking news, game invites, promo alerts.

### Messaging Services — Key Distinction

| Service | Purpose | Pattern | Scale |
|:--|:--|:--|:--|
| **Service Bus** | Enterprise messaging | Queues, pub-sub topics | Thousands of messages/sec |
| **Event Hubs** | Event streaming / telemetry ingestion | Partitioned stream, consumer groups | Millions of events/sec |
| **Event Grid** | Event routing / reactive notifications | Pub-sub, push to handlers | Pay per event, serverless |
| **Storage Queue** | Simple message queue | FIFO queue | Millions of messages, 64KB each |
| **Notification Hubs** | Mobile push notifications | Platform-specific push | Millions of devices |

---
## 10. Self-Test Questions

1. What is the difference between a VPN Gateway and ExpressRoute? **Answer:** VPN = encrypted over public internet; ExpressRoute = private dedicated line
2. An organization needs to filter traffic based on source IP and destination port for a specific subnet. Which service? **Answer:** NSG
3. A web app needs SSL termination and URL-based routing. Load Balancer or Application Gateway? **Answer:** Application Gateway (L7, SSL, URL routing)
4. You need to restrict access to Azure Storage so that it can only be accessed from your VNet. Which endpoint type? **Answer:** Private Endpoint or Service Endpoint
5. A company needs to route users in Europe to the Europe deployment and users in Asia to the Asia deployment. Which service? **Answer:** Traffic Manager (geographic routing)
