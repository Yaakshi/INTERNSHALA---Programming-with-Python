'''Book class'''

class Book:

    ''' Book __init__ method()'''

    def __init__(self,title,author,pub,price,no_of_books):
        self.t=title
        self.au=author
        self.p=pub
        self.pr=price
        self.nob=no_of_books
    
    '''Book getter methods'''

    def get_title(self):
        return self.t
    def get_author(self):
        return self.au
    def get_pub(self):
        return self.p
    def get_price(self):
        return self.pr
    def get_no_of_books(self):
        return self.nob

    '''Book setter methods'''

    def set_title(self,title):
        self.t=title
    def set_author(self,author):
        self.au=author
    def set_pub(self,pub):
        self.p=pub
    def set_price(self,price):
        self.pr=price
    def set_no_of_books(self,no_of_books):
        self.nob=no_of_books

    '''Book royalty() method'''

    def royalty(self):
        self.royalty_amt=0
        if self.nob<=500:
            self.royalty_amt=self.pr*self.nob*0.1
        if self.nob>500 and self.nob<=1500:
            self.royalty_amt=0.1*500*self.pr+self.pr*0.125*(self.nob-500)
        if self.nob>1500:
            self.royalty_amt=0.1*500*self.pr+0.125*1000*self.pr+0.15*self.pr*(self.nob-1500)
            
        return self.royalty_amt

'''Ebook class'''

class Ebook(Book):

    '''Ebook __init__() method'''

    def __init__(self,title,author,pub,price,no_of_books,epub,pdf,mobile):
        super().__init__(title,author,pub,price,no_of_books)
        self.ep=epub
        self.pd=pdf
        self.mob=mobile

    '''Ebook getter methods'''

    def get_epub(self):
        return self.ep
    def get_pdf(self):
        return self.pd
    def get_mobile(self):
        return self.mob
    
    '''Ebook setter methods'''

    def set_epub(self,epub):
        self.ep=epub
    def set_pdf(self,pdf):
        self.pd=pdf
    def set_mobile(self,mobile):
        self.mob=mobile

    '''Ebook royalty() method'''

    def royalty(self):
        self.royalty_amt=0
        if self.nob<=500:
            self.royalty_amt=self.pr*self.nob*0.1
        if self.nob>500 and self.nob<=1500:
            self.royalty_amt=0.1*500*self.pr+self.pr*0.125*(self.nob-500)
        if self.nob>1500:
            self.royalty_amt=0.1*500*self.pr+0.125*1000*self.pr+0.15*self.pr*(self.nob-1500)


        '''Remove GST: 
        GST Amount = Original Cost - [Original Cost x {100/(100+GST%)}]
        Net Price = Original Cost - GST Amount'''

        self.gst=self.royalty_amt-(self.royalty_amt*(100/(100+0.12)))
        self.net=self.royalty_amt-self.gst
        
        return self.net

'''Main'''
'''Object b1 for Book class'''

b1=Book("Secret Asset","Stella Rimmington","Arrow Books",500,2000)
print("BOOK")
print("Title: ",b1.get_title())
print("Author: ",b1.get_author())
print("Publisher: ",b1.get_pub())
print("Price: ",b1.get_price())
print("Royalty: ",round(b1.royalty(),2))
print()

'''Object eb1 for Ebook class'''

eb1=Ebook("Secret Asset","Stella Rimmington","Arrow Books",500,2000,"Scholastic","SA_SC.pdf",1234567890)
print("EBOOK")
print("Title: ",eb1.get_title())
print("Author: ",eb1.get_author())
print("Publisher: ",eb1.get_pub())
print("Price: ",eb1.get_price())
print("E-publisher: ",eb1.get_epub())
print("PDF: ",eb1.get_pdf())
print("Mobile: ",eb1.get_mobile())
print("Royalty: ",round(eb1.royalty(),2))