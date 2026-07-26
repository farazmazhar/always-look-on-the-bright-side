---
date: 2026-07-19
tags: [azure, certification, az-900, management, governance]
---

# AZ-900: Management & Governance (30-35% of Exam)

---

## 1. The Big Three (Most Tested Distinction)

| Tool | What It Controls | Key Phrase |
|:--|:--|:--|
| **Azure Policy** | What resource configurations are allowed | "Only deploy VMs in these regions. Require tags. Restrict SKUs." |
| **RBAC** | Who can do what on which resources | "Alice can read this storage account. Bob can create VMs." |
| **Resource Locks** | Prevent accidental delete or change | "Nobody can delete this production database." |

> **Policy = Governance rules. RBAC = Access control. Locks = Safety net. They are independent and work together.**

### Azure Policy in Detail

- Create **policy definitions** (built-in or custom).
- Assign to a scope (Management Group, Subscription, Resource Group).
- Policies are evaluated on deployment and existing resources.
- **Initiatives** group multiple policies together.
- Example: "Allow only East US and West Europe regions." Any VM deployed elsewhere is denied.

### Resource Lock Types

| Lock | Effect |
|:--|:--|
| **CanNotDelete** | Authorized users can read and modify the resource but cannot delete it. |
| **ReadOnly** | Authorized users can read the resource but cannot modify or delete it. |

- Locks apply regardless of RBAC — even an Owner cannot bypass a lock.
- To remove a resource, you must first **remove the lock** (requires specific permission).

---

## 2. Cost Management

### Factors Affecting Costs

| Factor | Explanation |
|:--|:--|
| **Resource type** | Different services have different meter rates. |
| **Service tier** | Premium costs more than Standard. |
| **Region** | Some regions are more expensive than others. |
| **Bandwidth** | **Ingress** (inbound data) is free. **Egress** (outbound data) costs money. |
| **Licensing** | Bring-your-own-license vs pay-as-you-go license costs. |
| **Reserved capacity** | Committing to 1 or 3 years reduces cost significantly. |
| **Usage** | You pay for what you consume. Idle resources still cost money. |

### Cost Management Tools

| Tool | Purpose | When |
|:--|:--|:--|
| **Pricing Calculator** | Estimate costs **before** deploying | Planning phase |
| **TCO Calculator** | Compare on-premises cost to Azure cost (Total Cost of Ownership) | Migration planning |
| **Cost Management + Billing** | Track **actual** spend, set budgets, configure alerts, analyze cost trends | Ongoing operations |
| **Tags** | Key-value pairs on resources for cost allocation, reporting, and organization | Always |

> **Pricing Calculator vs TCO Calculator:** Pricing = what will this cost in Azure? TCO = how much will I save by moving to Azure? They are different tools with different inputs.

### Cost Optimization Options

| Option | Description |
|:--|:--|
| **Reservations** | Commit 1 or 3 years. Up to 72% discount vs pay-as-you-go. Applies to VMs, SQL DB, Cosmos DB, etc. |
| **Savings Plans** | Commit to a fixed hourly spend (not specific VMs). Up to 65% discount. More flexible than Reservations. Applies across VM families and regions. |
| **Spot VMs** | Use spare Azure capacity at up to 90% discount. Azure can evict at any time. Best for interruptible workloads (batch jobs, dev/test). |
| **Azure Hybrid Benefit** | Use existing on-prem Windows Server / SQL Server licenses in Azure. Saves on licensing cost. |

---

## 3. Governance & Compliance

| Tool | Purpose |
|:--|:--|
| **Azure Policy** | Enforce rules and audit compliance across resources. |
| **Microsoft Purview** | Data governance, catalog, lineage, and compliance. Discover and classify data across hybrid/multi-cloud. Helps with regulatory compliance (GDPR, HIPAA). |
| **Azure Blueprints** | Orchestrate deployment of: Role assignments, Policy assignments, ARM templates, Resource groups. Use for environment setup governance-at-scale. |
| **Service Trust Portal** | Microsoft's public site with audit reports, compliance guides, and security/privacy documents. Used to verify Microsoft's compliance certifications. |

