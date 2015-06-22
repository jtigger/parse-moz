#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re

raw_mozs = []

with open('raw-mozs.txt', 'r') as raw_moz_file:
  raw_moz_data = raw_moz_file.read()

index_of_start_of_last_moz = 0

for m in re.finditer(r"(Monday|Tuesday|Wednesday|Thursday|Friday)", raw_moz_data):
  raw_mozs.append(raw_moz_data[index_of_start_of_last_moz:m.start()])
  index_of_start_of_last_moz = m.start()

for moz in raw_mozs:
  images = re.finditer(r"!\[[^\]]+\]\([^\)]+\)", moz)
  links = re.finditer(r"[^!]\[[^\]]+\]\([^\)]+\)", moz)
  quotes = re.finditer(r'["“]+(.*)["”]+', moz)
  explores = re.finditer(r"(explore|pro-tip|pro tip):\**(.*)", moz, flags=re.IGNORECASE)
  print "===- start -==="
  for image in images:
    print "image: " + image.group(0)
  for link in links:
    print "link: " + link.group(0)
  for quote in quotes:
    print "quote: " + quote.group(0)
  for explore in explores:
    print explore.group(1) + ": " + explore.group(2)
  print "===- end -==="

