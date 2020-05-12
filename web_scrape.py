# start_chrome ->input_date -> scroll_down -> find_cards_info -> save -> find_next (goto)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

def start_chrome():
	driver = webdriver.Chrome(executable_path='./chromedriver')
	driver.start_client()
	return driver
# weibo.com/?sxbg + start_t ...

def q(st,et):
	return f'?is_ori=1&is_text=1&key_word=&start_time={st}&end_time{et}&is_search=1&is_searchadv=1#_0'

def scroll_down():
	html_page = driver.find_element_by_tag_name('html')
	# <html>...</html>
	# FROM > input
	for i in range(15):
		print(i)
		html_page.send_keys(Keys.END)
		time.sleep(0.6)

def find_cards_info():
	content_sel = 'div.WB_feed_detail'
	cards       = driver.find_elements_by_css_selector(cards_sel)
	info_list   = []
	for card in cards:
		content_sel = 'div.WB_text.W_f14'
		time_sel    = 'div.WB_from.S_txt2'
		link_sel    = 'div.WB_from.S_txt2 > a:nth-child(1)'

		content     = card.find_element_by_css_selector(content_sel).text
		time        = card.find_element_by_css_selector(time_sel).text
		link        = card.find_element_by_css_selector(link_sel).get_attribute('href')

		info_list.append([content,time,link])
		#[[1,2,3],[4,5,6]...]
	return info_list

def find_next():
	next_sel  = 'a.page.next'
	next_page = driver.find_elements_by_css_selector(next_sel)
	if next_page:
		return next_page[0].get_attribute('href')

def save(info_list,name):
	full_path = './' + name + '.csv'
	if os.path.exists(full_path):
		with open(full_path, 'a') as f:
			writer = csv.writer(f)
			writer.writerows(info_list)
			print('Done')
	else:
		with open(full_path,'w+') as f:
			writer = csv.writer(f)
			writer.writerows(info_list)
			print('Done')



def run_crawler(base,duration):
	#2020-01-1~2020-01-05
	if not base.endswitch('feedtop')
		st, ed = duration.split('~')
		driver.get(base+q(st,et))
	else:
		driver.get(base)
	time.sleep(5)
	scroll_down()
	time.sleep(5)
	info_list = find_cards_info()
	save(info_list,duration)
	next_page = find_next()
	if next_page:
		run_crawler(next_page,duration)


base = 'https://weibo.com/talkoenglish'
driver = start_chrome()
input()
run_crawler(base, '2020-01-1~2020-01-05')

