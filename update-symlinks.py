#!/usr/bin/env python3
#
import os
import os.path
import re
import sys
from datetime import datetime

try:
	basedir = sys.argv[1]
except IndexError:
	basedir = '.';

print("scanning directory", basedir)
for filename in os.listdir(basedir):
	match = re.match('lapse-([0-9]+)\.jpg', filename)
	if not match:
		continue

	recorded_at = datetime.fromtimestamp(int(match.group(1)))
	symlink_directory = 'year-{year:04}/month-{month:02}/day-{day:02}/hour-{hour:02}'.format(
		year=recorded_at.year,
		month=recorded_at.month,
		day=recorded_at.day,
		hour=recorded_at.hour)

	symlink_filename = '{hour:02}-{minute:02}-{second:02}.jpg'.format(
		hour=recorded_at.hour,
		minute=recorded_at.minute,
		second=recorded_at.second)

	symlink_filepath = os.path.join(symlink_directory, symlink_filename)
	symlink_sourcepath = os.path.join('../../../..', basedir, filename)

	print(filename, " -> ", symlink_filepath)
	try:
		os.makedirs(symlink_directory)
		os.symlink(symlink_sourcepath, symlink_filepath)
	except FileExistsError:
		pass

print("done")
