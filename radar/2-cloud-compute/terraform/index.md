---
name: Terraform / OpenTofu
layer: 2-cloud-compute
ring: adopt
tags: [iac, provisioning, multi-cloud]
champions: []
since: 2026-06
ring_history:
  - { ring: adopt, date: 2026-06, reason: "Radar expansion — IaC default across all cloud engagements" }
certifications:
  - { name: "HashiCorp Certified: Terraform Associate", issuer: "HashiCorp", holders: [] }
references:
  - { client: "Mittelständler", title: "Cloud-Infrastrukturmodernisierung mit Terraform & OpenTofu", url: "https://pexon-consulting.de/casestudie/cloud-infrastrukturmodernisierung-abbau-technischer-schulden-durch-terraform-opentofu-automatisierte-cloud-plattformen/", public: true }
  - { client: "Enterprise-Kunde", title: "Aufbau einer Azure-Datenplattform (Terraform, Hub-and-Spoke)", url: "https://pexon-consulting.de/casestudie/aufbau-einer-azure-datenplattform/", public: true }
  - { client: "Mittelständler", title: "IT-Modernisierung mit Azure Virtual Desktop und Terraform", url: "https://pexon-consulting.de/casestudie/it-modernisierung-azure-cloud-migration-effiziente-infrastruktur-mit-azure-virtual-desktop-und-terraform/", public: true }
articles:
  - { title: "OpenTofu vs. Terraform vs. Pulumi: IaC-Vergleich 2026", url: "https://pexon-consulting.de/blog/opentofu-terraform-pulumi-vergleich/", date: 2026-03 }
  - { title: "OpenTofu statt Terraform: Der strategische Weg zu echter Open Source", url: "https://pexon-consulting.de/blog/opentofu-statt-terraform-der-strategische-weg-zu-echter-open-source/", date: 2025-12 }
---

## What is it?

Declarative infrastructure-as-code for all major clouds. OpenTofu is the open-source fork we evaluate where Terraform's BSL license is a concern.

## Why this ring?

Our IaC default — landing zones, AI platform infrastructure and GPU clusters are all provisioned with it.

## When to use it — and when not?

- **Use** for everything infrastructure — no click-ops on client projects.
- **Don't** mix with a second IaC tool in the same estate (→ Pulumi is on Hold).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://developer.hashicorp.com/terraform
- https://opentofu.org/
