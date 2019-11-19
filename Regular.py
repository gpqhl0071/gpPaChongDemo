#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import re

text = '<a href="/mongodb/mongodb_overview.htm">MongoDB - Overview</a>'

print(re.search('\"(.+)\"', text).group())

print(re.search('(?<=\")(.+?)(?=\")', text).group())
