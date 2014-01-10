#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import re
import datetime
from xml.dom import minidom
import random

def weekday(i):
	return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][i]

def yr(phenny,input):
	uri = 'http://www.yr.no/place/Norway/S%C3%B8r-Tr%C3%B8ndelag/Trondheim/Trondheim/varsel.xml'
	xmldoc = minidom.parse(urllib.urlopen(uri))

	if xmldoc:
		stringtosay = ""
		i = 0;
		for node in xmldoc.getElementsByTagName('tabular')[0].childNodes:
			if i==5:
				stringtosay = stringtosay + weekday(datetime.datetime.strptime(node.attributes["from"].value, "%Y-%m-%dT%H:%M:%S").weekday())+" - "
				stringtosay = stringtosay + node.childNodes[3].attributes["name"].value + " "
				stringtosay = stringtosay + node.childNodes[13].attributes["value"].value + u'°C | '
			i = i+1;
			if i > 7:
				i=0
		phenny.say(stringtosay[0:len(stringtosay)-3])

yr.commands = ['yr']
