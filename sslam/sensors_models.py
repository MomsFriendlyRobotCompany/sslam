# LGPL
# Copyright (c) 2018 Kevin J. Walchko
# Copyright (C) 2014 Suraj Bajracharya and Simon D. Levy

from __future__ import division
from __future__ import print_function


class Laser_Model(object):
	'''
	A class representing the specifications of a scanning laser rangefinder (Lidar).
	'''
	def __init__(self, scan_size, scan_rate_hz, detection_angle_degrees, distance_no_detection_mm, detection_margin=0, offset_mm=0):

		self.scan_size = scan_size
		self.scan_rate_hz = scan_rate_hz
		self.detection_angle_degrees = detection_angle_degrees
		self.distance_no_detection_mm = distance_no_detection_mm
		self.detection_margin = detection_margin
		self.offset_mm = offset_mm

	def __str__(self):

		return  'scan_size=%d | scan_rate=%3.3f hz | detection_angle=%3.3f deg | distance_no_detection=%7.4f mm | detection_margin=%d | offset=%4.4f m' % \
		(self.scan_size,  self.scan_rate_hz,  self.detection_angle_degrees, self.distance_no_detection_mm,  self.detection_margin, self.offset_mm)

	def __repr__(self):

		return str(self)

class LDS01_Model(Laser_Model):
	'''
	A class for
	scan_size, scan_rate_hz, detection_angle_degrees, distance_no_detection_mm, detection_margin=0, offset_mm=0
	'''
	def __init__(self, detectionMargin = 0, offsetMillimeters = 0):
		Laser_Model.__init__(self, 360, 5, 360, 120, detectionMargin, offsetMillimeters)

class URG04LX_Model(Laser_Model):
	'''
	A class for the Hokuyo URG-04LX
	'''
	def __init__(self, detectionMargin = 0, offsetMillimeters = 0):
		Laser.__init__(self, 682, 10, 240, 4000, detectionMargin, offsetMillimeters)

class XVLidar_Model(Laser_Model):
	'''
	A class for the GetSurreal XVLidar
	'''
	def __init__(self, detectionMargin = 0, offsetMillimeters = 0):
		Laser.__init__(self, 360, 5.5, 360, 6000, detectionMargin, offsetMillimeters)
