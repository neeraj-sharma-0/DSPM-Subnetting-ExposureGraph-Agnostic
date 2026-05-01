# DSPM for Data Exposure Topology — Subnetting and Blast Radius Analysis

## Overview

Implements a DSPM-driven approach to modeling **data exposure topology** using subnetting concepts.

Network segmentation is typically designed for infrastructure isolation, but **data exposure across segments is rarely quantified**. This repository models how sensitive data is distributed across subnets and how it can propagate through connectivity paths.

The focus is on identifying **where sensitive data resides, how it is exposed, and the potential blast radius** across segmented environments.

---

## Core Objective

> Model and analyze data exposure across subnet boundaries to quantify risk concentration and blast radius using DSPM principles.

---

## What This Project Does

Given a set of subnets and data assets, the system:

1. **Maps data to subnets**
   - associates datasets with network segments

2. **Classifies data**
   - sensitivity levels
   - PII and secrets
   - ownership

3. **Builds exposure topology**
   - subnets as nodes  
   - connectivity as edges  
   - data assets attached to nodes  

4. **Analyzes blast radius**
   - identifies propagation paths  
   - computes reachability across segments  

5. **Computes risk metrics**
   - exposure counts per subnet  
   - severity distribution  
   - connectivity-weighted risk  

6. **Generates evidence artifacts**
   - topology outputs  
   - exposure reports  
   - structured JSON and CSV artifacts  

---

## DSPM Lifecycle Coverage

| Stage    | Implementation                                       |
|----------|------------------------------------------------------|
| Discover | Data mapped to subnet segments                       |
| Classify | Sensitivity, PII, secrets, owner                     |
| Audit    | Exposure analysis and risk scoring                   |
| Enforce  | Identification of high-risk segments (informational) |
| Monitor  | Topology and exposure tracking                       |

---

## Exposure Model

The system models:

- **Subnets** → nodes  
- **Connections** → edges  
- **Data assets** → attached to nodes  

Risk is derived from:

- number of sensitive records  
- connectivity degree  
- reachable paths (blast radius)  

---

## Evidence Output

Artifacts written per run to:
