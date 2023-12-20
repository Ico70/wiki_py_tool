import typer # an alternative to import sys, argparse
import wikipedia #pip package for wikipedia, predecessor of wikipedia-api but with better documentation
import pypandoc #library that uses tex to convert documents, nb. pdf has problems due to wkhtmltopdf being deprecated
import yagmail #simpler alternative to smtplib
from bs4 import BeautifulSoup, NavigableString #for cleaning the requests input if it is used
from weasyprint import HTML, CSS #better to import both, than later try to debug why the page rules aren't interpreted
import requests #it is almost always better to render directly from url, this is for debugging
from tidylib import Tidy, tidy_document #helps with common errors that are made when a lot of users eddit wikipedia
import subprocess # nb. the easiest way with no dependencies is to install Prince to render pdf
from pdf_output import weasyprint, prince #pdf modules
import pycountry #the user does not need to type en or english to change the language, this module converts to a ISO code en
import enum # module that is needed for typer options to work
from typing import Optional


#initialize a typer object to later be used with decorator command 
app = typer.Typer()


# command that searches for articles resembling the input
@app.command()
def search(article: str):
    typer.echo(wikipedia.search(article))

# command that searches articles in that language. 
# Since the pages are in that language it is important to search
# for pages using that language.
@app.command()
def lang(language_abbreviation: str):
    typer.echo(wikipedia.set_lang(language_abbreviation))

# command that creates a wikipedia object for manipulation, cleaning up where needed
# dealing with encodings, some glyphs might be missing 
# since encoding to ascii fixes most of the problems in pdf output
# it is not usually noticable
@app.command()
def page(article_page: str):
    wiki_page = wikipedia.page(article_page)
    with open('active_file.txt', 'w', encoding='utf-8') as f:
        f.write(wiki_page.title)

    r = requests.get(f'{wiki_page.url}')
    print(r.encoding)

    content = r.content.decode('utf-8', 'ignore')
    content = content.encode("ascii", "ignore")
    content = content.decode()
    soup = BeautifulSoup(content, 'html.parser')
    
    # Now you can access the elements of the HTML
    with open('wiki_page.html', 'w', encoding='utf-8', errors='ignore') as f:
        f.write(soup.prettify())

    with open('wiki_page.html', 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
    # Tidy the document
    tidy_html, errors = tidy_document(html)

    with open('wiki_page.html', 'w', encoding='utf-8', errors='ignore') as f:
        f.write(tidy_html)

    return wiki_page.title
    
#command for converting the html file in case of epub
@app.command()
def convert(arg: str):
    with open('wiki_page.html', 'r', encoding='utf-8') as f:
        wiki_content = f.read()
    if wiki_content:
        with open('active_file.txt', 'r', encoding='utf-8') as f:
                current_title = f.read()
        wiki_page = wikipedia.page(current_title)
        if arg == "epub":
            output = pypandoc.convert_file(
                "wiki_page.html", "epub",format='html', outputfile=f"{wiki_page.title}.epub",
                extra_args=['--metadata', f'title="{wiki_page.title}.epub"']
            )
            assert output == ""
        elif arg == "pdf":
            #uncomment to print PDF with WeasyPrint
            weasyprint(wiki_page.html)
            #uncomment to print PDF with Prince
            #prince(wiki_page.html)
            
# https://realpython.com/python-send-email/#yagmail A large help in figuring out yagmail
@app.command()
def email(address):
    with open('active_file.txt', 'r', encoding='utf-8') as f:
                current_title = f.read()
    with open('wiki_page.html', 'r', encoding='utf-8') as f:
        wiki_content = f.read()

    receiver = "your@gmail.com"
    body = f"Your {wiki_content} article"
    filename = convert(current_title)

    yag = yagmail.SMTP("my@gmail.com")
    yag.send(
        to=receiver,
        subject="",
        contents=body,
        attachments=filename,
    )

# Find out your kindle adress https://www.amazon.com/sendtokindle/email
# this is called kindle and not an ereader since kindle is one of the rare companies 
# that gives you your own addres per the device purchased
# for now best bet for Kobo and others is Calibre. There are ways but it is mostly a hassle 

@app.command()
def kindle(addrs: str):
    with open('active_file.txt', 'r', encoding='utf-8') as f:
                current_title = f.read()
    with open('wiki_page.html', 'r', encoding='utf-8') as f:
        wiki_content = f.read()

    receiver = "your@gmail.com"
    body = f"Your {wiki_content} article"
    filename = convert(current_title)

    yag = yagmail.SMTP("my@gmail.com")
    yag.send(
        to=receiver,
        subject="",
        contents=body,
        attachments=filename,
    )


class Format(enum.Enum):
    pdf = "pdf"
    epub = "epub"

#the complete command to get and send a converted file with flags
@app.command()
def page_get(page: Optional[str] = typer.Option(None, "--page", help="Page to search for"),
         language: Optional[str] = typer.Option(None, "--language", help="Language to use"),
         convert: Optional[Format] = typer.Option(None, "--download", help="Download the article as EPUB or PDF"),
         email: Optional[str] = typer.Option(None, "--email", help="Email to send to")):
    lang = "en"
    if language:
        lang_code = pycountry.languages.get(name=language).alpha_2
        lang = wikipedia.set_lang(lang_code)
        print(lang)
    #command page at line 34
    if page:
        wiki_page = page(page)
    # convert is a command but the convert inside is an argument if it is Epub or PDF
    if convert:
        convert(convert)
        typer.echo("Downloading page as {convert}")
    if email:
        typer.echo(f"Sending email to: {email}")

if __name__ == "__main__":
    app()