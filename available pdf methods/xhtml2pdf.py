# documentation https://xhtml2pdf.readthedocs.io/en/latest/usage.html

from xhtml2pdf import pisa
from bs4 import BeautifulSoup, NavigableString

#tried to clean up the file hoping it would have a prettier result
#result was not better
with open('wiki_page.html', 'r') as file:
    fix_html = file.read()
soup = BeautifulSoup(fi_html, 'lxml')

fixed_html = str(soup)

output_filename = "test.pdf"

# common usage continued below          
# open output file for writing (truncated binary)
result_file = open(output_filename, "w+b")

# convert HTML to PDF
pisa_status = pisa.CreatePDF(
        fixed_html,            # the HTML to convert
        dest=result_file)      # file handle to recieve result

# close output file
result_file.close()            # close output file

# return False on success and True on errors
print(pisa_status.err)
