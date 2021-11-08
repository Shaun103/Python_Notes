import PyPDF2
import re


# _________________________________________________________________
# Manipulating PDF Files 
# path = 
f = open('/Users/User/Desktop/Python/Data/Find_the_Phone_Number.pdf','rb')

# converting Find_the_Phone_Number.pdf
pdf_reader = PyPDF2.PdfFileReader(f)

# Getting number of pages in a PDF
print('\n')
numPages = pdf_reader.numPages
print("The number of pages for \'Find_the_Phone_Number\' are: ", numPages)
print('\n')

# Getting page one of a PDF
page_one = pdf_reader.getPage(0)
page_two = pdf_reader.getPage(1)

print(page_one) # may look like a bunch of code 

# Extracting text from page one
print('\nPage ONE:')
page_one_text = page_one.extractText()
print(page_one_text)

# Extracting text from page two
print('\nPage TWO:') 
page_two_text = page_two.extractText()
print(page_two_text)

# _________________________________________________________________
# finding a phone number pattern 
pattern = r'\d{3}.\d{3}.\d{4}'

for n in range(pdf_reader.numPages):
    page  = pdf_reader.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern,page_text)
    
    if match:
        print("Here is your match: ")
        print(match.group())