### Microsoft Purview — Key Points

- Data catalog: discovers and classifies data across on-prem, Azure, and other clouds.
- Data lineage: shows where data came from and how it was transformed.
- Compliance: identifies sensitive data (PII, financial, health) and assesses risk.
- Not a security tool per se — it's a **data governance** and compliance tool.

---

## 4. Deployment & Management Tools

### Management Interfaces

| Tool | Type | Notes |
|:--|:--|:--|
| **Azure Portal** | Web GUI | Build, manage, monitor everything. Visual dashboards. |
| **Azure Cloud Shell** | Browser-based CLI | Bash + PowerShell via browser. No local install. Includes pre-installed tools (az CLI, kubectl, terraform, etc.). |
| **Azure CLI** | Command-line (`az` commands) | Cross-platform (Windows, Mac, Linux). Scriptable. |
| **Azure PowerShell** | PowerShell module (`Az` cmdlets) | Windows PowerShell or PowerShell Core. Scriptable. |
| **Azure Mobile App** | Mobile app | Monitor resources, check alerts, take quick actions. |

### Infrastructure as Code (IaC)

| Tool | Description |
|:--|:--|
| **ARM Templates** | Declarative JSON that defines resource configuration. Deploy via ARM. Idempotent — can deploy repeatedly with same result. Supports all Azure resources. |
| **Bicep** | Domain-specific language that transpiles to ARM templates. Cleaner syntax than JSON. Same idempotency guarantee. Microsoft's preferred IaC language for Azure. |
| **Terraform** | Third-party IaC tool (HashiCorp). Multi-cloud. Uses Azure Provider to manage resources. Also declarative and idempotent. |

### Azure Resource Manager (ARM)

ARM is the **deployment and management layer** for Azure. Every tool (Portal, CLI, PowerShell, IaC templates) sends requests to ARM via REST API.

- ARM authenticates the request.
- Validates the request.
- Sends it to the Azure resource provider for execution.

### Azure Arc

Extends Azure management and governance to resources **outside** Azure (on-premises, multi-cloud, edge).

- Manage non-Azure Windows/Linux servers, Kubernetes clusters, SQL Servers as if they are in Azure.
- Apply Azure Policy, RBAC, and tags.
- Use Azure Monitor, Defender for Cloud, Update Manager on non-Azure servers.

> **Key phrase:** "Single pane of glass for hybrid and multi-cloud management."

---

## 5. Monitoring Tools

| Tool | Purpose |
|:--|:--|
| **Azure Monitor** | Central telemetry hub. Collects metrics, logs, and traces from all Azure resources + on-prem. |
| **Log Analytics** | Query and analyze log data using **KQL** (Kusto Query Language). Data stored in a Log Analytics workspace. |
| **Application Insights** | Application Performance Monitoring (APM). Monitor live apps, detect anomalies, diagnose exceptions, trace requests. |
| **Azure Monitor Alerts** | Trigger notifications or automated actions when a metric crosses a threshold or a log event occurs. Actions: email, SMS, webhook, runbook, auto-scale. |
| **Azure Advisor** | Personalized recommendations across 5 pillars: **Cost**, **Security**, **Reliability**, **Operational Excellence**, **Performance**. Fully free. Actionable one-click fixes. |
| **Azure Service Health** | Shows status of Azure services in 3 views: your specific affected resources, specific regions, and global incidents. Notifies about planned maintenance and health advisories. |

### Azure Monitor vs Azure Advisor vs Service Health

| Tool | Answers |
|:--|:--|
| **Monitor** | "What is happening right now?" (Metrics, logs) |
| **Advisor** | "What should I do to improve?" (Recommendations) |
| **Service Health** | "Is Azure having a problem?" (Status, outages) |

---

## 6. Additional Tools

| Tool | Purpose |
|:--|:--|
| **Azure Resource Graph** | Query across all subscriptions at scale. Uses KQL. Explore resources, analyze inventory. Think "SQL for your Azure resources." |
| **Azure Marketplace** | Online store for third-party software and services certified to run on Azure. Deploy with a few clicks. |
| **SLA (Service Level Agreement)** | Microsoft's commitment for service uptime. Typically 99.9% for most services. More nines = more cost. Free tier services have no SLA. |
| **Azure Free Account** | $200 credit for 30 days + 12 months of popular free services + always-free services (App Service, Functions, Entra ID). |

---

## 7. Support Plans

| Plan | Cost (approx.) | Support | SLA | Use |
|:--|:--|:--|:--|:--|
| **Basic** | Free | No technical support | None | All subscriptions |
| **Developer** | $29/mo | Email, business hours, 1 contact | None | Trial, non-production |
| **Standard** | $100/mo | 24/7 phone + email, unlimited | 1hr severity A | Production workloads |
| **Professional Direct** | $1000/mo | Pooled support, arch guidance | 1hr severity A | Business-critical |
| **Unified** | Custom (EA) | Dedicated TAM, proactive | Fastest | Enterprise |

---

## 8. SLA — Downtime Mapping

| SLA % | Downtime / Week | Downtime / Month | Downtime / Year |
|:--|:--|:--|:--|
| 99.0% | 1.68 hours | 7.31 hours | 3.65 days |
| 99.5% | 50.4 minutes | 3.65 hours | 1.83 days |
| 99.9% | 10.1 minutes | 43.8 minutes | 8.77 hours |
| 99.95% | 5.04 minutes | 21.9 minutes | 4.38 hours |
| 99.99% | 1.01 minutes | 4.38 minutes | 52.6 minutes |
| 99.999% | 6.05 seconds | 26.3 seconds | 5.26 minutes |

**Composite SLA:** Multiply SLAs of chained services. E.g., Web App (99.95%) x Traffic Manager (99.99%) = ~99.94%.
**Service Credits:** If Azure fails to meet SLA, you may receive credits toward your bill.

---

## 9. Tags — Detailed Limitations

| Limit | Value |
|:--|:--|
| Max tags per resource | 50 |
| Tag name max length | 512 characters |
| Tag value max length | 256 characters |
| Resource group tags | Do **not** automatically apply to child resources |
| Tag inheritance | Use Azure Policy to auto-apply tags from RG to resources |
| Reserved prefixes | `microsoft.`, `azure.`, `windows.` cannot be used |
| Case sensitivity | Tag names case-insensitive. Values case-sensitive. |
| Cost reporting delay | Tags appear in cost analysis after usage reported (up to 24hrs) |

---

## 10. Management Scenario Map

| Scenario | Solution |
|:--|:--|
| Enforce that all VMs are tagged with "Department" | Azure Policy |
| Prevent an intern from deleting the production database | RBAC (give Reader, not Contributor) or Resource Lock (CanNotDelete) |
| Estimate how much a new project will cost in Azure | Pricing Calculator |
| Find out how much you'd save by moving to Azure | TCO Calculator |
| Track monthly spend and set budget alerts | Cost Management + Billing |
| Deploy the same infrastructure consistently across dev, test, prod | ARM Templates or Bicep |
| Manage servers in AWS and Azure from one place | Azure Arc |
| Diagnose a slow web application | Application Insights |
| Check if East US region is experiencing an outage | Service Health |
| Find all untagged resources across 50 subscriptions | Azure Resource Graph |
| Discover and classify all PII data in your organization | Microsoft Purview |
| Get free personalized recommendations to reduce costs | Azure Advisor |
| Audit Microsoft's ISO 27001 certification | Service Trust Portal |
| Run a bash script to create 10 VMs without installing anything locally | Azure Cloud Shell |
| Deploy a pre-configured VM with third-party firewall software | Azure Marketplace |

---

## 11. Cloud Adoption Framework (CAF)

Microsoft's structured methodology for cloud adoption. Six phases:

