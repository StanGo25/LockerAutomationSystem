import urllib2, urllib

user_name=#withheld for security reasons
user_pin=#withheld for security reasons

prodstat1=4
prodstat2=2

path='http://munro.humber.ca/~n01116269/db234.php?user_name='+user_name+'&user_pin='+user_pin  #the url you want to POST to
path2='http://munro.humber.ca/~n01116269/door.php?p_stat='+prodstat1+'&u_name='+user_name
path3='http://munro.humber.ca/~n01116269/lock.php?p_stat='+prodstat2+'&u_name='+user_name

req=urllib2.Request(path)
req2=urlib2.Request(path2)
req3=urlib2.Request(path3) 


req.add_header("Content-type", "application/x-www-form-urlencoded")
req2.add_header("Content-type", "application/x-www-form-urlencoded")
req3.add_header("Content-type", "application/x-www-form-urlencoded")

page=urllib2.urlopen(req).read()
page2=urllib2.urlopen(req2).read()
page3=urllib2.urlopen(req3).read()

print 'Product status has been updated'