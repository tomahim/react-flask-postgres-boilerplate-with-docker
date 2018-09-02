#!/bin/bash

declare -A arr

arr["sharefolder-backend"]="${PWD}/backend"
arr["sharefolder-client"]="${PWD}/client"
arr["sharefolder-db-init"]="${PWD}/db/init"

for key in ${!arr[@]}; do
    echo ${key} ${arr[${key}]}
    sharedfolder_exists=`vboxmanage showvminfo default | grep "Name: '${key}'"`
    if [[ -z $sharedfolder_exists ]]
    then
        vboxmanage sharedfolder add default --name ${key} --hostpath ${arr[${key}]} --transient
    else
        echo "[INFO] ${key} already set"
    fi
    docker-machine ssh default "sudo mkdir -p ${arr[${key}]}"
    docker-machine ssh default "sudo mount -t vboxsf -o defaults,uid=`id -u`,gid=`id -g` ${key} ${arr[${key}]}"
done

docker-compose up --build