#!/ bin/bash

HOMEPATH="/opt/flask-demo/scripts"

echo $HOMEPATH

if [[ $1 == "" ]]; then
    echo "Usage:\n    sh ./install.sh [ol test dev]"
    exit
fi

find $HOMEPATH | grep .pyc$ | xargs rm -f

#################################
CONF="/opt/fubang/data_monit/virt_device/conf"
rm -f $CONF/config.py
ln -s $CONF/config_$1.py $CONF/config.py


###########################
cp ./*.service /usr/lib/systemd/system/

systemctl daemon-reload

