import requests
from multiprocessing import Pool
from multiprocessing.dummy import Pool as DPool
from bs4 import BeautifulSoup
import re

class URLFinder: 
	def __init__(self,allurlsarg=[]): 
		self.allurls = allurlsarg
		with open('allurls.txt','r') as f: 
			self.start_urls = f.readlines()
		
	# for each url, get all the hrefs on that page and append to list. 
	def getHrefsFromURL(self, url): 
		try: 
			html = requests.get(url,timeout=1).text
		except:
			try:
				html = requests.get(url.replace('http://','https://'),timeout=1).text
			except: 
				# print("Failed to connect to",url)
				return
		# print("Successfully connected to",url)
		soup = BeautifulSoup(html,'html.parser')
		urls_to_add = [self.joinbaseurl(url,u.get('href')) for u in soup.findAll('a')]
		self.allurls += urls_to_add
		# print(len(self.allurls))

	def drive(self): 
		p = DPool(8)
		# if first call then self.allurls will be empty, use start_urls
		if len(self.allurls) == 0: 
			p.map(self.getHrefsFromURL,self.start_urls)
		else: # use the allurls argument passed in to the constructor
			p.map(self.getHrefsFromURL, self.allurls)
	
	def joinbaseurl(self,u1,u2): 
		if u1 is not None and u2 is not None and u1 != '' and u2 != '':
			if 'http' not in u2: 
				u1 = u1.strip('\n')
				u2 = u2.strip('\n')

				if u1[-1] == '/': 
					u1 = u1[:-1]
				if u2[0] == '/':
					u2 = u2[1:]
				res = u1 + '/' + u2
				# print("Joined",u1,"and",u2,"into",res)
			else: 
				return u2
			
		else:
			return ''
	

	def getallurls(self):
		def cond(el):
			if el is not None:
				return el != '' and 'http' in el
			else: 
				return False
		return list(set([el for el in self.allurls if cond(el)]))

uf = URLFinder()
uf.drive()
ufurls =  uf.getallurls() 
print("First url finder complete.")

print(str(len(ufurls)) + " urls in total to search.")

print("Writing urls to file: allurls2.txt")
with open('allurls2.txt','w+') as f: 
	for url in ufurls: 
		f.write(url + '\n')
