from pyfiglet import Figlet
from tabulate import tabulate

def figlet():
    f = Figlet(font='small', width = 200)
    print(f.renderText('wiki py tool'))

def top():
    text_top = """
Usage:
    page- [Name of the Article]
    language- [Language of the article]
    download- [Filetype of the article, pdf/epub]
    email- [Email address to send to, otherwise do not enter or add email-none]

Example:
    page-Eiffel Tower | language-en | download-pdf  | email-name.last@gmail.com
    page-Tour Eiffel  | language-fr | download-epub | email-name.last@gmail.com"""
    
    table = [[text_top]]
    top = tabulate(table, tablefmt='grid')
    print(top)
