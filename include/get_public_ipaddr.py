#!/usr/bin/env python
import re,urllib2,socket
class Get_public_ip:
  socket.setdefaulttimeout(5)
  def getip(self):
    try:
      myip = self.visit("http://whatismyip.akamai.com/")
    except:
      try:
        myip = self.visit("http://ifconfig.io/")
      except:
        myip = "0.0.0.0"
    return myip
  def visit(self,url):
    opener = urllib2.urlopen(url)
    if url == opener.geturl():
      str = opener.read()
    return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

if __name__ == "__main__":
  getmyip = Get_public_ip()
  print getmyip.getip()
