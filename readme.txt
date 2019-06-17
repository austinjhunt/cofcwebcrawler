allurls.txt: an initial list of urls, passed to build_urls_list.py such that all hrefs/links can be collected 
finalurls.txt: the final collection of hrefs/links built by the build_urls_list.py, to be passed into the global search 
build_url_list.py: script for using an initial url list (allurls.txt) to build/collect a full list of hrefs found on those urls, without duplicates
crawl.py: a web crawler script, executed as 'python crawl.py <some string>' that writes to a uniquely named text file all of the urls containing your string, as well as the number of instances of that string on each of those urls
