# Linux User Management Automation

## Problem This Solves
Managing Linux users manually across multiple servers is 
time-consuming and error-prone. This project automates 
user provisioning, group assignment, sudo access, and 
de-provisioning from a single CSV file.

## Architecture
users.csv → generate_vars.py → vars/main.yml → Ansible Role → Linux Servers

## Technologies Used
- Python 3 — CSV parsing and YAML generation
- Ansible — user provisioning and de-provisioning
- Jinja2 — sudoers template generation
- GitHub Actions — CI validation on every push
- GCP Compute Engine — test environment

## How To Run

### Step 1 — Add users to CSV
Edit users.csv with your user details.

### Step 2 — Generate Ansible vars
```bash
python scripts/generate_vars.py
```

### Step 3 — Run Ansible playbook
```bash
ansible-playbook ansible/playbook.yml -i inventory.ini
```

## What It Does
- Creates Linux users with correct groups
- Assigns sudo access via validated sudoers files
- Removes users and their sudo access when state=absent
- Idempotent — safe to run multiple times

## What I Learned
- Built the Python-to-Ansible bridge I used conceptually
  at TCS but never built from scratch
- Learned Jinja2 templating for system config files
- Understood idempotent design in practice not just theory

## Screenshot
[Screenshot after testing on GCP]
