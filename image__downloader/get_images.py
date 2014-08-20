"""
Script is used to download images from webpages.
"""
import os, urllib, get_urls

url = raw_input("Enter the url: ")
dir_ = raw_input("Enter the directory, where you want to save: ")

if not os.path.isdir(dir_):                                             #creating directory specified by input
	os.mkdir(dir_)

def get_image_url(page):
    """
    Returns image urls found on web page. 
    """
    start = page.find("src=")
    if start == -1:
        return None,0
    url_start = page.find('"',start+1)
    url_end = page.find('"',url_start+1)
    url = page[url_start:url_end]
    return url,url_end

def get_images(home_url,page,path):
	"""
    Downloads images using image_urls found on page. 
    """
	while True:
            url,end = get_image_url(page)
            if url:
                if url.endswith(".jpg") or url.endswith(".jpeg"):
                    if not url.startswith("http"):
                        url = home_url+url[2:]
                    name = extract_name(url)
                    print name
                    urllib.urlretrieve(url,path+"/"+name)
                page = page[end:]
            else:
                break
	
def extract_name(url):
    """
    Extracts the name of the image form provided url.
    """
    name = ""
    for ch in url[-1::-1]:
        if ch == "/":
            break
        name+=ch
        
    return name[-1::-1]

def union(a,b):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module combines two input lists.
    Checks for each entry in one list, if that does not exist in second
    list; it appends it to the second list.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print "entered union"
    for e in b:
        if e not in a:
            a.append(e)
            
def get_page(page):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module calls urlopen to collect the content of the input
    page from web.
    then returns that content to calling function.
    If any network error occurs and page is not fetched, it provides
    the user with suitable message.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print "entered get_page"
    try:
        return urllib.urlopen(page).read()
    except:
        print "There was some problem fetching the file."
        return None

def main(home_url,dir_):

    crawled = []
    page = get_page(home_url)                                         #fetching content of page, so that, we can collect urls from page.
    if page:
		get_images(home_url,page,dir_)                                                  #downloading images from home_url
    if page:
		links = get_urls.main(page)                                        #getting all the links form the page.
		if links:
			for url in links:                                       #iterating over the links in the list of links.
				if url not in crawled:
					crawled.append(url)
					if not url.startswith("http"):
					    url = home_url+url                          #the url of the locally referenced page.
					
					page = get_page(url)
					get_images(home_url,page,dir_)                    		  #converting the page
					if page:                                          #if page was fetched.  
						union(links,get_urls.main(page))              #union all new links from the page to old list of urls.
		else:
			print "There were no links on "+url
    
            
if __name__ == "__main__":
    main(url,dir_)
