# Linux User Management Automation

## Problem This Solves
Managing Linux users manually across multiple servers is 
time-consuming and error-prone. This project automates 
user provisioning, group assignment, sudo access, and 
de-provisioning from a single CSV file — the same problem 
I solved at enterprise scale at TCS across 1,200+ nodes.

## How It Works
users.csv → generate_vars.py → vars/main.yml → Ansible Role → Linux Servers

## Technologies Used
- Python 3 — CSV parsing and YAML generation
- Ansible — user provisioning and de-provisioning
- Jinja2 — sudoers template generation
- GitHub Actions — CI validation on every push
- GCP Compute Engine — test environment

## Project Structure
linux-user-automation/
├── users.csv # Input: user list
├── scripts/
│ └── generate_vars.py # Python: CSV to Ansible vars
├── ansible/
│ ├── playbook.yml # Master playbook
│ └── roles/
│ └── manage_users/
│ ├── tasks/main.yml # User management tasks
│ ├── templates/ # Jinja2 sudoers template
│ └── vars/main.yml # Generated user variables
└── .github/workflows/ci.yml # GitHub Actions CI pipeline

## How To Run

### Step 1 — Add users to CSV
Edit users.csv:
username,full_name,group,sudo_access,state
john_doe,John Doe,developers,yes,present

state: present = create user
state: absent  = delete user

### Step 2 — Generate Ansible vars
```bash
python scripts/generate_vars.py
```

### Step 3 — Run Ansible playbook
```bash
ansible-playbook ansible/playbook.yml -i ansible/inventory.ini
```

## What It Does
- Creates Linux users with correct group assignments
- Assigns sudo access via validated sudoers files
- Removes users and cleans up sudo access when state=absent
- Idempotent — safe to run multiple times with same result

## CI Pipeline
Every push to main triggers GitHub Actions which:
- Installs Ansible and ansible-lint
- Runs the Python script to validate CSV parsing
- Runs ansible-lint to validate playbook quality

## What I Learned
- Built the Python-to-Ansible bridge I managed conceptually
  at TCS but never built from scratch
- Understood Jinja2 templating for real system config files
- Practiced idempotent design — core Ansible principle
- Set up a real CI pipeline that validates on every commit
