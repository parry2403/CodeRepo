__author__ = 'Parry'

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


            mys = "myout/moptdata"  + ".txt"
            mfl = open(mys,"w")



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

            for line in datag:
                    line = line.split('\t')
                    pt = int(line[0])
                    ar = float(line[2])
                    tee = line[1] # landtype
                    temp_lt = olt2nlt[tee]
                    landType.append(temp_lt)
                     # indxMap : contains decision (change/nochange), and four preferred land types

                    indxMap[pt] = ((int((line[cNoChange]))+1)%2,line[E_LU])
                    areaMap[pt] = ar
                    myAreaMap[pt] = (tee,ar)
                    attractiveness[pt] = line[suitability]
                                        #print temp_lt
                    sumIndArea[temp_lt] += ar


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
                        mfl.write(str(neigh))
                        mfl.write("\t")
                        i=i+1

                mfl.write("\n")



converter()