#!/bin/bash

# program: list_all_ppa.sh
# last-modified: tc, 2015-08-05 -- 18:42 CEST
# description: gets all the PPA installed on a system.
# source: http://askubuntu.com/questions/148932/how-can-i-get-a-list-of-all-repositories-and-ppas-from-the-command-line

for APT in `find /etc/apt/ -name \*.list`; do
    grep -o "^deb http://ppa.launchpad.net/[a-z0-9\-]\+/[a-z0-9\-]\+" $APT | while read ENTRY ; do
        USER=`echo $ENTRY | cut -d/ -f4`
        PPA=`echo $ENTRY | cut -d/ -f5`
        echo sudo apt-add-repository ppa:$USER/$PPA
    done
done

echo
echo -e "Note 1 (tc): there might be a small bug with names which include a dot."
echo -e "Note 2 (tc): to remove a ppa, use "
echo -e "  sudo add-apt-repository --remove ppa:whatever/ppa"
echo
