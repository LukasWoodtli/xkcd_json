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


def find_oldest_to_read(s: set):
  # Source - https://stackoverflow.com/a/28178803
  # Posted by Antti Haapala, modified by community. See post 'Timeline' for change history
  # Retrieved 2026-10-06, License - CC BY-SA 3.0

  return next(i for i, e in enumerate(sorted(list(s)) + [None], 1) if i != e)


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
  print(f"Random xkcd to read: https://www.explainxkcd.com/wiki/index.php/{to_read}\n")
  oldest_to_read = find_oldest_to_read(read_xkcds)
  print(f"Oldest xkcd to read: https://www.explainxkcd.com/wiki/index.php/{oldest_to_read}")
