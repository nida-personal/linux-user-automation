import csv
import yaml
import os

# Paths
CSV_FILE = "users.csv"
VARS_FILE = "ansible/roles/manage_users/vars/main.yml"

def read_users_from_csv(csv_file):
    """Read user data from CSV and return list of user dicts."""
    users = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append({
                "username": row["username"].strip(),
                "full_name": row["full_name"].strip(),
                "group": row["group"].strip(),
                "sudo_access": row["sudo_access"].strip().lower() == "yes",
                "state": row["state"].strip()
            })
    return users

def write_vars_file(users, vars_file):
    """Write users list to Ansible vars YAML file."""
    data = {"manage_users_users": users}
    os.makedirs(os.path.dirname(vars_file), exist_ok=True)
    with open(vars_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    print(f"vars file written to: {vars_file}")
    print(f"Total users processed: {len(users)}")
    for user in users:
        print(f"  - {user['username']} | group: {user['group']} | "
              f"sudo: {user['sudo_access']} | state: {user['state']}")

if __name__ == "__main__":
    users = read_users_from_csv(CSV_FILE)
    write_vars_file(users, VARS_FILE)
