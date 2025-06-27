#!/bin/bash
for x in google.com bing.com youtube.com newgrounds.com wikipedia.com;
do
  if ping -q -c 2 -w 1 $x > /dev/null; then
    echo "$x is up"
  else
    echo "$x is down"
  fi
done
