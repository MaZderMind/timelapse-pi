#!/usr/bin/env python3
import datetime
import time
import os

import numpy


def main():
	time_to_shutter_microseconds_map = generate_time_to_shutter_microseconds_map()
	x_axis, y_axis = axes_lists_from_map(time_to_shutter_microseconds_map)

	while True:
		now = datetime.datetime.now()
		second_of_today = second_of_day(now.time())
		shutter = numpy.interp(second_of_today, x_axis, y_axis)
		filename = "/opt/timelapse/images/{year:04}-{month:02}-{day:02}___{hour:02}-{minute:02}-{second:02}.jpg".format(
			year=now.year,
			month=now.month,
			day=now.day,
			hour=now.hour,
			minute=now.minute,
			second=now.second)

		record_snapshot(shutter, filename)
		time.sleep(2.5)

def record_snapshot(shutter, filename):
	cmdline = "raspistill --verbose --hflip --vflip -ss {shutter} --awb off --awbgains 1.5,1.3 --exposure off --ISO 100 --metering matrix --ev -24 -o {filename} --timeout 0".format(
		shutter=shutter,
		filename=filename)

	print("{filename} shutter={shutter}".format(
		shutter=shutter,
		filename=filename))

	os.system(cmdline)


def generate_time_to_shutter_microseconds_map():
	return {
		second_of_day(datetime.time( 8,  0)): 10000,
		second_of_day(datetime.time(12,  0)):  3000,
		second_of_day(datetime.time(16, 30)):  3000,
		second_of_day(datetime.time(18,  0)):  8000,
		second_of_day(datetime.time(20,  0)): 15000,
	}

def second_of_day(timestamp):
	return timestamp.second + timestamp.minute * 60 + timestamp.hour * 60 * 60


def axes_lists_from_map(map):
	x_axis = sorted(map.keys())
	y_axis = [map[x] for x in x_axis]

	return x_axis, y_axis

if __name__ == '__main__':
	main()
