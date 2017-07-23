#!/bin/bash

#
#   install script for animal
#   reference: https://unix.stackexchange.com/questions/28791/prompt-for-sudo-password-and-programmatically-elevate-privilege-in-bash-script
#

# check for super user privilege
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

echo "Start setting up..."

# current working directory
path=`echo ${PWD}/`

# function exit with error
function exit_with_error {
    echo $1
    echo "Installation fails."
    exit 1
}

# make sure scripts are executable
if ! chsmod +x animalsay.py animal_auto_complete.sh; then
    exit_with_error "Unable to make animalsay.py animal_auto_complete.sh executable."
fi

# create symbolic link to animalsay.py in /usr/local/bin
if ! ln -s ${path}animalsay.py /usr/local/bin/animal; then
    exit_with_error "Unable to create symbolic link to animalsay.py in /usr/local/bin"
fi

# create symbolic link to auto complete script in /etc/bash_completion.d
if ! ln -s ${path}animal_auto_complete.sh /etc/bash_completion.d/animal; then
    exit_with_error "Unable to create symbolic link to auto complete script in /etc/bash_completion.d"
fi

echo "Done!"