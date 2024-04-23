# inet_4031_adduser_script


Description: 
This script automates user account creation on Unix/Linux systems by reading user data from standard input and executing system commands to create accounts, set passwords, and assign groups.



Operation Section: 

Each input line should follow the format:

username:password:first_name:last_name:group_data
Where group_data is comma-separated group names or '-' for no group.

Usage
Set script permissions: chmod +x create-users.py

Prepare input: Ensure create-users.input is formatted correctly.

Execute the script: sudo ./create-users.py < create-users.input
Features

Creates user accounts with specified usernames and details.

Sets user passwords securely.

Assigns users to specified groups, if applicable.
