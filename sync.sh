#!/bin/sh
while true; do
	rsync --remove-source-files --exclude "*~" --progress -av /opt/timelapse/images/ camera-pi@disks:/volume1/data/Transfer/timelapse/
	echo "done, sleeping"
	sleep 5
done
