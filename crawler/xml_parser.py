# -*- coding: utf-8 -*- 
import lxml.html
import re
import urllib2
import StringIO
from lxml import etree
from xml.etree import ElementTree
import datetime

rss1_ns = {'ns':"http://example.com/test",
"rss":"http://purl.org/rss/1.0/",
					"rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#",
					"dc":"http://purl.org/dc/elements/1.1/",
					"content":"http://purl.org/rss/1.0/modules/content/",
					"hatena":"http://www.hatena.ne.jp/info/xmlns#",
					"taxo":"http://purl.org/rss/1.0/modules/taxonomy/",
					"openSearch":"http://a9.com/-/spec/opensearchrss/1.0/"}

def strip_htmltag(text):
    p = re.compile(r"<[^>]*?>")
    return p.sub("", text)

def parse_i(i,category_id):
	
	title = i.findtext('./title')
	link = i.findtext('./link')
	description = strip_htmltag(i.findtext('./description'))
	date_tmp = i.findtext('./pubDate')
	date = datetime.datetime.strptime(date_tmp, "%a, %d %b %Y %H:%M:%S +0900")
	
	return {"title":unicode(title),
					"url":link,
					"pub_date":date,
					"description":unicode(description),
					"category_id":category_id}

def get_items(rss):

	items = []
	print rss[0],rss[1]
	req = urllib2.Request(rss[0],headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Connection': 'keep-alive'})

	
	src = StringIO.StringIO(urllib2.urlopen(req).read())
	xml = ElementTree.parse(src)
	

	if xml.findall('.//item'):
		item = xml.findall('.//item')
		for i in item:
			items.append(parse_i(i,rss[1]))

	return items

