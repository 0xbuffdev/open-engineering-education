# D8 — Cloud, Container & Kubernetes Security

**Track:** Security · **Prerequisite:** D1, S14 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P11 cloud assessment

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Secure the deployment layer: identities, networks, container images, Kubernetes workloads, and cloud control planes. You will assess a local cluster and a documented cloud configuration, then verify least-privilege, isolation, and supply-chain controls.

## Outcomes

You can:

- map cloud and cluster trust boundaries;
- explain IAM principals, roles, policies, and workload identity;
- assess network exposure, security groups, and Kubernetes network policies;
- harden containers and Pods with non-root, read-only filesystems, dropped capabilities, and seccomp;
- explain RBAC, service accounts, admission control, and secrets;
- assess image and supply-chain integrity;
- use audit logs and posture tools with evidence;
- identify a privilege-escalation path in an authorized cluster;
- write a cloud/Kubernetes assessment with remediation;
- state shared-responsibility limits.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [NSA/CISA Kubernetes Hardening Guide](https://www.cisa.gov/resources-tools/resources/kubernetes-hardening-guidance) | Full | Baseline controls |
| [Kubernetes security docs](https://kubernetes.io/docs/concepts/security/) | Pod security, RBAC, secrets, network policies, admission | Native controls |
| [OWASP Kubernetes Top 10](https://owasp.org/www-project-kubernetes-top-ten/) | Full | Risk taxonomy |
| [NIST SP 800-190](https://csrc.nist.gov/pubs/sp/800/190/final) | Full | Container security |
| [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes) | Selected controls | Configuration baseline |
| *Container Security* (Rice) | Ch. **1–8** | Threat model and controls |
| Cloud provider IAM/network docs | IAM, VPC, workload identity, audit logs | Provider facts |
| [SLSA](https://slsa.dev/) and [Sigstore](https://www.sigstore.dev/) | Overview | Supply chain |

## Modules

### 1. Shared responsibility and identity

- cloud account/organization structure;
- IAM users, roles, policies, trust relationships;
- least privilege and permission boundaries;
- workload identity and instance metadata;
- access keys and secret management;
- cross-account access;
- audit logging.

### 2. Network and isolation

- VPC/subnets/routes;
- security groups and network ACLs;
- public vs private endpoints;
- Kubernetes Services, Ingress, NetworkPolicy;
- DNS and egress;
- metadata endpoint protection;
- multi-tenant isolation.

### 3. Container security

- image provenance and digests;
- minimal base images;
- non-root, read-only rootfs;
- capabilities and seccomp;
- secrets in images/environment;
- runtime isolation (runc, gVisor, Kata);
- image scanning and signing.

### 4. Kubernetes security

- control plane and node hardening;
- RBAC and service accounts;
- Pod Security Standards/admission;
- resource limits and quotas;
- secrets encryption at rest;
- audit logs;
- workload identity;
- supply chain admission;
- etcd and backup security.

### 5. Assessment method

- scope and authorization;
- configuration review;
- posture scanning with validation;
- authorized privilege-escalation testing in a local cluster;
- evidence and severity;
- remediation and retest;
- shared-responsibility boundaries.

## Labs

### Lab 1 — Trust-boundary map

Map a local kind/k3s cluster plus one documented cloud deployment. Identify identities, control-plane and data-plane boundaries, and shared-responsibility gaps.

### Lab 2 — Container hardening

Harden a workload: non-root UID, read-only root filesystem, dropped capabilities, seccomp, resource limits, and digest-pinned image. Demonstrate one blocked action and explain the remaining risk.

### Lab 3 — RBAC and network policy

Create a least-privilege service account and Role. Test allowed/denied verbs. Add a default-deny NetworkPolicy and prove allowed/denied traffic. Record `kubectl auth can-i` and connection evidence.

### Lab 4 — Cluster assessment

Assess the local cluster against a documented subset of the CIS benchmark and OWASP Kubernetes Top 10. Validate at least two findings manually. Do not run destructive privilege escalation outside the local cluster.

### Lab 5 — Supply chain and cloud review

Verify an image digest/signature (or document why unavailable), generate an SBOM, and review one cloud IAM policy for least privilege. Write remediation and a retest plan.

## Exercises

1. Explain the shared-responsibility model for a managed Kubernetes service.
2. Write a least-privilege IAM policy for a read-only bucket prefix.
3. Explain a service-account token risk.
4. Design a default-deny network policy.
5. Explain Pod Security Standards.
6. Identify a privileged-container risk.
7. Explain image digest versus tag.
8. Map one finding to OWASP Kubernetes Top 10.
9. Explain audit-log coverage gaps.
10. State what a local cluster cannot prove about a cloud account.

## Project increment — P11 cloud assessment

Produce:

- trust-boundary and asset map;
- container hardening evidence;
- RBAC/network-policy tests;
- validated cluster findings with severity;
- supply-chain evidence (SBOM/signature or limitation);
- cloud IAM/network review;
- remediation and retest plan.

**Brief:** [P11 — authorized-assessment](../projects/project-ladder.md#p11--authorized-assessment)

## Exit check

- [ ] show a least-privilege identity with allowed/denied proof;
- [ ] demonstrate container hardening controls;
- [ ] prove default-deny network behavior;
- [ ] validate findings rather than repeat scanner output;
- [ ] assess image/supply-chain integrity;
- [ ] write remediation and retest criteria;
- [ ] state shared-responsibility and local-cluster limits.

## Common failure modes

- Treating a cluster as secure because the cloud is managed.
- Using `cluster-admin` for workloads.
- Relying on namespace isolation alone.
- Running privileged containers or mounting the host filesystem.
- Storing secrets in images or plain ConfigMaps.
- Trusting an unsigned image tag.
- Reporting CIS scanner output without validation.
- Testing a cloud account without authorization.

## Evidence to commit

- `labs/security/D8/` with trust map, hardening, RBAC/network tests, findings, supply-chain evidence, report
- P11 cloud assessment
- `notes/security/D8/summary.md`

## Optional depth

- *Kubernetes Security and Observability* (Creane et al.).
- NSA/CISA hardening guidance for Docker and Kubernetes.
- `kube-bench`, `kube-hunter`, `Trivy`, `Falco` docs (local use).
- OPA Gatekeeper/Kyverno policy examples.
- Cloud provider Well-Architected security pillar.
