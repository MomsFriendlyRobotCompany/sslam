#!/usr/bin/env python2

from __future__ import division
from __future__ import print_function
from sslam import RMHC_SLAM
from sslam import LDS01_Model
from pydar import LDS01
from pltslamshow import SlamShow


if __name__ == '__main__':

	MAP_SIZE_PIXELS         = 500
	MAP_SIZE_METERS         = 10
	LIDAR_DEVICE            = "/dev/tty.SLAB_USBtoUART"

	# Connect to Lidar unit
	lidar = LDS01()
	lidar.open(LIDAR_DEVICE)
	lidar.run(True)

	# Create an RMHC SLAM object with a laser model and optional robot model
	slam = RMHC_SLAM(LDS01_Model(), MAP_SIZE_PIXELS, MAP_SIZE_METERS)

	# Set up a SLAM display
	display = SlamShow(MAP_SIZE_PIXELS, MAP_SIZE_METERS*1000/MAP_SIZE_PIXELS, 'SLAM')

	# Initialize empty map
	mapbytes = bytearray(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS)

	try:
		while True:

			# Update SLAM with current Lidar scan
			pts = lidar.read()
			# need to reverse the order for it to plot correctly
			pts = list(reversed(pts)))

			slam.update(pts)

			# Get current robot position
			x, y, theta = slam.getpos()

			# Get current map bytes as grayscale
			slam.getmap(mapbytes)

			display.displayMap(mapbytes)
			display.setPose(x, y, theta)
			display.refresh()
			
	except KeyboardInterrupt:
		lidar.close()
