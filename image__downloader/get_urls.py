'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''This script collects all the urls from input page.
Also go through each url and collects all urls from their recursively.
It takes input as a url. and returns a list of all the urls found.''

It imports:
  -urllib

It defines:
  -main
  -get_all_links
  -get_next_url
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''
'''Required modules'''
''''''''''''''''''''''''''
import urllib
            
def get_next_url(page):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module finds the first url from the input page.
    where the href tag is found, is the starting of url.
    from the double qoutes, it finds end of the url.
    Finally returns that url, and its end point.
    returns none and 0, if href is not found.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print "entered get_next"
    
    start_link = page.find('href=')                       #to find if any url exist.
    if start_link == -1:                                  #if url not found
        return None,0
    start_url_at = page.find('"',start_link+1)            #starting of the url string.
    url_end = page.find('"',start_url_at+1)               #end of the url string. 
    url = page[start_url_at+1:url_end]                    #the url.
    return url,url_end                                    #url, and its end point.

def get_all_links(page):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module collects all urls from the input page
    It calls get_next_target to get a url in the page.
    one by one collects urls and return a list of them.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print "entered get_all_links"
    urls = []
    while True:
        url,end_pos =  get_next_url(page)                 #collecting the url and the position on the page, where url ends.
        if url:                                           #if url was found.
            urls.append(url)                              #creating an entry in the list.
            page = page[end_pos:]                         #extracting the remaining part of the page after the end_pos.
        else:
            break
    return urls

def main(page):
    print "Entered get_urls"
    return get_all_links(page)                            #all the urls found on the page.
