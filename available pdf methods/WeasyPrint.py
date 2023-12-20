from bs4 import BeautifulSoup, NavigableString #for cleaning the requests input if it is used
from weasyprint import HTML, CSS #better to import both, than later try to debug why the page rules aren't interpreted
import requests #it is almost always better to render directly from url, this is for debugging
from tidylib import Tidy, tidy_document #helps with common errors that are made when a lot of users eddit wikipedia

#A helpful resource
#https://stackoverflow.com/a/72796798

'''
if using Windows try this if you don't want to add to PATH
recommended that you do to save yourself the headache
option in Python 3.8 and newer
'''
#import os
#os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

#plain usage
HTML(f'{wiki_page.url}').write_pdf(f'{wiki_page.title}.pdf')

#if you decide to change css refer to 
# https://developer.mozilla.org/en-US/docs/Web/CSS/@page
css = CSS(string=' @page {size: ;}, body {width: ;}')
#wiki page is an object from the wikipedia library
#nb. it can be used as HTML(file)... or HTML(url)...
#url method is recommended to avoid getting all wikipedia links including edit
HTML(f'{wiki_page.url}').write_pdf(f'{wiki_page.title}.pdf', stylesheets=[css])

#Thanks to liZe for clarifying https://github.com/liZe
#important to note WeasyPrint renders as a page doing its best to immitate WebKit rules
#large tables and graphics will be cut off as it will not render the content as a browser beyond the size, no side scrolling
#either switch to landscape or try to fix the table padding and that of elements

