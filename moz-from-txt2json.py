#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import json

raw_mozs = []

with open('raw-mozs.txt', 'r') as raw_moz_file:
  raw_moz_data = raw_moz_file.read()

index_of_start_of_last_moz = 0

for m in re.finditer(r"(Monday|Tuesday|Wednesday|Thursday|Friday)", raw_moz_data):
  raw_mozs.append(raw_moz_data[index_of_start_of_last_moz:m.start()])
  index_of_start_of_last_moz = m.start()

mozs = []
for raw_moz in raw_mozs:
  images = re.finditer(r"!\[([^\]]+)\]\(([^\)]+)\)", raw_moz)
  links = re.finditer(r"[^!]\[([^\]]+)\]\(([^\)]+)\)", raw_moz)
  quotes = re.finditer(r'["“]+(.*)["”]+', raw_moz)
  explores = re.finditer(r"(explore|pro-tip|pro tip):\**(.*)", raw_moz, flags=re.IGNORECASE)
  print "===- start -==="
  print raw_moz
  print "--- parse ---"
  moz = {}
  for image in images:
    print "image: { url: " + image.group(2) + "; alt-text: " + image.group(1) + " }"
  for link in links:
    print "link: { url: " + link.group(2) + "; text: " + link.group(1) + " }"
  for quote in quotes:
    moz["quote"] = quote.group(0).replace("“","").replace("”","")
    print "quote: " + quote.group(0)
  for explore in explores:
    print explore.group(1) + ": " + explore.group(2)
  print "===- end -==="
  if "quote" in moz and moz["quote"]:
    print "Appending moz = " +moz["quote"]
    mozs.append(moz)

moz = { "mozs" : mozs }
print moz
print json.dumps(moz)
