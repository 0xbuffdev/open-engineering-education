# S14 — Containers, Virtualization & Cloud Operations

**Track:** Systems · **Prerequisite:** S10, S11 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P4 deployment
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Move from a program that runs on your laptop to a service that is packaged, deployed, observed, and recoverable. You will learn what a container actually is, where the isolation boundary ends, how virtual machines differ, and how cloud primitives fail. The goal is operational competence, not certification trivia.

## Outcomes

You can:

- explain kernel namespaces, cgroups v2, capabilities, seccomp, and mount namespaces;
- build a minimal OCI image and explain layers, digests, and registries;
- explain hypervisors, paravirtualization, virtio, and when a VM is the stronger boundary;
- run a local Kubernetes cluster and explain Pods, Deployments, Services, and probes;
- design a deployment with resource requests/limits, health checks, and a rollback path;
- use infrastructure as code and immutable image digests;
- explain IAM, network boundaries, object storage, and managed-database failure modes;
- collect logs, metrics, and traces from a deployed service;
- estimate cost and identify the dominant cost driver;
- state which parts of a cloud deployment you actually verified.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Linux namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html) | Full | The container isolation mechanism |
| [cgroups v2 docs](https://docs.kernel.org/admin-guide/cgroup-v2.html) | Chapters 1–4, memory and CPU controllers | Resource limits and accounting |
| [OCI image spec](https://github.com/opencontainers/image-spec) and [runtime spec](https://github.com/opencontainers/runtime-spec) | Image layout, config, lifecycle | What "container image" means |
| [Docker/containerd documentation](https://docs.docker.com/) or [Podman docs](https://podman.io/docs) | Build, run, volumes, networking | Practical tooling |
| [Kubernetes documentation](https://kubernetes.io/docs/concepts/) | Workloads, Services, config, probes, scheduling | Orchestration model |
| B4 *OSTEP* | Ch. **2, 4–6** (revisit) | Process and limited-direct-execution model |
| [Google SRE Book](https://sre.google/sre-book/table-of-contents/) | Ch. **1–4, 22–23** | SLO and production mindset (shared with S15) |
| Cloud provider docs | IAM, VPC, compute, object storage, managed DB | Provider-specific facts; record the date |

**Edition rule:** cloud consoles and Kubernetes APIs change. Pin the Kubernetes version, provider, region, and documentation date in `notes/systems/S14/resources.md`.

## Modules

### 1. Isolation from first principles

- namespaces: PID, mount, network, UTS, IPC, user, cgroup, time;
- `clone` flags and what each namespace changes;
- cgroups v2: hierarchy, delegation, CPU weight/quota, memory.max, pids.max, OOM;
- capabilities, no-new-privileges, seccomp, LSMs (AppArmor/SELinux);
- rootless containers and user namespaces;
- chroot versus pivot_root;
- the shared kernel: what a container does **not** isolate.

### 2. Images and the container lifecycle

- OCI image: config, layers, digests, manifests, indexes;
- Dockerfile/Containerfile: multi-stage builds, cache, non-root user, minimal base;
- image scanning and reproducible builds;
- registries, tags versus digests, pull policy;
- volumes and bind mounts;
- container networking: bridge, veth, port publishing, DNS;
- runtime: runc/crun, containerd, OCI hooks;
- PID 1, signal forwarding, zombie reaping, graceful shutdown.

### 3. Virtualization

- privileged vs de-privileged instructions;
- Type 1 and Type 2 hypervisors;
- hardware virtualization (VT-x/AMD-V), nested paging;
- virtio devices, paravirtual I/O;
- VM versus container threat model;
- cloud instance lifecycle, live migration, noisy neighbours;
- when to choose a VM, a container, or a managed service.

### 4. Kubernetes and declarative deployment

- control plane and node components;
- Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs;
- Services, EndpointSlices, Ingress/Gateway;
- ConfigMaps and Secrets (and why base64 is not encryption);
- requests, limits, QoS, eviction;
- liveness, readiness, and startup probes;
- rolling updates, surge/unavailable, rollback;
- persistent volumes and storage classes;
- namespaces, RBAC, service accounts, network policies;
- scheduling, affinity, taints/tolerations, topology spread;
- local cluster: kind, k3d, minikube, or k3s.

### 5. Cloud operations and cost

- VPC/subnets/routes/security groups;
- IAM principals, roles, policies, least privilege;
- object storage consistency and lifecycle;
- managed database backups, failover, connection limits;
- DNS, load balancers, TLS termination;
- infrastructure as code (Terraform/OpenTofu or Pulumi);
- secrets management and workload identity;
- observability: logs, metrics, traces, correlation IDs;
- cost: compute, storage, egress, idle capacity, retained logs;
- disaster recovery: RTO, RPO, restore test.

## Labs

### Lab 1 — Build a container by hand

Run a process with `unshare` and explicit namespace flags. Mount a minimal root filesystem, set a hostname, and observe `/proc` differences. Then compare with Docker or Podman. Explain exactly which isolation each layer adds.

### Lab 2 — Container hardening

Take a deliberately sloppy image (`root` user, large base, shell, secrets in layers) and harden it. Use a non-root UID, read-only root filesystem, dropped capabilities, seccomp profile, and explicit resource limits. Prove the changes with `docker inspect`/`podman inspect` and a capability test.

### Lab 3 — Local Kubernetes deployment

Deploy P4 `workbenchd` to kind/k3s with:

- a Deployment and Service;
- readiness/liveness probes;
- CPU/memory requests and limits;
- ConfigMap and a non-secret configuration;
- a rolling update and rollback;
- log and metric collection.

Break readiness deliberately and show that traffic stops.

### Lab 4 — Failure and recovery

Run these scenarios locally:

- kill a pod and observe replacement;
- exceed a memory limit and observe OOM behaviour;
- make a readiness probe fail;
- deploy a bad image tag;
- roll back;
- restore a backed-up volume.

Record the observed recovery time and any data loss.

### Lab 5 — Cost and boundary memo

For one small deployment, estimate monthly cost with a documented pricing date. Identify the top cost driver and one security boundary you did not verify. State what a managed service would and would not remove from your responsibility.

## Exercises

1. Explain the difference between a container and a VM in terms of the kernel boundary.
2. Trace `docker run` from client to `runc`.
3. Explain why `--privileged` is dangerous.
4. Explain cgroup v2 memory.max and OOM behaviour.
5. Explain image layers, digests, and cache invalidation.
6. Explain why a PID-1 process must forward signals and reap children.
7. Design readiness, liveness, and startup probes for a service with a slow model load.
8. Explain requests versus limits and the resulting QoS class.
9. Write a minimal least-privilege IAM policy for an object-prefix reader.
10. Explain one cloud failure mode that a local cluster cannot reproduce.

## Project increment — P4 deployment

Package and deploy `workbenchd`:

- multi-stage image, non-root, digest-pinned base;
- Kubernetes manifests or a Compose deployment with equivalent controls;
- probes, limits, secrets handling, and persistent state;
- structured logs and metrics;
- rolling update and rollback proof;
- backup/restore evidence;
- a deployment runbook with exact commands.

**Brief:** [P4 — workbenchd](../projects/project-ladder.md#p4--workbenchd)

## Exit check

- [ ] explain and demonstrate one namespace and one cgroup limit;
- [ ] show a hardened image and explain each control;
- [ ] deploy P4 locally and demonstrate a rolling update plus rollback;
- [ ] kill a pod/container and show recovery with timings;
- [ ] demonstrate that a readiness failure removes traffic;
- [ ] explain the VM-versus-container security boundary;
- [ ] restore state from backup and state RTO/RPO;
- [ ] name the dominant cost and one unverified cloud assumption.

## Common failure modes

- Treating a container as a security boundary without hardening.
- Running as root and mounting the Docker socket.
- Baking secrets into image layers.
- Setting a memory limit without understanding OOM kills.
- Using `latest` instead of an immutable digest.
- Confusing liveness with readiness.
- Assuming a cloud managed service removes backup responsibility.
- Testing only a successful deploy, never a rollback.

## Evidence to commit

- `labs/systems/S14/` with namespace/cgroup proof, hardened image, manifests, rollout/rollback log, failure matrix, cost memo
- P4 deployment artifacts and runbook
- `notes/systems/S14/summary.md`
- `notes/systems/S14/resources.md` with versions, provider, region, and pricing date

## Optional depth

- *Container Security* (Rice) for threat modelling.
- *Kubernetes Patterns* (Ibryam & Huß) for workload design.
- Cilium/network-policy documentation.
- OpenTelemetry Collector and Prometheus operator.
- Terraform/OpenTofu state, modules, and drift detection.
- Firecracker/gVisor/Kata Containers for stronger isolation models.
