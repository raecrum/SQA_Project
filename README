# CFR_TEST – Verification & Validation of 21 CFR Rules

## Project Overview

This project applies **Verification & Validation (V&V)** techniques to regulatory requirements from **21 CFR 117.130**.

We parse a CFR markdown file into structured requirements, generate expected parent-child relationships, create test cases, and validate them using Python scripts and GitHub Actions.

---

## Objectives

* Extract atomic requirements from CFR markdown
* Generate requirement structure mappings
* Create test cases for selected rules
* Perform verification and validation
* Log execution using basic software forensics
* Automate workflow using GitHub Actions

---

## Repository Structure

```id="tree1"
.
├── .github/workflows/ci.yml
├── inputs/
│   └── CFR-117.130.md
├── logs/
│   └── SQA.log
├── scripts/
│   ├── generate_requirements.py
│   ├── generate_test_cases.py
│   ├── verify.py
│   ├── validate.py
│   ├── myLogger.py
│   ├── requirements.json
│   ├── expected_structure.json
│   ├── selected_rules.json
│   └── test_cases.json
├── SQA_report.pdf
├── SQA_screenshots.pdf
└── README.md
```

---

## How to Run (Mac & Windows)

### Requirements

* Python 3.8+
* pip

---

### Setup

```bash id="setup1"
git clone https://github.com/YOUR_TEAM/TEAMNAME-SQA2026-AUBURN.git
cd TEAMNAME-SQA2026-AUBURN
```

---

### Step 1: Generate Requirements

```bash id="run1"
python scripts/generate_requirements.py
```

---

### Step 2: Generate Test Cases

```bash id="run2"
python scripts/generate_test_cases.py
```

---

### Step 3: Run Verification

```bash id="run3"
python scripts/verify.py
```

---

### Step 4: Run Validation

```bash id="run4"
python scripts/validate.py
```

---

## Outputs

Generated files are located in `/scripts`:

* `requirements.json` → parsed requirements
* `expected_structure.json` → parent-child mappings
* `test_cases.json` → generated test cases

---

## Logging & Forensics

* Logs stored in: `logs/SQA.log`
* Tracks:

  * Missing or skipped requirements
  * Validation/verification results
  * Execution status

---

## Deliverables

* Source code and scripts
* Generated JSON outputs
* `SQA_report.pdf` (project report)
* `SQA_screenshots.pdf` (execution evidence)

---

## Team Members

* Rae Crumley
* Claire Weber
* Weida Zhao