| Phase | Description |
|:--|:--|
| **Strategy** | Define business justification and expected outcomes. Why move? |
| **Plan** | Create a cloud adoption plan. Assess digital estate. Identify workloads. |
| **Ready** | Prepare the landing zone — set up subscriptions, networking, identity, governance. |
| **Organize** | Align teams and skills. Define roles (Cloud Ops, Cloud Governance, Cloud Strategy). |
| **Adopt** | Migrate or innovate. Execute the plan. |
| **Manage** | Ongoing operations, cost management, security, and governance. |

**Related: Azure Well-Architected Framework** (five pillars):
1. **Cost Optimization**
2. **Operational Excellence**
3. **Performance Efficiency**
4. **Reliability**
5. **Security**

> **CAF vs Well-Architected Framework:** CAF = how-to guide for adoption journey (process-focused). WAF = design principles for building good cloud solutions (architecture-focused).

---

## 12. Azure DevOps

A cloud-based suite of collaboration tools for the full software development lifecycle.

| Service | Description |
|:--|:--|
| **Azure Boards** | Agile project management. Kanban boards, backlogs, sprint planning, work item tracking, dashboards. |
| **Azure Repos** | Git repositories for source control. Pull requests, branch policies, code search, code reviews. |
| **Azure Pipelines** | CI/CD platform. Build, test, and deploy to any cloud or on-premises. YAML or classic visual designer. Integrates with GitHub, Bitbucket, etc. |
| **Azure Test Plans** | Manual and exploratory testing. Test case management, browser-based testing. |
| **Azure Artifacts** | Package management. Host and share NuGet, npm, Maven, Python, and Universal packages. |

> Azure DevOps is a **SaaS** platform — it runs independently from your Azure cloud resources. It's the successor to Team Foundation Server (TFS).

---

## 13. GitHub & GitHub Actions

### GitHub

- Cloud-hosted Git platform. Code hosting, collaboration, pull requests, issues, discussions.
- Microsoft-owned but platform-agnostic — works with any cloud.
- GitHub Codespaces: cloud-hosted dev environments.
- GitHub Copilot: AI code completion.

### GitHub Actions

- CI/CD workflow automation built into GitHub.
- Triggered by events: push, pull request, schedule, issue comment.
- **Workflows** defined in YAML (`.github/workflows/`).
- **Actions** = reusable building blocks. Marketplace has thousands.
- Deploy to Azure: use `azure/login`, `azure/webapps-deploy`, `azure/cli` actions.

> **Azure DevOps vs GitHub:** Azure DevOps = full ALM suite (Boards, Repos, Pipelines, Test Plans, Artifacts). GitHub = code-first with Actions for CI/CD. Both deploy to Azure. Many orgs use both.

---

## 14. Azure DevTest Labs

Create self-service, pre-configured lab environments for development and testing.

| Capability | Description |
|:--|:--|
| **Quick environment setup** | Pre-configured VM templates (OS, tools, config). Users spin up labs without IT involvement. |
| **Cost control** | Set auto-shutdown schedules (e.g., VMs turn off at 7 PM). Set limits on number of VMs and allowed VM sizes per user. |
| **Quotas & policies** | Per-lab limits: max VMs per user, allowed VM series, allowed public IPs. |
| **Custom images** | Create and share golden images with pre-installed tools across the team. |
| **Formulas** | Reusable configurations that define a VM setup (image, size, VNet, artifacts). |

> **Use case:** Replace the "works on my machine" problem. Devs and testers get identical, disposable environments. No cost surprises due to auto-shutdown and quotas.

---

## 15. Azure Automation

Automate frequent, time-consuming, and error-prone cloud management tasks.

