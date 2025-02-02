#!/bin/bash

export RESTIC_REPOSITORY=/home/user/Desktop/res        
export RESTIC_PASSWORD=SUPER-SECRET-PASSWORD

DIRECTORIES=(
    "/home/user/Desktop/secret_data/"
)

DATE=$(date +'%Y-%m-%d_%H-%M-%S')

LOGFILE="/var/log/restic_backup_$DATE.log"

echo "Створення резервної копії: $DATE" >> $LOGFILE
for DIR in "${DIRECTORIES[@]}"; do
    echo "Бекап директорії: $DIR" >> $LOGFILE
    restic backup "$DIR" >> $LOGFILE 2>&1
done

echo "Бекап завершено: $DATE" >> $LOGFILE
