#!/bin/bash

#
#   animal command auto completion script
#   reference: https://askubuntu.com/questions/68175/how-to-create-script-with-auto-complete
#

_animal()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="-l --list -h --help -q --quote -s --say -n --natural -i --insult -c --communism -g --got -r --reference"
    animal_list=$(cat /home/hung/opt/animalsay/animal_list.txt | tr "\n" " ")
    animal_list=$(echo ${animal_list} any)

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    else
        COMPREPLY=( $(compgen -W "${animal_list}" -- ${cur}) )
        return 0
    fi
}

complete -F _animal animal