| Capability | Description |
|:--|:--|
| **Runbooks** | PowerShell or Python scripts executed in Azure. Triggered by schedule, webhook, or alert. Process automation at scale. |
| **Desired State Configuration (DSC)** | Declarative configuration management. Define how a server should be configured; Azure enforces it. |
| **Update Management** | Centrally manage OS updates and patches for Windows/Linux VMs across Azure, on-prem, and other clouds (via Azure Arc). |
| **Change Tracking & Inventory** | Track software changes, file changes, registry changes, and installed software across VMs. |
| **Shared resources** | Credentials, variables, connections, certificates stored securely and shared across all runbooks. |

> **DevTest Labs vs Automation:** DevTest Labs = environment provisioning for dev/test. Automation = operational task automation (patching, config management, scheduled scripts).

---

## 16. CI/CD Concepts (High-Level for AZ-900)

| Term | Meaning |
|:--|:--|
| **Continuous Integration (CI)** | Developers merge code frequently. Each merge triggers an automated build and test. |
| **Continuous Delivery (CD)** | Every build that passes tests is automatically deployable. Deployment may be manual approval. |
| **Continuous Deployment** | Every passing build is automatically deployed to production (no manual approval). |
| **Build Pipeline** | Compiles code, runs unit tests, produces artifacts. |
| **Release Pipeline** | Takes build artifacts, deploys to environments (dev, test, prod) with approval gates. |

> AZ-900 tests CI/CD awareness at a conceptual level only. No tool-specific deep dives.

---

## 17. Deployment to Azure — Key Paths

| Method | Tool |
|:--|:--|
| Git-based deploy | Push to Azure App Service from GitHub, Azure Repos, Bitbucket, local Git |
| CI/CD pipeline | Azure Pipelines, GitHub Actions, Jenkins |
| Package deploy | ZIP, WAR, container image |
| IaC deploy | ARM templates, Bicep, Terraform — deployed via pipeline |
| Manual | FTP, Azure CLI, Cloud Shell |

---

## 18. Factors That Affect Azure Costs

### Compute Costs

| Factor | How It Affects Cost |
|:--|:--|
| **VM size / SKU** | Larger VMs (more vCPUs, RAM) cost more per hour. GPU and HPC VMs are the most expensive. |
| **Operating system** | Windows VMs cost more than Linux due to licensing. |
| **Running time** | You pay per second (Linux) or per minute (Windows) of uptime. Stopped (deallocated) VMs stop billing for compute. |
| **Region** | Same VM size can cost differently in different regions. |
| **Reserved vs pay-as-you-go** | Reserved (1 or 3 years) gives up to 72% discount. Pay-as-you-go has no commitment but highest per-unit cost. |
| **Azure Hybrid Benefit** | Use on-prem Windows Server / SQL Server licenses to reduce VM cost. |
| **B-series (burstable)** | Cheaper than fixed-size VMs when workload is idle most of the time. Credits accumulate during idle, consumed during bursts. |

### Storage Costs

| Factor | How It Affects Cost |
|:--|:--|
| **Amount stored (GB/TB)** | Pay per GB per month. |
| **Access tier** | Hot = highest storage cost, lowest access cost. Cool/Cold/Archive = progressively cheaper storage, more expensive to read. |
| **Redundancy** | LRS = cheapest. ZRS = more. GRS/RA-GRS/GZRS = most expensive (geo-replication). |
| **Transactions** | Read/write/list operations are billed per 10,000 transactions. Hot has lowest transaction cost. |
| **Data retrieval** | Archive tier charges for rehydration (hours to complete). |
| **Premium vs Standard** | Premium (SSD-backed) costs more per GB but has lower transaction costs. |

### Networking Costs

| Factor | How It Affects Cost |
|:--|:--|
| **Outbound data (egress)** | Data leaving Azure to the internet is charged. Inbound data (ingress) is **free**. |
| **Between regions** | Data transfer between Azure regions (inter-region egress) is charged. |
| **Between AZs** | Data transfer between availability zones in the same region may be charged. |
| **Within same AZ** | Usually free. |
| **Public IP addresses** | Standard SKU public IPs have an hourly charge even when not associated with a running VM. |
| **VPN Gateway** | Charged per hour + per GB of data processed. ExpressRoute costs more but is flat-rate for bandwidth. |
| **Load Balancer / Application Gateway** | Billed per hour + per GB processed. |

