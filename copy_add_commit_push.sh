#!/bin/bash

WORKDIR=/home/ttt/th-work/report
DATE=`date +"%Y%m%d-%H%M"`
echo "##############################################################################################"
echo


ls -lh $WORKDIR/*.tex;
echo;
read -p "Copy all the .tex files from $WORKDIR (y/n)? ";
[ "$REPLY" == "y" ] && cp $WORKDIR/*.tex . -v;
[ "$REPLY" == "y" ] ||
	{
	echo "Ok, see you.";
	echo;
	exit 1;
	}

echo;
echo "##############################################################################################"
echo
ls -lh *.tex
echo;
read -p "Git add all the .tex files (y/n)? ";
[ "$REPLY" == "y" ] &&
	{
		for FILE in `ls *.tex`; do
			git add $FILE ;
		done;
	}
[ "$REPLY" == "y" ] ||
	{
		echo "Ok, see you.";
		echo;
		exit 2;
	}

echo;
echo "##############################################################################################"
echo
echo "git status -s"
echo;
git status -s;
echo "##############################################################################################"
echo

read -p "Commit (y/n)? "
[ "$REPLY" == "y" ] && git commit -m "$DATE update";
[ "$REPLY" == "y" ] || {
		echo "Not committing.. Ok, as you like.."
		echo "See you."
		exit 3;
	}
echo;
echo "##############################################################################################"
echo
read -p "Push (y/n)? "
[ "$REPLY" == "y" ] && git push origin master

echo;
echo "##############################################################################################"

exit 0;


