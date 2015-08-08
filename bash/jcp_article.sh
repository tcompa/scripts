#!/bin/bash

# Script to open articles from JChemPhys
# tc, 2014-08-29

# Choose a browser
BROWSER=firefox


echo
echo '*********************************************************************'
echo
echo 'Script to fetch articles from JChemPhys'
echo

#Input
read -p "Volume? " VOLUME
read -p "Page? " PAGE
HOMEPAGE=0

# Check volume
if [[ $VOLUME =~ ^[\-0-9]+$ ]] && (( VOLUME > 0)); then
 echo '  volume set to '$VOLUME
else
 HOMEPAGE=1
 echo '  wrong volume number -> journal homepage'
fi

echo '  page set to '$PAGE

if [ "$HOMEPAGE" == '0' ]; then
 LINK="http://scitation.aip.org/search?noRedirect=true&value8=%22The+Journal+of+Chemical+Physics%22&option8=journalbooktitle&operator12=AND&option12=resultCategory&value12=ResearchPublicationContent&operator13=AND&value13=${VOLUME}&option13=prism_volume&operator14=AND&value14=${PAGE}&option14=elocationpage"
else
 LINK=http://scitation.aip.org/content/aip/journal/jcp#
fi

echo
echo 'Trying to open the following link: '$LINK
echo
echo '*********************************************************************'
echo

$BROWSER $LINK &
