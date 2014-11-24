#!/usr/bin/python
import re
from lxml import etree,objectify


f = open('output/dell.jpg.xml','r')

contents = f.read()

contents = re.sub(r'<document(.*?)>',r'<document>',contents)

root = etree.fromstring(contents)
cardField = dict()

for elem in root.iter("field"):
	for value in elem[0].iter("value"):
		cardField[elem.get('type').lower()] = value.text

print cardField.items()
