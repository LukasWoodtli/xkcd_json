#!/usr/bin/env python3

import urllib.request
import json
import os

THIS_FILES_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

newest_xkcd = 'http://xkcd.com/info.0.json'

record_file = os.path.join(THIS_FILES_DIRECTORY, 'read_xkcd.txt')

response = urllib.request.urlopen(newest_xkcd)
xkcd = response.read()

num_of_xkcds = json.loads(xkcd)['num']

with open(record_file, 'r') as f:
  lines = f.readlines()
  lines = lines[1:]
  lines = [i for i in lines if i != '\n']
  lines = [i.replace('\n','') for i in lines]
  num = len([i for i in lines if '-' not in i])
  lines = [i for i in lines if '-' in i]
  for line in lines:
    nums = line.split('-')
    assert len(nums) == 2
    num += (int(nums[1]) - int(nums[0]) + 1)
  
  still_to_read = num_of_xkcds - num
  print("Total xkcd comics: %i" % num_of_xkcds)
  print("Read already: %i" % num)
  print("Still to read: %i" % still_to_read)
  print("Percent read: %.2f" % (num*100/num_of_xkcds))