### Other Cost Factors

| Factor | How It Affects Cost |
|:--|:--|
| **Service tier** | Premium/Standard/Basic tiers of services (App Service, SQL DB, etc.) have different pricing. |
| **Support plan** | Basic = free. Standard = ~$100/mo. Professional Direct = ~$1000/mo. |
| **Licensing** | BYOL (Hybrid Benefit) vs pay-as-you-go licensing included in service cost. |
| **Idle resources** | Unattached public IPs, unused disks, stopped-but-not-deallocated VMs, idle load balancers all still cost money. |
| **Resource count** | Some services charge per resource (e.g., per public IP, per load balancer). |

---

## 19. Cost Reduction Strategies

### Reserved Capacity & Commitments

| Strategy | Discount | Applies To | Flexibility |
|:--|:--|:--|:--|
| **Reserved Instances** | Up to 72% | Specific VM type + region for 1 or 3 years | Low — locked to specific SKU and region |
| **Savings Plans** | Up to 65% | Hourly compute spend commitment (any VM family, any region) | High — can change VM family and region |
| **Azure Hybrid Benefit** | Varies | Windows Server + SQL Server licenses | Use existing licenses in Azure |
| **Spot VMs** | Up to 90% | Spare Azure capacity | None — can be evicted any time |

> **Reservations vs Savings Plans:** Reservations = commit to specific VMs, bigger discount. Savings Plans = commit to hourly spend amount, more flexible.

### Right-Sizing & Waste Elimination

| Strategy | How |
|:--|:--|
| **Right-size VMs** | Use Azure Advisor cost recommendations. Downgrade over-provisioned VMs. |
| **Auto-shutdown** | Use auto-shutdown schedules for dev/test VMs. Or Azure DevTest Labs with mandatory schedules. |
| **Delete unused resources** | Unattached disks, unused public IPs, idle load balancers, old snapshots, old backups. |
| **Stop deallocated VMs** | Stopping from portal/CLI deallocates the VM — compute billing stops. Stopping from OS keeps billing. |
| **Use B-series VMs** | Burstable VMs for workloads that idle most of the time. |

### Storage Optimization

| Strategy | How |
|:--|:--|
| **Choose right access tier** | Hot for active data, Cool for 30+ days, Cold for 90+ days, Archive for 180+ days. |
| **Use lifecycle management** | Automatically move blobs to cheaper tiers or delete after N days. |
| **Choose right redundancy** | LRS is cheapest. Only use GRS/GZRS for production critical data. |
| **Delete old snapshots and backups** | Unused snapshots accumulate and cost money. |
| **Use Premium only when needed** | Premium storage costs more per GB. Standard is sufficient for most use cases. |

### Monitoring & Governance

| Strategy | How |
|:--|:--|
| **Set budgets** | Configure monthly/quarterly budgets in Cost Management. Get email alerts at thresholds. |
| **Use cost alerts** | Alert when cost exceeds budget or when anomaly is detected. |
| **Use Tags** | Tag resources by department, project, environment. View cost breakdown by tag in Cost Analysis. |
| **Apply Azure Policy** | Deny expensive VM SKUs. Enforce tags. Require specific regions. |
| **Azure Advisor** | Free personalized cost recommendations. One-click apply for many. |
| **TCO Calculator** | Before migrating: estimate savings vs on-prem. Generates a report. |

---

## 20. Pricing Calculator vs TCO Calculator

| | Pricing Calculator | TCO Calculator |
|:--|:--|:--|
| **Purpose** | Estimate cost of Azure services before deploying | Compare on-prem costs to projected Azure costs |
| **Input** | Azure services, regions, usage estimates | On-prem server count, storage, networking, power, labor |
| **Output** | Monthly cost estimate for Azure | Cost savings report (on-prem vs Azure) |
| **When** | Planning a new deployment | Planning a migration to Azure |
| **URL** | `https://azure.microsoft.com/pricing/calculator/` | `https://azure.microsoft.com/pricing/tco/calculator/` |

