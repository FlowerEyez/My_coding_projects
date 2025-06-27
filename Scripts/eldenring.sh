#!/bin/bash

echo "Welcome, please select your starting class:
1 - warrior
2 - thief
3 - cleric
4 - archer"

read class

case $class in

	1)
		type="warrior"
		hp=20
		attack=15
		magic=0
		;;
	2)
		type="thief"
		hp=5
		attack=25
		magic=5
		;;
	3)
		type="cleric"
		hp=10
		attack=5
		magic=20
		;;
	4)
		type="archer"
		hp=10
		attack=25
		magic=0
		;;
esac

echo "you have choosen the $type class. Your HP is $hp, your attack is $attack, and your magic is $magic."

echo "You Died"

#First beast battle

beast=$(( $RANDOM % 2 ))

echo "you encounter a wild boar... prepare to fight, pick a number between 0 or 1. (0/1)"

read avatar

if [[ $beast == $avatar && 47 > 27 ]]; then
	echo "you killed the wild boar!!!"
else
	echo "You Died"
	exit 1
fi

sleep 2

echo "you encounter Marget The Fell... prepare to fight, pick a number between 0-9 (0/9)"

read avatar

beast=$(( $RANDOM % 10 ))

if [[ $beast == $avatar || $avatar == "coffee" ]]; then
	echo "You killed Marget The Fell"
elif [[ $USER == "anodyne" ]]; then
	echo "Hi, anodyne"
else
        echo "You Died"
        exit 1
fi

