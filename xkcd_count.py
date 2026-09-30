#!/usr/bin/env python3

import urllib.request
import json
import os
import random

THIS_FILES_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

newest_xkcd = 'http://xkcd.com/info.0.json'

record_file = os.path.join(THIS_FILES_DIRECTORY, 'read_xkcd.txt')

response = urllib.request.urlopen(newest_xkcd)
xkcd = response.read()

num_of_xkcds = json.loads(xkcd)['num']

read_xkcds = set()

with open(record_file, 'r') as f:
  lines = f.readlines()
  lines = lines[1:]
  lines = [i for i in lines if i != '\n']
  lines = [i.replace('\n','') for i in lines]
  for line in lines:
    if '-' in line:
      nums = line.split('-')
      assert len(nums) == 2
      for i in range(int(nums[0]), int(nums[1]) + 1):
        read_xkcds.add(i)
    else: 
      read_xkcds.add(int(line)) 
  
  num = len(read_xkcds)
  still_to_read = num_of_xkcds - num
  
  print("Total xkcd comics: %i" % num_of_xkcds)
  print("Read already: %i" % num)
  print("Still to read: %i" % still_to_read)
  print("Percent read: %.2f" % (num*100/num_of_xkcds))

  all_xkcds = set(range(1, num_of_xkcds + 1))
  not_read = all_xkcds - read_xkcds
  to_read = random.choice(list(not_read))
  print(f"Random xkcd to read: https://www.explainxkcd.com/wiki/index.php/{to_read}")
