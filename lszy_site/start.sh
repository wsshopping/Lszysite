#! /bin/sh

pkill nohup
nohup python  manage.py runserver &

cd ../nginx/sbin
killall  -9 nginx  
./nginx -p ../


