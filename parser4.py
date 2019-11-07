def recommend():
    import pyttsx3
    engine = pyttsx3.init()
    import pandas as pd
    import numpy as np
    import re
    import string
    x=string.punctuation
    y=x.replace('+','')
    y=y+' '

    import csv
    import re
    import spacy
    import sys
    import time
    from importlib import reload
    reload(sys)
    import pandas as pd
    #sys.setdefaultencoding('utf8')
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    #from cStringIO import StringIO
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
    import os
    import sys, getopt
    import numpy as np
    from bs4 import BeautifulSoup
    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2
    #import urllib2
    #from urllib2 import urlopen
    #Function converting pdf to string
    def convert(fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(fname,'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text
    #Function to extract names from the string using spacy
    #def extract_name(string):
    # r1 = unicode(string)
    # nlp = spacy.load('xx')
    #  doc = nlp(r1)
    #   for ent in doc.ents:
    #     if(ent.label_ == 'PER'):
        #        print(ent.text)
        #        break
    #Function to extract Phone Numbers from string using regular expressions
    #def extract_phone_numbers(string):
    #    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    #    phone_numbers = r.findall(string)
    #    return [re.sub(r'\D', '', number) for number in phone_numbers]
    #Function to extract Email address from a string using regular expressions
    #def extract_email_addresses(string):
    #    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    #    return r.findall(string)
    #Converting pdf to string
    resume_string = convert("testresume.pdf")
    resume_string1 = resume_string
    #Removing commas in the resume for an effecient check
    resume_string = resume_string.replace(',',' ')
    #Converting all the charachters in lower case
    resume_string = resume_string.lower()
    #Information Extraction Function
    def extract_information(string):
        string.replace (" ", "+")
        query = string
        soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/" + query), "html.parser")
        #creates soup and opens URL for Google. Begins search with site:wikipedia.com so only wikipedia
        #links show up. Uses html parser.
        '''for item in soup.find_all('div', attrs={'id' : "mw-content-text"}):
            print(item.find('p').get_text())
            print('\n')'''
    with open('techatt.csv', 'r') as f: 
        reader = csv.reader(f)
        your_listatt = list(reader)
    with open('techskill.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    with open('nontechnicalskills.csv', 'r') as f:
        reader = csv.reader(f)
        your_list1 = list(reader)
    #Sets are used as it has a a constant time for lookup hence the overall the time for the total code will not exceed O(n)
    s = set(your_list[0])
    s1 = your_list
    s2 = your_listatt
    skillindex = []
    skills = []
    skillsatt = []
    print('\n')
    #extract_name(resume_string1)
    #print('\n')
    #print('Phone Number is')
    #y = extract_phone_numbers(resume_string)
    #y1 = []
    #for i in range(len(y)):
    #    if(len(y[i])>9):
            #y1.append(y[i])
    #print(y1)
    #print('\n')
    #print('Email id is')
    #print(extract_email_addresses(resume_string))
    for word in resume_string.split(" "):
        if word in s:
            skills.append(word)
    skills1 = list(set(skills))
#    print('\n')
#    print("Following are his/her Technical Skills")
#    print('\n')
    np_a1 = np.array(your_list)
    for i in range(len(skills1)):
        item_index = np.where(np_a1==skills1[i])
        skillindex.append(item_index[1][0])

    nlen = len(skillindex)
    #for i in range(nlen):
        #print(skills1[i])
        #print(s2[0][skillindex[i]])
        #print('\n')
    final_list = [] 
    for i in skills: 
        if i not in final_list: 
            final_list.append(i) 


    final_list = [''.join(c.lower() for c in s if c not in y) for s in final_list]
    #print(final_list)

    df=pd.read_csv('Projectnames1.csv',engine='python')
    data=np.array(df)
    df=df.fillna(" ")
    lst=[]

    for i in range(1,df.shape[0]-1):
        a=''
        for j in df.iloc[i,1:]:
            #print(j)
            if(j!=chr(32)):
                a=a+','+j
        lst.append(a.split(','))
        #print(a)
    lst2=[0 for i in range(len(lst))]
    for i in range(len(lst)):
        lst2[i]=(lst[i][1:])

    #print(lst2)

    d=0
    for i in lst2:
        lst2[d]=[''.join(c.lower() for c in s if c not in y) for s in i]
        d+=1
#    print(lst2)


    count=[]
    for i in lst2:
        c=0
        for j in final_list:
            if j in i:
                c+=1
        count.append(c)
    idx=count.index(max(count))
  #  print(count)
    s=str(df.iloc[idx+1,0])
    engine.say("Try this Project:")
    time.sleep(1)
    engine.say(s)
    engine.runAndWait()
    return s
    
#recommend()
