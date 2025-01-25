import pymupdf

def search_phrase_in_pdf(pdf_path, phrase):
    doc = pymupdf.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text()
        if phrase in text:
            return True
    return False

pdf_path = "reports\sample_report2.pdf"
phrase = "COMPLETE BLOOD COUNT"

if search_phrase_in_pdf(pdf_path, phrase):
    print(f"The phrase '{phrase}' was found in the PDF.")
else:
    print(f"The phrase '{phrase}' was not found in the PDF.")