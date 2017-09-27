#!/bin/bash

#SELECT="year-2017/month-10/day-{02..14}/hour-{08..18}/*.jpg"
#SELECT="year-2017/month-*/day-*/hour-{08..18}/*.jpg"
SELECT="/mnt/timelapse/day-5/lapse-927{08..20}*.jpg"

for FPS in 60 25; do
	eval cat $SELECT | ffmpeg -hide_banner -y -nostdin -threads 16 -r $FPS -f image2pipe -i - -vf scale=-1:1080 -analyzeduration 20000000 -c:v:0 libx264 -pix_fmt yuv420p -bufsize:0 8192k -crf:0 20 -minrate:0 100k -maxrate:0 5000k -profile:0 main -level:0 4.0 -threads 8 -movflags +faststart -f mp4 lapse-${FPS}fps.mp4
done
