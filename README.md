# wiki_py_tool

## Description of the tool

A suite of tools that allows easy management, conversion and sending of wikipedia articles, to email or kindle.
The main functionality is enabled using typer which is a great wrapper for click.
Typer really streamlined the whole process and the only problem I had with it was the lack of support for typehinting some return values.

Additional modules are:  
wikipedia, which is a pythonic wrapper for the wikimedia api and a great no headache solution for getting wikipedia objects.
yagmail a simple solution that is a great alternative to smtplib
and of course the converters which enable a lot of heavy lifting
which are: weasyprint, pypandoc and prince. There were many others and in the next iteration I am moving to the headless browser alternative.
Wikipedia as a community edited solution can sometimes be subject to different formating styles, hard to track errors and a plethora of character encodings.
Not to mention the greatest gripe of all which is the lack of certain media if it is not named as an absolute path.
Following the deprecation of wkhtmltopdf it is the most optimal solution as wkhtmltopdf would still be relevant had it support for more recent versions of WebKit.

I would like to offer my most sincere gratitude to the maintainers of WeasyPrint for helpimng me out and fixing a rather peculiar bug which made my outputs unusable.
Sadly it is was not a one stop solution to my problems but for others who want to print out invoices and various other media that they control it is a great solution.

I tried to reduce the dependency size requirements as much as I could and in the end that took me down a long and winding rabbit hole.
From eliminating headless browsers as an option since they weighed around hundreds of MB I ended up experimenting and downloading many GB of font configurations, Latex compilers, and GTK binaries. 
I violated one of the commandments of the Zen of Python "Simple is better than complex" and for that folly i was rightly punished. :D

##How to use
wiki_py_tool has several commands to help you find wikipedia information,   
convert those articles to your desired format and email the converted articles to your email or kindle.
Available commands: search, lang, page, convert, email, kindle

**search command:**  
```terminal
search "Name of the article"
```
The result will be a list of similar named articles.

**lang command:**
```terminal
lang "language"
```
Specifies the language that will be used for this session until you change it.
By deafult the language to seash articles is english.
Languages can be specified in two different ways: "en" or "English"
The capitalization does not matter but names must be correct.
The list of languages supported with their respective country codes is at:
https://en.wikipedia.org/wiki/ISO_639-3

**page command:**  
```terminal
page "Name of the article"
```
The page command will return a wikipedia object ready for further manipulation.
search command that was discussed previously helps narrow down the search.
Not to worry if you are in a hurry the page commands prints a nice overview into the terminal  
so you can verify that is the article you are looking for.
At the current state there exists a need cleaning up the article additionaly using BeautifulSoup and Tidy
but it will soon be updated.

**convert** command allows for the conversion of the article you have chosen.
```terminal
convert "pdf" or "epub" --choose one
```             
This command converts the wikipedia object to the desired format.

**email**
```terminal
email "your@email.com"
```
This allows you to send the article to your email address.
Important note before sending you need to enable sending from this client   
in your 2 factor authentication options.

**kindle**
```terminal
email "your@kindle.com"
```
So far this is just a convenience as kindle supplies an email address with every ereader.
For kobo and other readers the process is more complicated and it is best to use already established tools like
Calibre that allow options of Local network and establishing a Network server.
Again this is just for convenience.

The guide is published here:
https://www.amazon.com/sendtokindle/email

But in essence it is just a matter of finding your unique already supplied kindle address.

## Installing Dependencies

This project uses a number of Python libraries.   
You can install them using the requirements.txt file included in the project's root directory.  

Here's how:  
- Open a terminal window.  
- Navigate to the project's root directory.  
- Run the following command:

```terminal
pip install -r requirements.txt
```

This command tells pip (a package manager for Python) to install all the libraries listed in the requirements.txt file.
