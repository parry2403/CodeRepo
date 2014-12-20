__author__ = 'Parry'
import shapefile


olt2nlt = {}
if True:
            olt2nlt["AIR"] = 1
            olt2nlt["CIV"] = 2
            olt2nlt["HIC"] = 3
            olt2nlt["LIC"] = olt2nlt["HCC"] = 4
            olt2nlt["LLRN"] = olt2nlt["ER"] = 5
            olt2nlt["MFRN"] = 6
            olt2nlt["MHP"] = 7
            olt2nlt["MRN"] = 8
            olt2nlt["MUN"] =  9
            olt2nlt["NCC"] = 10
            olt2nlt["POS"]= 11
            olt2nlt["RCR"]= 12
            olt2nlt["RL"] = 13
            olt2nlt["SCC"]= 14
            olt2nlt["SLRN"] = 15
            olt2nlt["SOC"] = 16
            olt2nlt["TC"] = 17
            olt2nlt["UC"] = 18
            olt2nlt["UN"] = 19
            olt2nlt["VC"] = olt2nlt["HRR"] = 20
            olt2nlt["WF"] = 21
            olt2nlt["MUC"] = 22
            olt2nlt["MC"] = 23
            olt2nlt["TOD"] = 24
            common =["HRR","HCC","ER"]
# Read in our existing shapefile
r = shapefile.Reader("myout/final.shp")

# Create a new shapefile in memory
w = shapefile.Writer()

# Copy over the existing fields
w.fields = list(r.fields)
#print r.records()

# Add our new field using the pyshp API
w.field("Orig", "C", "40")

# We'll create a counter in this example
# to give us sample data to add to the records
# so we know the field is working correctly.
i=0

# Loop through each record, add a column.  We'll
# insert our sample data but you could also just
# insert a blank string or NULL DATA number
# as a place holder
#f= open("out/sols0.txt","r")
#data = f.read().splitlines()
for rec in r.records():
 rec.append(olt2nlt[rec[4]])
 #i+=1
 # Add the modified record to the new shapefile
 w.records.append(rec)

# Copy over the geometry without any changes
w._shapes.extend(r.shapes())

# Save as a new shapefile (or write over the old one)
w.save("myout/final.shp")