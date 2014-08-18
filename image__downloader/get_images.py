"""
Script is used to download images from webpages.
"""
import os, urllib

url = raw_input("Enter the url: ")
dir_ = raw_input("Enter the directory, where you want to save: ")

if not os.path.isdir(dir_):
	os.system(r'sudo md '+dir_)
    #os.mkdir(dir_)
    
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
    page = get_page(home_url)                                               #converting the page into pdf.
    if page:
        while True:
            url,end = get_image_url(page)
            print url
            if url:
                if url.endswith(".jpg") or url.endswith(".jpeg"):
                    if not url.startswith("http"):
                        url = home_url+url[2:]
                    name = extract_name(url)
                    print name
                    urllib.urlretrieve(url,name)
                page = page[end:]
            else:
                break
            #links = get_urls(page)                                        #getting all the links form the page.
            
if __name__ == "__main__":
    main(url,dir_)
