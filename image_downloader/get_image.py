import os,urllib

url = raw_input("Enter url: ")
dir_ = raw_input("Enter directory: ")

if not os.path.isdir(dir_):
    os.mkdir(dir_)

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
        print "There was some problem fetching the file "+page
        return None

def get_image(page):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module finds the first url from the input page.
    where the src tag is found, is the starting of image url.
    from the double qoutes, it finds end of the image url.
    Finally return the url of image,and end point of the url.
    returns none and 0, if src is not found.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    start = page.find("src=")
    if start == -1:
        return None, 0
    start_url = page.find('"',start+1)
    end_url = page.find('"',start_url+1)
    url = page[start_url+1:end_url]
    return url,end_url

def extract_name(url):
    length = len(url)
    name = ""
    for ch in url[-1::-1]:
        if ch == "/":
            break
        name+=ch
    name = name[-1::-1]    
    return name    
    
def get_all_images(home,page,dir_):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module collects all urls from the input page.
    It calls get_image to get a url in the page.
    one by one collects urls and downloads the images using wget.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    os.chdir(dir_)
    while True:
        url,end = get_image(page)
        i=1
        if url:
            if url.endswith(".jpg") or url.endswith(".jpeg"):
                os.system(r'C:\"Program Files (x86)"\GnuWin32\bin\wget '+url)
##                if not url.startswith("http"):
##                    url=home+url[2:]
##                image = get_page(url)
##                if image:
##                    name = extract_name(url)
##                    files = open(dir_+"\\"+name, 'wb')
##                    files.write(image)
##                    files.close()
##                
            page = page[end:]
        else:
            break
                 
page = get_page(url)
get_all_images(url,page,dir_)
