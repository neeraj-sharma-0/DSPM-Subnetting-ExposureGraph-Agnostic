# DSPM Subnetting ExposureGraph -- Lifecycle (Colab-First Edition)

## Overview

This project implements a subnet-aware **Data Security Posture
Management (DSPM)** model executed through a Colab-native notebook
workflow.

The repository contains a structured `src/` directory representing the
packaged implementation.\
The current public notebook executes in a Colab-first mode and does not
require local installation of the package.

This keeps the project:

-   Easy to run
-   Reproducible in clean environments
-   Structured for future CLI packaging

------------------------------------------------------------------------

# Repository Structure

    .
    ├── DSPM_Subnetting_ExposureGraph_Lifecycle.ipynb
    ├── requirements.txt
    ├── src/
    │   └── dspm_subnetting_exposuregraph/
    │       └── ...
    ├── out/ (generated artifacts)

The `src/` directory represents the modular implementation of:

-   Exposure graph logic
-   Risk scoring engine
-   CLI entry points (future-ready)
-   Destroy workflow logic

The notebook currently operates without requiring editable installs.

------------------------------------------------------------------------

# Lifecycle Model Implemented

The operational lifecycle executed in the notebook is:

CREATE → MAINTAIN → AUDIT → DESTROY

## CREATE

-   Synthetic asset generation
-   CIDR-based subnet modeling
-   Exposure graph construction
-   Risk scoring artifact generation

## MAINTAIN

-   Deterministic recomputation
-   Idempotent artifact regeneration

## AUDIT

-   SHA256 hashing of generated artifacts
-   Evidence-ready output

## DESTROY

-   Controlled teardown of generated artifacts
-   Destroy receipt generation
-   Lifecycle closure validation

------------------------------------------------------------------------

# Risk & Exposure Modeling

The scoring engine produces:

-   Asset-level risk scores
-   Subnet exposure relationships
-   Structured CSV + JSON artifacts

Exposure graph artifacts are generated in `out/`.

------------------------------------------------------------------------

# Why This Design

This project intentionally separates:

-   Modular implementation (`src/`)
-   Execution harness (notebook)
-   Artifact outputs (`out/`)

This mirrors production security pipelines where:

-   Core logic is modular
-   Execution is environment-specific
-   Artifacts are auditable

------------------------------------------------------------------------

# Technical Stack

-   Python 3.9+
-   pandas
-   networkx
-   Colab-compatible runtime

Install:

pip install -r requirements.txt

------------------------------------------------------------------------

# Intended Audience

-   DSPM Engineers
-   Cloud Security Engineers
-   Zero Trust Architects
-   DevSecOps Platform Engineers

------------------------------------------------------------------------

# Integrity Statement

The notebook runs independently in Colab-first mode. The `src/`
structure is included to demonstrate modular architecture and future CLI
packaging alignment.

No claims extend beyond implemented functionality.

------------------------------------------------------------------------

Author: Neeraj Sharma
