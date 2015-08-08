#!/bin/bash

# program:       aps_article.sh
# author:        tc
# last modified: 2015-08-08 -- 17:30 CEST
# notes:         opens articles from APS journals (see link.aps.org)

# Choose a browser
BROWSER=firefox

# If you want to use a proxy, uncomment the next line and set the correct address
#PROXY=.proxyname.someuniversity.fr


echo
echo '*********************************************************************'
echo
echo 'Script to fetch articles from APS journals (PRL, PR{A,B,C,D,E,X}, RMP)'
echo

#Input
read -p "Journal? [default: PRL, other options: a, b, c, d, e, x, rmp]  " JOURNAL
read -p "Volume? " VOLUME
read -p "Page? " PAGE
HOMEPAGE=0

# Check journal
if [ "$JOURNAL" == 'a' ];   then JOURNAL=PRA; JOURNAL_long=PhysRevA; fi;
if [ "$JOURNAL" == 'b' ];   then JOURNAL=PRB; JOURNAL_long=PhysRevB; fi;
if [ "$JOURNAL" == 'c' ];   then JOURNAL=PRC; JOURNAL_long=PhysRevC; fi;
if [ "$JOURNAL" == 'd' ];   then JOURNAL=PRD; JOURNAL_long=PhysRevD; fi;
if [ "$JOURNAL" == 'e' ];   then JOURNAL=PRE; JOURNAL_long=PhysRevE; fi;
if [ "$JOURNAL" == 'x' ];   then JOURNAL=PRX; JOURNAL_long=PhysRevX; fi;
if [ "$JOURNAL" == 'rmp' ]; then JOURNAL=RMP; JOURNAL_long=RevModPhys; fi;

JOURNAL_lo=`echo $JOURNAL | tr [:upper:] [:lower:]`
JOURNAL_up=`echo $JOURNAL | tr [:lower:] [:upper:]`
if [ "$JOURNAL_lo" == 'prl' ] || [ "$JOURNAL_lo" == 'pra' ] || [ "$JOURNAL_lo" == 'prb' ] || [ "$JOURNAL_lo" == 'rmp' ] || [ "$JOURNAL_lo" == 'prc' ] || [ "$JOURNAL_lo" == 'prd' ] || [ "$JOURNAL_lo" == 'pre' ] || [ "$JOURNAL_lo" == 'prx' ]; then
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
echo '  page set to '$PAGE

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
