---
layout: page
title: APIGuard Assurance
description: Development of an API-agnostic, contract-driven tool for REST API security assurance, with a particular focus on semantic security violations that traditional functional and syntactic testing does not capture.
img:
importance: 10
category: Academic
permalink: /projects/apiguard-assurance/
cv_id: apiguard-assurance
toc:
  sidebar: left
---

<!-- Scaffolded from the CV's data (single source of truth) - expand with the
     full write-up below the Summary section. -->

## Summary (from CV)

*Master's Thesis Project (A.Y. 2025/2026)*

- Built in **Python 3.12**, with a **dynamic test-discovery mechanism** allowing new security checks to be added without modifying the core engine.
- Implemented *specified oracles* directly in each test's code: every check encodes its own evaluation criterion, derived from the domain knowledge of the control under test.
- Enforced **strict static typing** (mypy) and **runtime validation** (Pydantic), with full documentation coverage across the public API.
- Built **reproducible packages** with **Hatch**, verifying identical SHA-256 hashes across repeated builds.
- Designed an **extensible** connector architecture to integrate external security scanners, decoupling test logic from tool-specific output parsing.
