import urllib.request
import io
def get_robots_txt(url):
  if url.endsWith('/'):
    path = url
  else
    path = url + '/'
  req = urllib.request.urlopen(path + "robots.txt", data=NONE)
  data = io.IOTextWrapper(req, encoding="utf-8")
  return data
