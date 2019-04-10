#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='check_siae',
	version='0.1',
	description='Nagios Check for SIAE Microelettronica ALFOplus80HD',
	author='Peter Adam',
	author_email='info@cygnusnetworks.de',
	license='GPL',
	packages=['siae_snmp'],
	scripts=['check_siae'],
	install_requires=['configparser', 'nagiosplugin', 'pysnmp'])
