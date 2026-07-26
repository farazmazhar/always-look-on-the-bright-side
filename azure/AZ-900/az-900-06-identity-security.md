---
date: 2026-07-19
tags: [azure, certification, az-900, identity, security]
---

# AZ-900: Identity & Security (35-40% of Exam, Part 5)

---

## 1. Microsoft Entra ID (formerly Azure Active Directory)

**Microsoft Entra ID** is Azure's cloud-based identity and access management service.

| Capability | Description |
|:--|:--|
| **Authentication** | Verify identity for users, apps, and devices. |
| **SSO (Single Sign-On)** | Sign in once, access thousands of cloud apps. |
| **Application management** | Manage access to SaaS apps (Salesforce, Office 365, etc.). |
| **Device management** | Register and manage devices; enforce device compliance policies. |
| **B2B / B2C** | External identities (see below). |
| **Hybrid identity** | Sync on-prem AD with Microsoft Entra ID (Entra Connect). Entra ID extends on-prem directories to cloud. |

### Microsoft Entra ID vs Windows Server Active Directory

| | Microsoft Entra ID | Windows Server AD |
|:--|:--|:--|
| **Identity type** | Cloud-native | On-prem directory |
| **Protocols** | SAML, OAuth, OpenID Connect, WS-Federation | LDAP, Kerberos, NTLM |
| **Structure** | Flat (no OUs, no GPOs natively) | Hierarchical (OUs, forests, domains) |
| **Devices** | Register/join devices to Entra ID | Domain-join to on-prem AD |

### Microsoft Entra Domain Services

**Managed domain services** that provide **LDAP, Kerberos, NTLM, and Group Policy** in the cloud — without you managing domain controllers.

- Use when you need legacy authentication protocols in Azure (e.g., lift-and-shift a legacy app that requires LDAP).
- Entra ID itself does **not** provide LDAP/Kerberos — that is the role of Entra Domain Services.
- Managed by Azure — patching, replication, and backup are automatic.

---

## 2. Authentication & Authorization

| Concept | Meaning |
|:--|:--|
| **Authentication (AuthN)** | Proving who you are. Who are you? |
| **Authorization (AuthZ)** | What you are allowed to do. What can you access? |
| **MFA (Multi-Factor Authentication)** | Two or more verification methods: something you **know** (password), something you **have** (phone, key), something you **are** (biometric). |
| **SSO (Single Sign-On)** | One login for many applications. Reduces password fatigue. |
| **Passwordless** | Remove passwords entirely. Methods: Windows Hello (biometric/PIN), FIDO2 security keys, Microsoft Authenticator app (phone sign-in). More secure than passwords. |

---

## 3. External Identities

Allow people outside your organization to access your apps and resources.

| Feature | Purpose |
|:--|:--|
| **B2B (Business-to-Business)** | Invite guest users from other organizations. They use their own identity provider (e.g., their own Entra ID or Google) to sign in to your apps. |
| **B2C (Business-to-Consumer)** | Customer-facing identity. Users can sign up/sign in with social accounts (Google, Facebook) or email. Fully branded experience. |
| **Entra B2B Direct Connect** | Mutual two-way trust with another Entra ID organization for Teams/shared channels (no guest objects needed). |

**B2B vs B2C:** B2B = collaborate with other orgs. B2C = serve external customers at scale with branded sign-up/sign-in.

---

## 4. Conditional Access

Conditional Access controls access based on **signals** — when these conditions are met, apply these controls.

**Typical "If-Then" Logic:**
- IF user is signing in from an untrusted location
- THEN require MFA (or block access)

| Signal Type | Examples |
|:--|:--|
| User/group | Specific user, group membership, role |
| Location | Named locations (trusted IP ranges), country |
| Device | Device platform, compliance state, hybrid/Azure AD join |
| Application | Which app is being accessed |
| Risk | User risk, sign-in risk (from Entra ID Protection) |

**Controls you can apply:** Require MFA, require device to be marked compliant, require approved client app, block access, grant limited access.

---

## 5. Role-Based Access Control (RBAC)

RBAC controls **who** can do **what** on **which** resources.

**Three elements:**
- **Security Principal:** The "who" — user, group, service principal, managed identity.
- **Role Definition:** The "what" — a collection of permissions (e.g., read, write, delete).
- **Scope:** The "which" — at what level (Management Group > Subscription > Resource Group > Resource).

**Built-in roles (most tested):**
- **Owner:** Full access + can delegate access to others.
- **Contributor:** Can create/manage resources but cannot grant access to others.
- **Reader:** Can view resources but cannot modify.
- **User Access Administrator:** Can manage user access but cannot manage resources.

> **Role assignment is additive:** A user assigned Reader at subscription and Contributor at resource group level has Reader on subscription but Contributor on that resource group. Access is inherited downwards.

---

## 6. Zero Trust Model

**Core principles:**
1. **Verify explicitly:** Always authenticate and authorize based on all available data points.
2. **Use least-privilege access:** Limit user access with Just-In-Time (JIT) and Just-Enough-Access (JEA).
3. **Assume breach:** Minimize blast radius. Segment access. Verify end-to-end encryption.

**Key phrase:** "Never trust, always verify." Nothing is trusted by default — every access request is verified as if it originates from an open network.

---

## 7. Defense-in-Depth Model

