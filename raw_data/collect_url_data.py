# Author : Manishanker Talusani

# Python file to collect urls for FASHION from Guardian newspaper
#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import codecs

UTF8Writer = codecs.getwriter('utf8')

import urllib2
from goose import Goose
from bs4 import BeautifulSoup

section_dict = {}
g=Goose()

OUTPUTFILE="finance.txt"
OUTPUT_URLS="finance_urls.txt"

def get_urls(main_url):
    resp = urllib2.urlopen(main_url)
    html_doc = resp.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    sections = soup.find_all('section')
    with open(OUTPUT_URLS, 'a') as u:
        for section in sections:
            if (section.get('id')):
                urls = []
                temp = section.find_all('a')

                for x in temp:
                    if not x.get('href') in urls:
                        urls.append(x.get('href'))
                     	u.write(x.get('href') + "\n")
                        get_main_text(x.get('href'))

                section_dict[section.get('id')] = urls
                print "dict is : ", section_dict


def get_main_text(main_url):
    article = g.extract(url=main_url)
    with open(OUTPUTFILE, 'a') as ut:
        ut = UTF8Writer(ut)
        ut.write('\n###########################################################' + "\n")
        #ut.write("\n")
        ut.write(article.cleaned_text)


def main():
    for x in range(17):
        page_number = (x + 1)
        append_url = '?page=' + str(page_number)
        main_url = 'https://www.theguardian.com/money' + append_url
        get_urls(main_url)


if __name__ == '__main__':
    main()

