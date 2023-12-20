#import pdfkit

#nb. wkhtmltopdf bin folder needs to be in the path,
#to be safe add it to system path and then restart terminal no reboot needed

#https://pypi.org/project/pdfkit/
config = pdfkit.configuration(wkhtmltopdf='path to executable in the bin folder')

try:
  config = pdfkit.configuration()
except OSError:
  print("wkhtmltopdf not present in PATH")

#very grateful for the help in debugging
#https://stackoverflow.com/a/42495690
#https://stackoverflow.com/a/75652164


elif arg == "pdf":
            
            #this was to decompose wikipedias html object or request output
            #to decompose its table of contents and replace it with whhtmltopdf outline option 
            #but it did not work
            #much of the parsing on articles does not work efficiently
            #possible reason spans, td, tr, p and a and div are overlapping or their padding is  
           
            with open('wiki_page.html', 'r', encoding="utf-8") as file:
                soup = BeautifulSoup(file, 'html.parser')
                toc = soup.find(id='vector-toc')
                if toc:
                    toc.decompose()

            #'soup' contains the HTML without the table of contents
            html = str(soup)
            
            with open('wiki_page.html', 'w', encoding="utf-8") as file:
                file.write(html)
            
            #refer to https://wkhtmltopdf.org/usage/wkhtmltopdf.txt for the explanation of options
            
            #does not seem to take effect
            toc = {
            "toc-header-text": f"{wiki_page.title}",
            }
            
            #very important to enable local-file-access, 
            #pdf rendering is not ideal but it is readable at a very tiny font
            #printing is not suggested
            
            #options are configurable but it is best to leave encoding as UTF-8
            #no-outline does not seem to have effect
            
            #https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
            options = {
            'enable-local-file-access': '',
            'page-size': 'A4',
            'margin-top': '0mm',
            'margin-right': '20mm',
            'margin-bottom': '0mm',
            'margin-left': '20mm',
            'encoding': "UTF-8",
            'no-outline': None
            }
            
            #nb. wiki_page is an object from the wikipedia library
            #usage to render from url
            pdfkit.from_url('url', f'{wiki_page.title}.pdf' ,options=options, configuration = config, options = options, toc=toc)
            #usage to render from file
            pdfkit.from_file('path to html', f'{wiki_page.title}.pdf' ,options=options, configuration = config, options = options, toc=toc)
  