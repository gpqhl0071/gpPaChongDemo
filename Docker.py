#!/usr/bin/python
# -*- coding: utf-8 -*-

from splinter import Browser
import re

# open a browser
browser = Browser('chrome')
browser.visit('https://www.runoob.com/docker/docker-command-manual.html')

search_results_xpath = '//*[@id="content"]/ul[*]/li'  # simple, right?

search_results = browser.find_by_xpath(search_results_xpath)

scraped_data = []
for search_result in search_results:
    title = search_result.html  # trust me
    menuUrl = re.search('(?<=href=")(.+?)(?=\")', title)
    if menuUrl is not None:
        newTitle1 = re.search('(?<=\">)(.+?)(?=\<)', title)

        menuUrl = '(https://www.tutorialspoint.com/' + menuUrl.group() + ')'
        menuTitle = '['+newTitle1.group()+']'

        str = menuTitle + menuUrl

        print(str)
    # print(title)
