#!/bin/bash

#
#   uninstall script for animal
#   reference: https://unix.stackexchange.com/questions/28791/prompt-for-sudo-password-and-programmatically-elevate-privilege-in-bash-script
#

# check for super user privilege
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

echo "Start uninstalling..."

# function exit with error
function exit_with_error {
    echo $1
    echo "Uninstallation fails."
    exit 1
}

# delete symbolic link to animalsay.py in /usr/local/bin
if ! rm /usr/local/bin/animal; then
    exit_with_error "Unable to delete /usr/local/bin/animal"
fi

# delete symbolic link to auto complete script in /etc/bash_completion.d
if ! rm /etc/bash_completion.d/animal; then
    exit_with_error "Unable to delete /etc/bash_completion.d/animal"
fi

echo "\'animal\' has been uninstall!"
