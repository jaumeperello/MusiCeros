#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

if [ "$1" == "start" ]; then
    echo "starting"
    cd $DIR
    source myvenv/bin/activate
    cp logs/out.MusiCeros.log error/
    nohup python MusiCeros_bot.py > logs/out.MusiCeros.log 2>&1 &  
    echo "started"
fi

if [ "$1" == "stop" ]; then
    ps -ef | grep "python MusiCeros_bot.py" | grep -v grep | awk '{print $2}' | xargs kill
    echo "stopped"
fi

if [ "$1" == "status" ]; then
    echo "status"
    ps -ef | grep "python MusiCeros_bot.py" | grep -v grep
fi

if [ "$1" == "reboot" ]; then
    ps -ef | grep "python MusiCeros_bot.py" | grep -v grep | awk '{print $2}' | xargs kill
    echo "stopped"
    sleep 5
    cd $DIR
    source myvenv/bin/activate
    cp logs/out.MusiCeros_bot.log error/
    nohup python MusiCeros_bot.py > logs/out.MusiCeros_bot.log 2>&1 &  
    echo "started"    
fi
