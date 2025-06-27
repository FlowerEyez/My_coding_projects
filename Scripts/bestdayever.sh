#!/bin/bash
compliment=$1
user=$(whoami)
date=$(date)
whereami=$(pwd)
echo "Good morning $user!"
sleep 1
echo "You're looking good $user."
sleep 1
echo "you're $compliment looks nice today!"
sleep 2
echo "You are currently logged in as $user and you are in the directory $whereami. Also today is: $date"
