#!/bin/bash

# Script to open articles from APS journals (see link.aps.org)
# tc, 2013-07-21



# Choose a browser
BROWSER=firefox

# If you want to use a proxy, uncomment the next two lines and set the correct address
#PROXY=proxy.library.uu.nl
#PROXY='.'$PROXY



echo
echo '*********************************************************************'
echo
echo 'Script to fetch articles from APS journals (PRL,PRA,PRB,RMP,..)'
echo

#Input
read -p "Journal? [PRL]  " JOURNAL
read -p "Volume? " VOLUME
read -p "Page? " PAGE

# Check journal
JOURNAL_lo=`echo $JOURNAL | tr [:upper:] [:lower:]`
JOURNAL_up=`echo $JOURNAL | tr [:lower:] [:upper:]`
if [ "$JOURNAL_lo" == 'prl' ] || [ "$JOURNAL_lo" == 'pra' ] || [ "$JOURNAL_lo" == 'prb' ] || [ "$JOURNAL_lo" == 'rmp' ] || [ "$JOURNAL_lo" == 'prc' ] || [ "$JOURNAL_lo" == 'prd' ] || [ "$JOURNAL_lo" == 'pre' ]; then
 echo '  journal set to '$JOURNAL_up
else
 echo '  journal set to PRL by default';
 JOURNAL=PRL
fi

# Check volume
if [[ $VOLUME =~ ^[\-0-9]+$ ]] && (( VOLUME > 0)); then
 echo '  volume set to '$VOLUME
else
 VOLUME=1
 echo '  volume number set to 1 by default'
fi

# Check page
if [[ $PAGE =~ ^[\-0-9]+$ ]] && (( PAGE > 0)); then
 echo '  page set to '$PAGE
else
 PAGE=1
 echo '  page number set to 1 by default'
fi

LINK=http://link.aps.org$PROXY/abstract/$JOURNAL/v$VOLUME/p$PAGE

echo
echo 'Trying to open the following link: '$LINK
echo
echo '*********************************************************************'
echo

$BROWSER $LINK &> /dev/null &