---

## 21. Cost Management + Billing Features

| Feature | Description |
|:--|:--|
| **Cost Analysis** | Explore and analyze actual costs. Filter by scope, time range, tag, resource type. |
| **Budgets** | Set spending thresholds. Get alerts via email when budget is reached. |
| **Alerts** | Budget alerts: notify at % of budget. Cost anomaly alerts: detect unusual spikes. |
| **Cost Recommendations** | Advisor cost recommendations integrated into Cost Management. |
| **Cost Exports** | Schedule exports of cost data to storage account (CSV). Integrate with Power BI. |
| **Invoices** | View and download PDF invoices for each billing period. |
| **Billing scopes** | View cost by management group, subscription, resource group. |

---

1. A company wants to save money on VMs they plan to run continuously for 3 years. Which pricing option?
2. A developer leaves a test VM running over the weekend from inside the OS. Is it still billing for compute?
3. Data transferred into Azure from the internet — does it cost money?
4. A company has on-prem Windows Server licenses with Software Assurance. How can they reduce Azure VM costs?
5. You need to automatically move blobs from Hot to Archive after 180 days. What feature?
6. A team wants to know how much they'll save by moving their on-prem datacenter to Azure. Which tool?
7. Which redundancy option has the lowest cost?
8. A startup has an unpredictable batch processing workload that can be interrupted. Which VM pricing option?

**Answers:**
1. Reserved Instances (3-year)
2. Yes — stopping from OS does not deallocate the VM, compute billing continues
3. No — ingress (inbound) data is free
4. Azure Hybrid Benefit
5. Blob lifecycle management
6. TCO Calculator
7. LRS (Locally Redundant Storage)
8. Spot VMs

## 22. Azure Monitor Action Groups

Action Groups are **collections of notification and action preferences** used by Azure Monitor alerts.

When an alert fires, the action group defines what happens:

| Action Type | Description |
|:--|:--|
| **Email / SMS / Push / Voice** | Notify people via email, SMS, Azure mobile app push, or voice call. |
| **Webhook** | Call a URL (e.g., trigger a Logic App, Slack, PagerDuty, ITSM). |
| **Azure Function** | Execute a function as a response to the alert. |
| **Logic App** | Trigger a Logic App workflow. |
| **Automation Runbook** | Execute an Azure Automation runbook. |
| **ITSM** | Create a ticket in ServiceNow, BMC, etc. via ITSM connector. |

- Action Groups are **reusable** — create once, use across multiple alert rules.
- Can be shared across subscriptions within the same region.

---

## 23. Compliance & Legal Documents

| Document | What It Is |
|:--|:--|
| **Microsoft Privacy Statement** | Explains what personal data Microsoft collects, how it's used, and for what purposes. Applies to all Microsoft consumer and enterprise services. |
| **Online Services Terms (OST)** | Legal agreement between Microsoft and volume licensing customers. Governs use of Azure, M365, Dynamics 365, and other online services. Includes service-specific terms. |
| **Data Protection Addendum (DPA)** | Defines Microsoft's data processing obligations under GDPR and other privacy laws. Covers data location, security, breach notification, sub-processors. Part of OST. |
| **Microsoft Trust Center** | Public website: `https://www.microsoft.com/trust-center`. Central hub for security, privacy, compliance documentation. Find audit reports, compliance guides, whitepapers. |
| **Service Trust Portal** | `https://servicetrust.microsoft.com/`. Access to audit reports (SOC, ISO, FedRAMP), compliance guides, and third-party assessment reports. Requires Microsoft account login. |

> **Trust Center vs Service Trust Portal:** Trust Center = marketing/overview of compliance. Service Trust Portal = actual audit reports and documents.

---

## 24. Log Analytics Workspace

A **Log Analytics Workspace** is the storage and query environment for log data in Azure Monitor.

| Concept | Description |
|:--|:--|
| **Workspace** | A logical container that stores log data from multiple sources. All logs in one workspace share the same retention and access settings. |
| **Data sources** | Azure resources (VMs, containers, App Service), on-prem servers (via Azure Arc or Log Analytics agent), custom application logs, Azure Activity log, Entra ID sign-in logs. |
| **KQL (Kusto Query Language)** | The query language used in Log Analytics. Read-only. Designed for fast analysis of large datasets. |
| **Retention** | Default: 30 days free. Up to 730 days with additional cost. Archive tier up to 7 years. |
| **RBAC** | Control access to workspace data via Azure RBAC. Separately from the resources that generate the data. |
| **Multiple workspaces** | Common pattern: separate workspaces for dev/test/prod, or one centralized workspace for cross-service queries. |

> **Key point:** A Log Analytics Workspace is required before you can query logs in Azure Monitor. Resources send their diagnostic data to a workspace, and you query it with KQL.

---

1. An administrator wants to prevent all users from deleting a critical VM, including users with Owner role. What should they use?
2. What is the difference between the Pricing Calculator and the TCO Calculator?
3. A company needs to apply a policy that requires all storage accounts to use HTTPS. What tool?
4. You want to query "show me all VMs across all subscriptions that are running Windows." Which tool?
5. A global company needs to manage Kubernetes clusters in Azure, AWS, and their on-prem data center from a single control plane. Which service?

**Answers:** 1. Resource Lock (CanNotDelete) 2. Pricing = estimate cloud costs. TCO = compare on-prem vs cloud savings. 3. Azure Policy 4. Azure Resource Graph 5. Azure Arc
## 25. Self-Test Questions

1. An admin wants to prevent all users from deleting a critical VM, including users with Owner role. What should they use? **Answer:** Resource Lock (CanNotDelete)
2. What is the difference between the Pricing Calculator and the TCO Calculator? **Answer:** Pricing = estimate cloud costs; TCO = compare on-prem vs cloud savings
3. A company needs to apply a policy that requires all storage accounts to use HTTPS. What tool? **Answer:** Azure Policy
4. You want to query "show me all VMs across all subscriptions that are running Windows." Which tool? **Answer:** Azure Resource Graph
5. A global company needs to manage Kubernetes clusters in Azure, AWS, and on-prem from a single control plane. Which service? **Answer:** Azure Arc
6. A dev team needs CI/CD pipelines to build and deploy code to Azure. Which Azure DevOps service? **Answer:** Azure Pipelines
7. A team wants self-service lab environments for testing with auto-shutdown to control costs. Which service? **Answer:** Azure DevTest Labs
8. An admin needs to run a PowerShell script every night to stop idle VMs across subscriptions. Which service? **Answer:** Azure Automation (Runbooks)
9. A developer wants to host a private npm package within their DevOps toolchain. Which service? **Answer:** Azure Artifacts
10. An org wants to centrally manage OS updates for VMs across Azure and on-prem. Which capability? **Answer:** Update Management
11. A team uses GitHub and wants to deploy to Azure on every push to main. Which tool? **Answer:** GitHub Actions
12. A lab manager needs to limit devs to 3 VMs each. Which feature? **Answer:** DevTest Labs (quotas/policies)
13. A company wants to save money on VMs they plan to run continuously for 3 years. Which pricing option? **Answer:** Reserved Instances (3-year)
14. A developer leaves a test VM running over the weekend after stopping it from inside the OS. Is compute still billing? **Answer:** Yes — stopping from OS does not deallocate the VM
15. Data transferred into Azure from the internet — does it cost money? **Answer:** No — ingress is free
16. A company has on-prem Windows Server licenses with Software Assurance. How can they reduce Azure VM costs? **Answer:** Azure Hybrid Benefit
17. Which redundancy option has the lowest storage cost? **Answer:** LRS (Locally Redundant Storage)
18. A startup has an unpredictable batch workload that can be interrupted. Which VM pricing option? **Answer:** Spot VMs
