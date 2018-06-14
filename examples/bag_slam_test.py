#!/usr/bin/env python2
# MIT License Kevin Walchko (c) 2018
#
# this needs: pip install the-collector
# this needs: pip install matplotlib

from __future__ import division
from __future__ import print_function
from the_collector.bagit import BagReader
from sslam import LDS01_Model
from pltslamshow import SlamShow
from sslam import RMHC_SLAM
import time


if __name__ == '__main__':
	MAP_SIZE_PIXELS         = 500
	MAP_SIZE_METERS         = 8

	reader = BagReader()
	data = reader.load('test.json')  # read in the file and conver to dict
	scans = data['lidar']
	slam = RMHC_SLAM(LDS01_Model(), MAP_SIZE_PIXELS, MAP_SIZE_METERS)
	display = SlamShow(MAP_SIZE_PIXELS, MAP_SIZE_METERS*1000/MAP_SIZE_PIXELS, 'SLAM')

	# Initialize empty map
	mapbytes = bytearray(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS)

	try:
		# scans = [[data, timestamp], ....]
		for pts, dt in scans:
			# need to reverse the order for it to plot correctly
			slam.update(list(reversed(pts)))

			# Get current robot position
			x, y, theta = slam.getpos()

			# Get current map bytes as grayscale
			slam.getmap(mapbytes)

			# display map
			display.displayMap(mapbytes)
			display.setPose(x, y, theta)
			display.refresh()

			# scan is 5 Hz
			time.sleep(1/5)

		while True:  # just leave it up and running for a while
			continue
	except KeyboardInterrupt:
		print("got ctrl-C ...")
