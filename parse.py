"""
Utility
--------
This demo script show how to extract key-value pairs from a page with a
"predictable" layout, as it can be found in invoices and other formalized
documents.

In such cases, a text extraction based on "words" leads to results that
are both, simple and fast and avoid using regular expressions.

The example analyzes an invoice and extracts the date, invoice number, and
various amounts.

Because of the sort, correct values for each keyword will be found if the
value's boundary box bottom is not higher than that of the keyword.
So it could just as well be on the next line. The only condition is, that
no other text exists in between.

Please note that the code works unchanged also for other supported document
types, such as XPS or EPUB, etc.
"""

import pymupdf

doc = pymupdf.open("BloodBud/reports/sample_report.pdf")  # insert document here
page = doc[0]
words = page.get_text("words", sort=True)  

# expected information to extract from pdf
expected_words = ["haemoglobin", "red blood cell", "rbc", "packed cell volume",
                   "hematocrit", "mean cell volume", "mean cell hemoglobin", "mean cell hemoglobin concentration",
                   "rdw", "platelet", "neutrophils", "lymphocytes", "eosinophils", "white blood cell", "monocytes",
                     "basophils", "pcv", "mcv", "mch", "mchc", "wbc"]

def parse2():
    for i, word in enumerate(words):
        # information items will be found prefixed with their "key"
        text = word[4]
        if text.lower() in expected_words:
           parse(text, i) # might be a return rather than a print

def parse(text, index, x = words):
    if (x[index + 1][4].lower() == "count"):
        try:
            result = float(x[index + 2][4])
            print(text + " Count: " + x[index + 2][4])
        except:
            return
    else:
        try:
            result = float(x[index + 1][4])
            print(text + ": " + x[index + 1][4])
        except:
            return
parse2()