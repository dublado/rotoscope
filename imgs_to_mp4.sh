#!/bin/sh

cd $1

palette="/tmp/palette.png"

filters="fps=24"

ffmpeg -nostats -loglevel 0 -framerate 24 -pattern_type glob -i '*.bmp' -vf "$filters,palettegen" -y $palette
ffmpeg -nostats -loglevel 0 -framerate 24 -pattern_type glob -i '*.bmp' -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $2
