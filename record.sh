#!/bin/sh
raspistill --verbose --hflip --vflip -ss 4000 --awb off --awbgains 1.5,1.3 --exposure off --ISO 100 --metering matrix --ev -24 -o /opt/timelapse/images/lapse-%d.jpg --datetime --timelapse 10000 --timeout 0
