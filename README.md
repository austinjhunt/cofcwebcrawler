#### allurls.txt:
##### an initial list of urls, passed to build\_urls\_list.py such that all hrefs/links can be collected 
#### finalurls.txt: 
##### the final collection of hrefs/links built by the build\_urls\_list.py, to be passed into the global search 
#### build\_url\_list.py:
##### script for using an initial url list (allurls.txt) to build/collect a full list of hrefs found on those urls, without duplicates
#### crawl.py:
##### a web crawler script, executed as 'python crawl.py \<some string\>' that writes to a uniquely named text file all of the urls containing your string, as well as the number of instances of that string on each of those urls

# Usage: 
#### Create a virtual environment using python 3.6
`virtualenv --python=python3.6 myvenv`

#### Activate it
`source myvenv/bin/activate`

#### Install requirements
`pip install -r requirements.txt`

#### Run the crawl script with your query. 
`python crawl.py blogs.cofc.edu/scs`


