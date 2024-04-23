#!/usr/bin/python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Check if the line is properly formatted with five fields separated by ':'
        fields = line.strip().split(':')
        if len(fields) != 5:
            continue

        username, password, first_name, last_name, group_data = fields

        # Construct the GECOS field for the user
        gecos = f"{first_name} {last_name},,,"
        
        # Split the groups and filter out any '-' indicating no group
        groups = [group.strip() for group in group_data.split(',') if group != '-']

        # Print a message about account creation
        print(f"Creating account for {username}...")
        
        # Create the user account without a password
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        os.system(cmd)

        # Print a message about setting the password
        print(f"==> Setting the password for {username}...")
        cmd = f"echo '{password}\n{password}' | sudo passwd {username}"
        os.system(cmd)

        # Assign the user to the specified groups
        for group in groups:
            if group:
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                os.system(cmd)

if __name__ == "__main__":
    main()
