class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printmsg(self):
        print(f'Happy Birthday {self.fname} {self.lname}')