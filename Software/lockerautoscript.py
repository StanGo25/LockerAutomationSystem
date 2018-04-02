import urllib2, urllib
import time
import sys
import datetime
import re

user_name='Jeremy'
user_pin='1996'

prodstat1=4
prodstat2=2


while True: 
    print 'Checking product status'
    path='http://munro.humber.ca/~n01116269/display.php?u_name='+user_name
    
    req=urllib2.Request(path)
    req.add_header("Content-type", "application/x-www-form-urlencoded")

    page=urllib2.urlopen(req).read()

    notag = re.sub("<.*?>", " ", page)
    
    print notag
    
    time.sleep(5)
    

path2='http://munro.humber.ca/~n01116269/door.php?p_stat='+prodstat1+'&u_name='+user_name
path3='http://munro.humber.ca/~n01116269/lock.php?p_stat='+prodstat2+'&u_name='+user_name

req2=urlib2.Request(path2)
req3=urlib2.Request(path3) 

req2.add_header("Content-type", "application/x-www-form-urlencoded")
req3.add_header("Content-type", "application/x-www-form-urlencoded")

page2=urllib2.urlopen(req2).read()
page3=urllib2.urlopen(req3).read()

print 'Product status has been updated'