# CybersecurityProject

Verification code: WTC-A7YZ9GGC


# File Integrity Monitor

A Python-based cybersecurity project that detects unauthorized or unexpected changes to files by comparing their current SHA-256 hashes against a trusted baseline.

## Overview

File integrity is an important part of cybersecurity. If an attacker modifies, replaces, adds, or deletes files on a system, those changes can potentially affect the system's security or functionality.

This project implements a simple **File Integrity Monitor (FIM)** using Python.

The monitor creates a trusted baseline of files and their SHA-256 hashes. During an integrity check, it compares the current state of the monitored directory against that baseline and reports any changes.

The project was developed as part of a cybersecurity elective to demonstrate practical security concepts including hashing, integrity monitoring, baselines, and automated testing.

---

## Cybersecurity Concept

This project focuses on **Integrity**, one of the three principles of the **CIA Triad**:

* **Confidentiality** – protecting information from unauthorized access.
* **Integrity** – ensuring information has not been changed without authorization.
* **Availability** – ensuring systems and information remain accessible.

The File Integrity Monitor focuses specifically on **Integrity** by detecting changes to files.

A FIM does not prevent a file from being changed. Instead, it detects that a change has occurred by comparing the current file against a previously trusted state.

---

## How It Works

The monitor uses **SHA-256 hashing** to create a digital fingerprint for each file.

The process is:

```text
                CREATE BASELINE
                      │
                      ▼
              Scan monitored files
                      │
                      ▼
              Calculate SHA-256
```