Layered approach to security. If one layer fails, the next one still protects.

**Layers (outermost to innermost):**

| Layer | Description | Tools |
|:--|:--|:--|
| **Physical** | Datacenter security | Fences, cameras, biometric locks, security guards |
| **Perimeter** | Network edge protection | DDoS Protection, edge firewalls |
| **Network** | Internal network segmentation | NSGs, VNet segmentation, firewall rules, deny-by-default |
| **Compute** | Securing compute resources | VM patching, endpoint protection, secure access to VMs |
| **Application** | Secure development | Secure SDLC, vulnerability scanning, WAF |
| **Data** | Protect data itself | Encryption at rest/transit, data masking, Key Vault |

---

## 8. Encryption & Key Management

| Concept | Description |
|:--|:--|
| **Encryption at Rest** | Data stored on disk is encrypted. Azure Storage encrypts data by default using Microsoft-managed keys. You can also use customer-managed keys (CMK) via Key Vault. |
| **Encryption in Transit** | Data is encrypted while moving across networks (TLS/SSL). HTTPS for web, SMB 3.0 encryption for Azure Files. |
| **Azure Key Vault** | Securely store and manage secrets, encryption keys, and certificates. Hardware Security Module (HSM) option. Audit all access. |

---

## 9. Microsoft Defender for Cloud

A unified security management and threat protection platform for hybrid cloud workloads.

**Two main capabilities:**
- **CSPM (Cloud Security Posture Management):** Assesses your environment, gives a **Secure Score**, and recommends fixes. Identifies misconfigurations.
- **CWP (Cloud Workload Protection):** Threat protection for resources (VMs, containers, SQL, storage). Alerts on attacks.

**Free tier:** Assessment + recommendations only. **Paid tier:** Full threat protection (Defender for Servers, Defender for SQL, etc.).

---

## 10. Microsoft Sentinel

Cloud-native **SIEM** (Security Information and Event Management) + **SOAR** (Security Orchestration, Automation, and Response).

- Collects data at cloud scale across all users, devices, apps, and infrastructure.
- Uses AI to detect threats.
- Automates response with **playbooks** (Logic Apps-based).

> **Defender for Cloud vs Sentinel:** Defender = protect and assess posture. Sentinel = detect, investigate, and respond to threats (SIEM/SOAR). They integrate with each other.

---

## 11. Microsoft Entra — Extended Details

### Entra Verified ID

A **decentralized identity** system based on open standards (W3C Verifiable Credentials, DID).

- Users control their own identity credentials — not stored in a central directory.
- Issue and verify credentials without a trusted third party.
- Use cases: employee ID verification, student transcripts, loyalty cards, proof of vaccination.
- Part of Microsoft's broader decentralized identity vision (ION network on Bitcoin).

### Entra Permissions Management

A CIEM (Cloud Infrastructure Entitlement Management) tool. Formerly CloudKnox.

- Discover, manage, and monitor permissions across Azure, AWS, and GCP.
- Identifies **unused and excessive permissions** across multi-cloud.
- Reduces the attack surface by enforcing least privilege at cloud scale.
- Provides a permissions creep index and remediation guidance.

### Entra Workload Identities

Identities for **applications and services** (not human users).

| Identity Type | Description |
|:--|:--|
| **Service Principal** | An identity created for an application (app registration) in Entra ID. Used for app-to-app authentication. |
| **Managed Identity** | A special type of service principal that Azure manages automatically. No credentials to store. Two types: |
| | **System-assigned:** Tied to a single Azure resource. Deleted when resource is deleted. |
| | **User-assigned:** Standalone identity. Can be shared across multiple resources. |
| **Workload Identity Federation** | Allows external services (GitHub Actions, Kubernetes) to authenticate to Azure without storing secrets — uses OpenID Connect (OIDC). |

> **Managed Identity key point:** Apps running on an Azure VM or App Service can use managed identity to access Azure resources (Key Vault, Storage, SQL) without any code changes for credential management.

### Entra Identity Governance

Tools to manage the identity lifecycle at scale.

| Feature | Description |
|:--|:--|
| **Access Reviews** | Periodically review who has access to groups, apps, and privileged roles. Automate removal of unnecessary access. |
| **Entitlement Management** | Create access packages that bundle group memberships, app access, and Teams membership. Users can request access via self-service portal with approval workflows. |
| **Lifecycle Workflows** | Automate joiner/mover/leaver processes. Auto-provision access when someone joins, auto-remove when they leave. Triggered by HR events. |
| **Privileged Identity Management (PIM)** | Just-in-time (JIT) privileged access. Users activate elevated roles only when needed, for a limited time. Requires approval and MFA. Full audit trail. |

---
## 12. Self-Test Questions

1. A company needs to lift a legacy app that uses LDAP for authentication. Which service? **Answer:** Microsoft Entra Domain Services
2. What is the difference between authentication and authorization? **Answer:** AuthN = proving who you are; AuthZ = what you can do
3. A company wants to invite contractors from another organization to access their internal portal. Which Entra feature? **Answer:** B2B (External Identities)
4. "Never trust, always verify" describes which security model? **Answer:** Zero Trust
5. A security architect wants to defend against network attacks, application vulnerabilities, and data theft using multiple overlapping protections. Which model? **Answer:** Defense in Depth
