import urllib.request
def wget(url):
    """ This is function which retrieve data from url """
    try:
        webpage = urllib.request.urlopen(url)
        page_contents = webpage.read().decode()
        return page_contents
    except Exception as ero:
        print(f"Error {ero}")
