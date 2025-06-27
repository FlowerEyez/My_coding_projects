#!/bin/bash
echo "What is your name?"
read name
echo "How old are you?"
read age
echo "Hello $name, you are $age years old."
sleep 2
echo "Calculating..."
sleep 1
echo "*......."
sleep 1
echo "**......"
sleep 1
echo "****...."
sleep 1
echo "*******."
sleep 3
echo "Loading failed..."
sleep 1
echo "JK"
sleep 1
getrich=$((( $RANDOM % 80 ) + $age ))
echo "$name, you will become a millionaire when you are $getrich years old."
