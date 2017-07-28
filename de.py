#!/usr/bin/python
import threading, urllib2, re, json

path = 'de.json'
db = dict()
counter = 0
times = 20
url = 'http://developerexcuses.com'
reg = '<a href=\"/\" rel=\"nofollow\" style=\"text-decoration: none; color: #333;\">(.+)</a>'

def read_url():
  global counter
  data = urllib2.urlopen(url).read()
  a = re.search(reg, data).group(0)
  s = a[71:-4]
  if s in results:
    print('Old: %s' % (s))
    return
  print('New: %s. %s' % (len(results), s))
  counter += 1
  results.add(s)

def fetch_parallel():
  threads = [threading.Thread(target=read_url) for _ in range(times)]
  for t in threads:
    t.start()
  for t in threads:
    t.join()

def main():
  global results
  with open(path,'r') as f:
    db = json.load(f)

  results = set(db['de'])
  fetch_parallel()

  print('%s/%s new, total %s' % (counter, times, len(results)))
  db['de'] = results = list(results)
  with open(path,'w') as f:
    json.dump(db, f, indent=2)

if __name__ == "__main__":
  main()