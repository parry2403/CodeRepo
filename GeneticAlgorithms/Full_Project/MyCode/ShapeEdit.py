__author__ = 'Parry'
import shapefile



# Read in our existing shapefile
r = shapefile.Reader("myout/final.shp")

# Create a new shapefile in memory
w = shapefile.Writer()

# Copy over the existing fields
w.fields = list(r.fields)
fil=7
#for count in range(fil):
if True:
# Add our new field using the pyshp API
    w.field("rs5", "C", "40")

# We'll create a counter in this example
# to give us sample data to add to the records
# so we know the field is working correctly.
    i=0

# Loop through each record, add a column.  We'll
# insert our sample data but you could also just
# insert a blank string or NULL DATA number
# as a place holder
    f= open("nc/solsc58.txt","r")
    data = f.read().splitlines()
    for rec in r.records():
        rec.append(data[i].split()[1])
        i+=1
 # Add the modified record to the new shapefile
        w.records.append(rec)

# Copy over the geometry without any changes
w._shapes.extend(r.shapes())

# Save as a new shapefile (or write over the old one)
w.save("myout/final")