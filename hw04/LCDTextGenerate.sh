#!/bin/bash
#!chmod +x
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background azure -fill black -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'ImageMagick\nECE 434\nEmbedded Linux' \
     -draw "text 75,100 'Nathaniel Craan'" \
     -draw "text 75,150 'Today is Friday!'" \
     $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE