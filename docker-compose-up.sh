#!/bin/bash


BACKEND_PATH="${PWD}/backend"
BACKEND_NAME="sharefolder-backend"

CLIENT_PATH="${PWD}/client"
CLIENT_NAME="sharefolder-client"

DB_PATH="${PWD}/db/init"
DB_NAME="sharefolder-db"

sharedfolder_exists=`vboxmanage showvminfo default | grep "Name: '${BACKEND_NAME}'"`
if [[ -z $sharedfolder_exists ]]
then
    vboxmanage sharedfolder add default --name ${BACKEND_NAME} --hostpath ${BACKEND_PATH} --transient
else
    echo "[INFO] ${BACKEND_NAME} already set"
fi

sharedfolder_exists=`vboxmanage showvminfo default | grep "Name: '${CLIENT_NAME}'"`
if [[ -z $sharedfolder_exists ]]
then
    vboxmanage sharedfolder add default --name ${CLIENT_NAME} --hostpath ${CLIENT_PATH} --transient
else
    echo "[INFO] ${CLIENT_NAME} already set"
fi

sharedfolder_exists=`vboxmanage showvminfo default | grep "Name: '${DB_NAME}'"`
if [[ -z $sharedfolder_exists ]]
then
    vboxmanage sharedfolder add default --name ${DB_NAME} --hostpath ${DB_PATH} --transient
else
    echo "[INFO] ${DB_NAME} already set"
fi

docker-machine ssh default "sudo mkdir -p ${BACKEND_PATH}"
docker-machine ssh default "sudo mount -t vboxsf -o defaults,uid=`id -u`,gid=`id -g` ${BACKEND_NAME} ${BACKEND_PATH}"

docker-machine ssh default "sudo mkdir -p ${CLIENT_PATH}"
docker-machine ssh default "sudo mount -t vboxsf -o defaults,uid=`id -u`,gid=`id -g` ${CLIENT_NAME} ${CLIENT_PATH}"

docker-machine ssh default "sudo mkdir -p ${DB_PATH}"
docker-machine ssh default "sudo mount -t vboxsf -o defaults,uid=`id -u`,gid=`id -g` ${DB_NAME} ${DB_PATH}"

docker-compose up --build