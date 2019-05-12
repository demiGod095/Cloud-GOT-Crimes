#!/bin/bash

. ./unimelb-comp90024-group-52-openrc.sh; ansible-playbook -i hosts -u ubuntu --key-file=~/.ssh/id_alwyn wordpress.yaml