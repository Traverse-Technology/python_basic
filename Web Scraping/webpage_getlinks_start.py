import sys
import re
import webpage_read

def print_links(pagecontent):
    """ find all hyperlinks on the webpage input and print """
    print('[*] print_links()')
    # regex to match on hyperlinks
    links = re.findall("<a.+?>.+?</a>", pagecontent) 
    # sort and print the links
    links.sort()
    print(f'[+] {len(links)} HyperLinks Found:')
    for link in links:
        print(link)


def main():
    pagecontent = webpage_read.wget('https://www.w3schools.com')
    # Get the links
    print(type(pagecontent))
    print_links(pagecontent)


if __name__ == '__main__':
    main()
