#!/bin/bash

# Script to open articles from APS journals (see link.aps.org)
# tc, 2014-04-04

# Choose a browser
BROWSER=firefox

# If you want to use a proxy, uncomment the next line and set the correct address
#PROXY=.proxy.example.university.org


echo
echo '*********************************************************************'
echo
echo 'Script to fetch articles from APS journals (PRL,PRA,PRB,RMP,..)'
echo

#Input
read -p "Journal? [PRL]  " JOURNAL
read -p "Volume? " VOLUME
read -p "Page? " PAGE
HOMEPAGE=0

# Check journal
if [ "$JOURNAL" == 'a' ]; then JOURNAL=PRA; fi;
if [ "$JOURNAL" == 'b' ]; then JOURNAL=PRB; fi;
if [ "$JOURNAL" == 'c' ]; then JOURNAL=PRC; fi;
if [ "$JOURNAL" == 'd' ]; then JOURNAL=PRD; fi;
if [ "$JOURNAL" == 'e' ]; then JOURNAL=PRE; fi;
if [ "$JOURNAL" == 'PRA' ]; then JOURNAL_long=PhysRevA; fi;
if [ "$JOURNAL" == 'PRB' ]; then JOURNAL_long=PhysRevB; fi;
if [ "$JOURNAL" == 'PRC' ]; then JOURNAL_long=PhysRevC; fi;
if [ "$JOURNAL" == 'PRD' ]; then JOURNAL_long=PhysRevD; fi;
if [ "$JOURNAL" == 'PRE' ]; then JOURNAL_long=PhysRevE; fi;

JOURNAL_lo=`echo $JOURNAL | tr [:upper:] [:lower:]`
JOURNAL_up=`echo $JOURNAL | tr [:lower:] [:upper:]`
if [ "$JOURNAL_lo" == 'prl' ] || [ "$JOURNAL_lo" == 'pra' ] || [ "$JOURNAL_lo" == 'prb' ] || [ "$JOURNAL_lo" == 'rmp' ] || [ "$JOURNAL_lo" == 'prc' ] || [ "$JOURNAL_lo" == 'prd' ] || [ "$JOURNAL_lo" == 'pre' ]; then
 echo '  journal set to '$JOURNAL_up
else
 echo '  journal set to PRL by default';
 JOURNAL=PRL; JOURNAL_lo=prl; JOURNAL_up=PRL; JOURNAL_long=PhysRevLett
fi

# Check volume
if [[ $VOLUME =~ ^[\-0-9]+$ ]] && (( VOLUME > 0)); then
 echo '  volume set to '$VOLUME
else
 HOMEPAGE=1
 echo '  wrong volume number -> journal homepage'
fi

# Check page
#if [[ $PAGE =~ ^[\-0-9]+$ ]] && (( $PAGE > 0)); then
echo '  page set to '$PAGE
#else
# HOMEPAGE=1
# echo '  wrong page number -> journal homepage'
#fi

if [ "$HOMEPAGE" == '0' ]; then
 LINK=http://journals.aps.org$PROXY/$JOURNAL_lo/abstract/10.1103/$JOURNAL_long.$VOLUME.$PAGE
else
 LINK=http://$JOURNAL_lo.aps.org$PROXY;
fi

echo
echo 'Trying to open the following link: '$LINK
echo
echo '*********************************************************************'
echo

$BROWSER $LINK &
