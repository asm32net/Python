import urllib
import urllib2
url = 'http://localhost/py-cgi-2016/hello-get.py'
values = {
	'first_name':'PASCAL',
	'last_name':'asm32'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)

response = urllib2.urlopen(req)

html = response.read()
