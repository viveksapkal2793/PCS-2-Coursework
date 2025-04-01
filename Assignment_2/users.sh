#!/bin/bash

echo "User Account Information"

# Display the header
printf "%-20s %-15s %-15s %-15s\n" "Username" "User ID" "Home Directory" "Shell"
echo "------------------------------------------------------------"

# Iterate over user accounts
while IFS=: read -r username password uid gid info home shell; do
    # Exclude system users (UID less than 1000)
    if [ "$uid" -ge 1000 ]; then
        # Display user information
        printf "%-20s %-15s %-15s %-15s\n" "$username" "$uid" "$home" "$shell"
    fi
done < /etc/passwd
