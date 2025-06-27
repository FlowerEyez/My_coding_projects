#!/bin/bash

#check to see if the internet is down

echo "What website do you want to check?"
read target

while true
do
  if ping -q -c 2 -w 1 $target > /dev/null; then
    echo "Hey, It works"
    break
  else
    echo "Not working..."
  fi
sleep 2
done
