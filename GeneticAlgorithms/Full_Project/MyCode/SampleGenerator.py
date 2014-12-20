from collections import defaultdict, Counter

class Myscript:

   def __init__(self):
      self.rows = 0
      self.columns = 0
      self.area = 0
      self.notallowed = 0
      self.currentline = 0
      self.total = 0

   def render(self,filename):
        f = open(filename, "r")
        data = f.read().splitlines()
    # First line species the number and land use types
      #  print data[self.currentline]
        self.rows = int(data[self.currentline].split()[1]);
        self.currentline = self.currentline+1
        self.columns = int(data[self.currentline].split()[1]);
        self.currentline = self.currentline+3
      #  print self.rows
      #  print self.columns
        self.area = data[self.currentline].split()[1];
        self.currentline = self.currentline+1
        self.notallowed = data[self.currentline].split()[1];
        self.currentline = self.currentline+1
        self.total = self.rows*self.columns
        w =  open('gen','w')
        print >>w, '5 U R I C G'
        print >>w, self.total
        for counter in range(self.total):
            print >>w, counter,
            if counter%self.columns !=0:
                print >>w, counter-1,
            if counter%self.columns !=self.columns-1:
                print >>w, counter+1,
            if counter/self.rows !=0:
                print >>w, counter-self.columns,
            if counter/self.rows !=self.rows-1:
                print >>w, counter+self.columns,
            print >>w, ''


dataGen = Myscript()
dataGen.render('rasterex')
