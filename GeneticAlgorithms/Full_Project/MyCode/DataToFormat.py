__author__ = 'Parry'

import csv
def converter():
            olt2nlt = {}
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


            mys = "myout/mdata"  + ".txt"
            mfl = open(mys,"w")
            mfl.write(str(24))
            mfl.write("\t")
            #mfl.write(problem.rasterVal)
            for node in olt2nlt:
                if node not in common:
                  mfl.write(str(node))
                  mfl.write("\t")
            mfl.write("\n")
            f= open("Adj_List_Final.gal","r")
            data = f.read().splitlines()[1:]
            adj_List = {}
            for line in data:
                l = line.split(' ')
                if not l[0] is '':
                        node = int(l[0])
                        if int(l[0]) not in adj_List:
                                      adj_List[node]=[]
                        for i in range(1,len(l)):
                              neighbours = int(l[i])
                              adj_List[node].append(neighbours)
                              if  neighbours not in adj_List:
                                    adj_List[neighbours] =[]
                              if node not in adj_List[neighbours]:
                                      adj_List[neighbours].append(node)

    #        mys = "myout/mdata"  + ".txt"
         #
         #    mfl = open(mys,"w")
            #mfl.write(problem.rasterVal)
            mfl.write(str(len(adj_List)))
            mfl.write("\n")
            for node in adj_List:
                mfl.write(str(node))
                mfl.write("\t")
                for neigh in adj_List.get(node):
                    mfl.write(str(neigh))
                    mfl.write("\t")
                mfl.write("\n")



            A_LU=3
            B_LU=4
            C_LU=5
            D_LU=6
            E_LU=7
            cSUIT=11
            cNoChange=9
            suitability = 10
            minA = {}
            maxA = {}
            suit=[]
            olt = {}
            indxMap = {}
            areaMap = {}
            landType = []
            myAreaMap = {}
            attractiveness = {}
            g=open("Main_data_file.csv","r")
            dim=0
            area = {}
            sumIndArea = []
            for i in range(0,25):
                sumIndArea.append(0)

            datag = g.readlines()[1:]
           # print len(datag)
            nchange={}
            for line in datag:
                    line = line.split('\t')
                    pt = int(line[0])
                    ar = float(line[2])
               #     tee = line[1] # landtype
                #    temp_lt = olt2nlt[tee]
                #    landType.append(temp_lt)
                     # indxMap : contains decision (change/nochange), and four preferred land types
                    nchange[pt]=line[cNoChange]
                #    indxMap[pt] = (tee,(int((line[cNoChange]))+1)%2,line[A_LU] ,line[B_LU] ,line[C_LU],line[D_LU],line[E_LU])
                    areaMap[pt] = ar
                 #   myAreaMap[pt] = (tee,ar)
                    attractiveness[pt] = line[suitability]
                                        #print temp_lt
                 #   sumIndArea[temp_lt] += ar
            p=0
            initial=1
            A=2
            B=3
            C=4
            D=5
            E=6
            f=open("SWAS_Parcels-ALL_Sheet1.csv","r")
       #     reader = csv.DictReader("SWAS_Parcels-ALL_Sheet1.csv", delimiter=',')
          #  print f.read()
            datag = f.readlines()[1:]
         #   print len(datag)
            mareas = []

         #   for i in range(2,7):
          #      testsum =[]
           #     for opo in range(0,25):
            #     testsum.append(0)
        #    for i in range(43278):
         #       indxMap[i]=None
            print len(datag)
            i=0
            for line in datag:
                        line =line.replace("\"","")
                        line = line.split('\n')[0].split(",")
                      #  print line
                     #   print pt
                        pt = int(line[0])
                   #     if i!=pt:
                    #        print i
                     #       i=pt
                     #   i=i+1

                   #     ar = float(line[2])
                        tee = line[1] # landtype
                        if tee in olt2nlt.keys():
                            temp_lt = olt2nlt[tee]
                        else:
                             tee = "WF"
                             temp_lt = olt2nlt["WF"]
                        landType.append(temp_lt)
                         # indxMap : contains decision (change/nochange), and four preferred land types

                        indxMap[pt] = (tee,(int((nchange[pt]))+1)%2,line[A] ,line[B] ,
                                       line[C],line[D],line[E])
                  #      areaMap[pt] = ar
                        myAreaMap[pt] = (tee,areaMap[pt])
                   #     attractiveness[pt] = line[suitability]
                                            #print temp_lt
                     #   print "here"
                        sumIndArea[temp_lt] += areaMap[pt]
              #  print sumIndArea
         #       mareas.append(testsum)
       #     print indxMap
            print len(indxMap)
            mini =[]
            maxi=[]
            ct=0

         #   print mareas
       #     for j in range(0,25):
        #        dum=[]
         #       for li in range(0,5):
          #          dum.append(mareas[li][j])
         #       print dum
           #     mini.append((min(dum),max(dum)))
           #     maxi.append())
        #    print maxi
           # print mini
    #        mys = "myout/mdata"  + ".txt"
         #   mfl = open(mys,"w")
            #mfl.write(problem.rasterVal)

            mfl.write(str(len(indxMap)))
            mfl.write("\n")
            for node in indxMap:
                mfl.write(str(node))
                mfl.write("\t")
                temp ={}
                indxMap.get(node)
                i=0
                for neigh in indxMap.get(node):
                    if i ==0:
                        mfl.write(str(neigh))
                        mfl.write("\t")
                        i=i+1
                    elif i == 1:
                        mfl.write(str(neigh))
                        mfl.write("\t")
                        i=i+1
                    else:
                    #     if temp.get(neigh) == None:
                            temp[neigh] = neigh
                            mfl.write(str(neigh))
                            mfl.write("\t")
                mfl.write("\n")

            area_sum=0.00
            for i in range(43278):
                    if not i in areaMap:
                            areaMap[i]=0
            for pt in areaMap.keys():
                 area_sum = area_sum + areaMap[pt]



                # Loading area targets
            gh = open("Targets_File.csv","r")
            datagh = gh.readlines()[1:]
            for line in datagh:
                line = line.split('\t')
                        #print line[0], line[1], line[2]
                if line[3].endswith("\n"):
                 #   print line[3].split("\n")[0]
                    line[3]=line[3].split("\n")[0]
                minA[line[3].strip()] = float(line[1]) * area_sum
                maxA[line[3].strip()] = float(line[2]) * area_sum
                print  line[3].strip() ,minA[line[3]]
                print  line[3].strip() ,maxA[line[3]]
                        #print line[0], minA[int(line[0])], maxA[int(line[0])], area_sum

     #       mys = "myout/mdata"  + ".txt"
           # mfl = open(mys,"w")
            #mfl.write(problem.rasterVal)
            mfl.write(str(len(minA)))
            mfl.write("\n")
            for node in minA:
                mfl.write(str(node))
                mfl.write("\t")
                mfl.write(str(minA[node]))
                mfl.write("\t")
                mfl.write(str(maxA[node]))
                mfl.write("\n")


    #        mys = "myout/mdata"  + ".txt"
       #     mfl = open(mys,"w")
            #mfl.write(problem.rasterVal)
            mfl.write(str(len(myAreaMap)))
            mfl.write("\n")
            for node in myAreaMap:
                mfl.write(str(node))
                mfl.write("\t")
                temp ={}
                myAreaMap.get(node)
                i=0
                for neigh in myAreaMap.get(node):
                    if i ==0:
                        mfl.write(str(neigh))
                        mfl.write("\t")
                        i=i+1
                    elif i == 1:
                        mfl.write(str(neigh))
                        mfl.write("\t")
                        i=i+1

                mfl.write("\n")

            mfl.write(str(len(attractiveness)))
            mfl.write("\n")
            for node in attractiveness.keys():
                mfl.write(str(node))
                mfl.write("\t")
                mfl.write(str(attractiveness.get(node)))


                mfl.write("\n")


converter()