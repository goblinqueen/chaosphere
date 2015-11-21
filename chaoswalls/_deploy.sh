#! /bin/bash

yandex-disk status >/dev/null

if [ $? -eq 0 ]
then
  echo "Disk is running"
else
  echo "Disk is not running, attempting startup"
  yandex-disk start
  if [ $? -eq 0 ]
  then
    echo "Success"
  else
    exit $?
  fi
fi

echo "Synchronising images"
rsync -v /home/eltha/Yandex.Disk/chaoswalls/images/* images
if [ $? -eq 0 ]
then
  echo "Success"
else
  exit $?
fi

appcfg.py -A chaoswalls update app.yaml

