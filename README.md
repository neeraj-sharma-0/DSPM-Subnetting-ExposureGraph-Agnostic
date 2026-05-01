# DSPM for Exposure Graphs — Subnetting-Agnostic Lifecycle and Asset Risk Analysis

## Overview

Implements a DSPM-inspired workflow to model **data exposure relationships using graph structures**, built in a Colab-first environment.

This repository focuses on:
- generating synthetic asset data
- constructing an exposure graph
- scoring assets based on connectivity and attributes
- producing structured artifacts
- archiving outputs with a lifecycle receipt

This is an **exposure graph and lifecycle modeling framework**, not a full network subnet/CIDR simulation or enforcement system.

---

## Core Objective

> Model asset-level exposure using graph relationships and apply a DSPM-style lifecycle to generate auditable outputs.

---

## What This Project Does

Using a Colab notebook, the system:

1. **Generates synthetic assets**
   - asset IDs
   - basic attributes (e.g., type, exposure flags)

2. **Builds an exposure graph**
   - nodes represent assets
   - edges represent connectivity / exposure relationships
   - implemented using NetworkX

3. **Computes asset scores**
   - based on graph connectivity and exposure characteristics

4. **Generates artifacts**
   - CSV for asset scores
   - JSON for graph structure

5. **Applies lifecycle stages**
   - CREATE → MAINTAIN → AUDIT → DESTROY (archive)

6. **Archives outputs**
   - stores artifacts in a versioned archive
   - generates an archive receipt

---

## DSPM Lifecycle Mapping

| Phase   | Implementation |
|---------|----------------|
| Create  | Synthetic asset generation |
| Maintain| Graph construction and updates |
| Audit   | Asset scoring and output generation |
| Destroy | Archiving artifacts with receipt |

---

## Graph Model

The system models:

- **Nodes** → assets  
- **Edges** → exposure relationships  

Analysis is limited to:
- connectivity patterns  
- simple exposure scoring  

---

## Generated Artifacts

Per run, the following files are produced:

- `scores_assets.csv` — asset-level scores  
- `exposure_graph.json` — graph structure  

Archived outputs include:

- `archive_receipt.json` — metadata about archived artifacts  

---

## Execution Environment

- Designed for **Google Colab**
- No external dependencies beyond standard Python + NetworkX
- Fully reproducible via notebook execution

---

## Example Run

- assets generated: 50  
- graph edges created: ~120  
- scoring completed: yes  
- artifacts generated:
  - `scores_assets.csv`
  - `exposure_graph.json`
- archive created: yes  

---

## Scope and Limitations

This repository:

- does not implement real subnetting (CIDR / IP routing)  
- does not map assets to actual network segments  
- does not compute true blast radius  
- does not include PII / sensitivity classification  
- does not generate full DSPM evidence manifests  
- does not delete artifacts (archive-only lifecycle)  

Focus is limited to:

- exposure graph modeling  
- asset-level scoring  
- lifecycle-based artifact generation and archiving  

---

## Why This Matters

Graph-based modeling provides a way to understand how assets relate and potentially expose each other, even without full network context.

This project demonstrates:

- how exposure relationships can be represented  
- how DSPM lifecycle concepts can be applied to generated data  
- how to produce reproducible artifacts for analysis  

---

## One-Line Summary

> Colab-based DSPM-style exposure graph framework using synthetic assets, NetworkX modeling, asset scoring, and archive-based lifecycle outputs.
