#!/usr/bin/env python3

import os
import shutil
from datetime import datetime, timedelta

# Backup variables
backup_dir = "/path/to/backup/directory"
backup_prefix = "backup_{}".format(datetime.now().strftime("%Y-%m-%d"))
backup_count = 10

# Current date
current_date = datetime.now().strftime("%Y%m%d")

# Generate backup filename
backup_filename = "{}-{}.tar.gz".format(backup_prefix, current_date)

# Create backup directory if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Remove backups older than backup_count days
for file in os.listdir(backup_dir):
    if file.startswith("backup_"):
        file_date_str = file.split("_")[1].split(".")[0]
        file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
        if datetime.now() - file_date > timedelta(days=backup_count):
            os.remove(os.path.join(backup_dir, file))

# Perform the incremental backup using shutil.copytree
latest_backup_dir = os.path.join(backup_dir, "latest")
shutil.copytree(os.path.expanduser("~"), os.path.join(backup_dir, backup_filename), symlinks=True, dirs_exist_ok=True)

# Create a symbolic link to the latest backup
if os.path.islink(latest_backup_dir):
    os.unlink(latest_backup_dir)
os.symlink(os.path.join(backup_dir, backup_filename), latest_backup_dir)
