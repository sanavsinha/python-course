class library:
    def __init__(self,title,author):
        
        self.title=title
        self.author=author
    def borrow(self):
        return True
    def isborrowed(self):

        return False

book1=library("tui t sutherland","wings of fire")
book2=library("makashi kishimoto","naruto")
book3=library("xyz","wings of fire")
