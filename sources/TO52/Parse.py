# coding: utf8
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from TO52.Book import Book
from TO52.Page import Page
import time

__author__ = 'Iki'


class Parse:
    def __init__(self):
        print("Parsing")

    @staticmethod
    def run(path):
        print "Calling parser :%s" % path

        t0 = time.clock()

        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()
        book = Book()
        i = 0
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                      check_extractable=True):
            page_tmp = Page()
            begin_page = len(retstr.getvalue())
            interpreter.process_page(page)
            page_tmp.text = retstr.getvalue()[begin_page:-1]
            book.pages.append(page_tmp)
        fp.close()
        device.close()
        retstr.close()
        print "Parsing in:", time.clock() - t0
        return book
