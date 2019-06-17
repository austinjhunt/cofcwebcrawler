import requests
import sys
from multiprocessing.dummy import Pool
from halo import Halo



class GlobalSearcher: 
	def __init__(self,_string): 
		self.string = _string
		with open('finalurls.txt','r') as f: 
			self.start_urls = f.readlines()
		self.found_string_locations = []

	# args: string to search for, and url where html is found
	# return all instances of the input string. 
	def searchHTMLforstring(self, url): 
		url = url.strip('\n').strip('\r')
		if url.startswith('//'):
			url = url[2:]
		try:
			content = requests.get(url,timeout=.01).text
		except: 
			try:	
				use_https = url.replace('http','https')
				content = requests.get(use_https,timeout=1).text
			except:
				return
		if str(self.string) in str(content): # if the string is found anywhere in the html, write this location to the file. 
			writestring = self.string + " found at URL: " + url + "," + str(content.count(self.string)) + " times."
			print(writestring)
			self.found_string_locations.append(writestring)		
	def drive(self): 
		p = Pool(5)
		p.map(self.searchHTMLforstring,self.start_urls)
		
	def get_found_string_locations(self): 
		return list(set(self.found_string_locations))


def gen_filename(string): 
	invalids = [':','/','\\', '$','.',',','[',']','{','}','(',')','!','"',';','\'','*','?','<','>','|']
	return ''.join([el if el not in invalids else '_' for el in string])
	

if __name__ == "__main__": 
	spinner = Halo(text='Loading', spinner='dots')
	spinner.start()
	string = sys.argv[1]
	gs = GlobalSearcher(string)	
	gs.drive()
	fsl = gs.get_found_string_locations()
	# write search results to an appropriately named file based on query
	filename = "search_results_" + gen_filename(string) + ".txt"
	print("Writing results of search to file: " + filename)
	with open(filename,'w+') as f: 
		for line in fsl: 
			f.write(line + '\n')
	spinner.stop()
