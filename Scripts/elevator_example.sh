#!/bin/bash

echo "Welcome to the Elevator Test"
sleep 1
echo "going up..."
sleep 1

for x in {1..17};
do
  if [[ $x == 13 ]]; then
    continue
  fi
  echo "floor $x"
  sleep 1
done
