#!/bin/bash

# Backup variables
backup_dir="/path/to/backup/directory"
backup_prefix="backup_$(date +%Y-%m-%d)"
backup_count=10

# Current date
current_date=$(date +%Y%m%d)

# Generate backup filename
backup_filename="$backup_prefix-$current_date.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Remove backups older than backup_count days
find "$backup_dir" -name "backup_*" -mtime +$backup_count -exec rm {} \;

# Perform the incremental backup using rsync
rsync -a --link-dest="$backup_dir/latest" "$HOME" "$backup_dir/$backup_filename"

# Create a symbolic link to the latest backup
rm -f "$backup_dir/latest"
ln -s "$backup_filename" "$backup_dir/latest"
