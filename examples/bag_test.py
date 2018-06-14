#!/usr/bin/env python2
# MIT License Kevin Walchko (c) 2018
#
# this needs: pip install the-collector

from __future__ import division
from __future__ import print_function
import matplotlib.pyplot as plt
import time
from math import pi
from the_collector.bagit import BagReader


if __name__ == '__main__':
	reader = BagReader()
	data = reader.load('test.json')  # read in the file and conver to dict
	scans = data['lidar']
	# need to reverse the order for it to plot correctly
	scans = list(reversed(scans)))

	theta = [i*2*pi/360 for i in range(360)]

	plt.ion()
	plt.grid(True)

	# scans = [[data, timestamp], ....]
	for pts, dt in scans:
		plt.subplot(111, projection='polar')
		plt.plot(theta, pts)
		plt.draw()
		plt.pause(0.2)
		plt.clf()
