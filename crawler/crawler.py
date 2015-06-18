#!/usr/bin/env python
#coding:utf-8
import sys,mysql.connector

import urllib2
import lxml.html
from httpie import *
from xml_parser import *

con = mysql.connector.connect(
		host='localhost',
		db='c9',
		user='yosukeee0512',
		passwd='',
		buffered=True)
cur = con.cursor()

def get_rss_list():
	cur.execute('SELECT url,id FROM %s' % ('news_category') )
	res = cur.fetchall()
	return res
	
def get_tag_list():
	cur.execute('SELECT name,id FROM %s' % ('news_tag') )
	res = cur.fetchall()
	return res

def get_pool_list():
	cur.execute('SELECT url FROM %s' % ('movie_pool') )
	res = cur.fetchall()
	return res

def insert_items(items,tags):
	for item in items:
		try:
		    cur.execute('INSERT INTO %s (`title`, `url`, `description`, `pub_date`,`category_id`) VALUES("%s", "%s", "%s", "%s","%s")' % ('news_article',item['title'], item['url'] ,item['description'],item['pub_date'],item['category_id']))
		    con.commit()
		    for tag in tags:
		    	if tag[0] in item['title']:
		    		print tag[0]
		    		cur.execute('INSERT INTO %s (`article_id`, `tag_id`) VALUES("%s", "%s")' % ('news_article_tag',cur.lastrowid,tag[1]))
		except:
		    pass

def insert_tags(items):
	for item in items:
		print item
		try:
		    cur.execute('INSERT INTO %s (`name`) VALUES("%s")' % ('news_tag',item))
		    con.commit()
		except:
		    pass

def double_check(items,pool_items):
	for pool_item in pool_items[:]:
		for item in items[:]:
			if pool_item[0]==item['link']:
				items.remove(item)
				break
	return items

rss_list = get_rss_list()
tag_list = get_tag_list()



print rss_list
for rss in rss_list:
    items = get_items(rss)
    insert_items(items,tag_list)


#pool_items = get_pool_list()

#items = double_check(items,pool_items)


