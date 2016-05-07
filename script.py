#!/usr/bin/python

import urllib2
from html2text import html2text

for line in html2text(urllib2.urlopen("https://www.chittendenhumane.org/Dogs").read()).split("\n"):
	if ""
	print line