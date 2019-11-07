from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
from io import StringIO
import string
import pyttsx3
import time
engine = pyttsx3.init()
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as fh:
        # iterate over all pages of PDF document
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            # creating a resoure manager
            resource_manager = PDFResourceManager()
           
            # create a file handle
            fake_file_handle = io.StringIO()
           
            # creating a text converter object
            converter = TextConverter(
                                resource_manager,
                                fake_file_handle,
                                codec='utf-8',
                                laparams=LAParams()
                        )

            # creating a page interpreter
            page_interpreter = PDFPageInterpreter(
                                resource_manager,
                                converter
                            )


            # process current page
            page_interpreter.process_page(page)
           
            # extract text
            global text;
            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()

   

# calling above function and extracting text
for page in extract_text_from_pdf('testresume.pdf'):
    text += ' ' + page
#print(text)
import spacy
nlp = spacy.load('en_core_web_sm')

doc_2 = nlp(text)
def name_ext():
   
    for ent in doc_2.ents:
        if ent.label_ == "PERSON":
            name= '{}'.format(ent)

            engine.say("Hi:")
            #time.sleep(1)
            engine.say(name)
            engine.runAndWait()
            return name
            break
#name_ext()
