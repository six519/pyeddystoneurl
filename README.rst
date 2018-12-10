pyeddystoneurl
==============

Python C Extension To Scan Eddystone-URL Bluetooth Low Energy Beacons

Scanning With Non-Root User
===========================
::

	sudo setcap cap_net_raw+ep /pythonpath/python

Install Requirements For Linux (Ubuntu, Debian)
===============================================
::

	sudo apt-get install libbluetooth-dev

Install Requirements For Linux (Red Hat, CentOS, Fedora)
========================================================
::

	sudo yum install bluez-libs-devel

Installing Through PyPi
=======================
::

	pip install pyeddystoneurl

Python Sample Usage
===================
::

	import pyeddystoneurl
	devices = pyeddystoneurl.discover(10)