import httplib, urllib
import zlib, time
import json
import urllib2

params = urllib.urlencode({'kca15-1-asian': 'kca15-jkt48', 
							'kca15-1-asian_l': 'ASIA'
						 })

headers = {
			"Host" : "kca-intl-funnel.mtvnservices.com",
			"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0", 
			"Accept" : "*/*",
			"Accept-Language" : "en-US,en;q=0.5",
			"Accept-Encoding" : "gzip, deflate",
			"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
			"Referer" : "http://kca.nick-asia.com/vote",
			"Origin" : "http://kca.nick-asia.com",
			"Connection" : "keep-alive",
			"Pragma" : "no-cache",
			"Cache-Control" : "no-cache"
			}

while True:
	try:
		conn = httplib.HTTPConnection("kca-intl-funnel.mtvnservices.com")
		conn.request("POST", "/api/v2/kca.mtvi.com/collections/kca2015-vote/entries.json", params, headers)
		response = conn.getresponse()
		conn.close

		data = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)
		result_json = json.loads(data, encoding='utf-8')
		rlink = result_json[0]['link']['href']
		if rlink:
			f = urllib2.urlopen(rlink)
			data = f.read()
			if data:
				result_json = json.loads(data, encoding='utf-8')
				status = result_json['collection']['entries']['entry']['createdDate']
				if status:
					print "vote jam : %s" % status
		time.sleep(5)
	except Exception as e:
		print str(e)
