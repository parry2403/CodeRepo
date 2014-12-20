from random import Random
from time import time
import inspyred
import copy
from inspyred import ec
from inspyred.ec import emo
from inspyred.ec import selectors
from inspyred.ec import variators
from inspyred import swarm
import itertools
import math
import random
from collections import defaultdict, Counter
from math import log
class Benchmark(object):
        
        def __init__(self, dimensions, objectives=1):
                self.dimensions = dimensions
                self.objectives = objectives
                self.bounder = None
                self.maximize = False
                
        def __str__(self):
                if self.objectives > 1:
                        return '{0} ({1} dimensions, {2} objectives)'.format(self.__class__.__name__, self.dimensions, self.objectives)
                else:
                        return '{0} ({1} dimensions)'.format(self.__class__.__name__, self.dimensions)
                
        def __repr__(self):
                return self.__class__.__name__
        
        def generator(self, random, args):
                """The generator function for the benchmark problem."""
                raise NotImplementedError
                
        def evaluator(self, candidates, args):
                """The evaluator function for the benchmark problem."""
                raise NotImplementedError
                
        def __call__(self, *args, **kwargs):
                candidate = [a for a in args]
                fit = self.evaluator([candidate], kwargs)
                return fit[0]

class NSGA2MOSO(Benchmark):





        def __init__(self, dimensions=43278):

                Raster =True
                landtypes = {}
                invertedlandtypes = {}
                adj_List = {}
                indxMap = {}
                typeArea = defaultdict(float)
                roadDistance = {}
                attractiveness = {}
                devDistance = {}
                b = {}
                areaMap = {}
                compatibility = defaultdict(float)
                conversion = defaultdict(float)
                landUseAllowed = 3
                minA = defaultdict(float)   # Minimum area for each land type (1-25)
                maxA = defaultdict(float)   # Max area for each land type
                currentTypes =[]
                currentline = 0

                f = open("sample", "r")
                data = f.read().splitlines()
                # First line species the number and land use types
                l = data[currentline].split();
                currentline = +1
                n = int(l[0])

                # Mapping for LandTypes
                for i in range(1, n + 1):
                    landtypes[l[i]] = i - 1
                    invertedlandtypes[i - 1] = l[i]
                print landtypes

                # number of parcels
                parcels = int(data[currentline]);
                currentline = currentline + 1

                # Adjacency List
                for i in range(0, parcels):
                    line = data[currentline + i]
                    neighbours = line.split()
                    k = int(neighbours[0])
                    adj_List[k] = []

                    if (len(neighbours) > 1):
                        for neighbour in range(1, len(neighbours)):
                            j = int(neighbours[neighbour])
                            adj_List[k].append(j)
                currentline = currentline + parcels
                print adj_List

                parcels = int(data[currentline]);
                currentline = currentline + 1

                # Land Use type Index
                for i in range(0, parcels):
                    line = data[currentline + i]
                    allowedTypes = line.split()
                    k = int(allowedTypes[0])
                    indxMap[k] = []

                    currenttype = landtypes[allowedTypes[1]]
                    currentTypes.append(currenttype)
                    indxMap[k].append(currenttype)

                    isallowed = int(allowedTypes[2])
                    indxMap[k].append(isallowed)

                    if (len(allowedTypes) > 2 ):
                        for allowedType in range(landUseAllowed, len(allowedTypes)):
                            j = landtypes[allowedTypes[allowedType]]
                            indxMap[k].append(j)
                currentline = currentline + parcels
                print currentTypes

                n = int(data[currentline]);
                currentline = currentline + 1

                # Land Use with min max areas and b
                for i in range(0, n):
                    line = data[currentline + i]
                    allowedTypes = line.split()

                    currenttype = landtypes[allowedTypes[0]]
                    typeArea[currenttype] = 0
                    minA[currenttype] = float(allowedTypes[1])
                    maxA[currenttype] = float(allowedTypes[2])
                    b[currenttype] = allowedTypes[2]
                currentline = currentline + n
                print minA
                print maxA

                parcels = int(data[currentline]);
                currentline = currentline + 1
                #Current Area
                for i in range(0, parcels):
                    line = data[currentline + i]
                    allowedTypes = line.split()
                    k = int(allowedTypes[0])
                    currenttype = landtypes[allowedTypes[1]]
                    typeArea[currenttype] = typeArea[currenttype] + int(allowedTypes[2])
                    areaMap[i] = int(allowedTypes[2])
                currentline = currentline + parcels
                print 'Area*****'
                print typeArea

                parcels = int(data[currentline]);
                currentline = currentline + 1
                #Road Distance and Attractiveness
                for i in range(0, parcels):
                    line = data[currentline + i]
                    allowedTypes = line.split()
                    pt = int(allowedTypes[0])
                    roadDistance[pt] = float(allowedTypes[1])
                    attractiveness[pt] = float(allowedTypes[2])
                    devDistance[pt] = float(allowedTypes[3])

                currentline = currentline + parcels
                #Compatibility Matrix
                for type1 in range(0, n):
                    line = data[currentline + type1]
                    compats = line.split();
                    for type2 in range(0, n):
                        compatibility[type1, type2] = compats[type2]

                currentline = currentline + n
                print compatibility
                #Conversion Matrix
                for type1 in range(0, n):
                    line = data[currentline + type1]
                    converts = line.split();
                    for type2 in range(0, n):
                        conversion[type1, type2] = converts[type2]

                currentline = currentline + n
                print conversion

               # currentline = currentline + 1
                print data[currentline]
                rasterFile = data[currentline].split()[2]
                print rasterFile
                rows=0
                columns=0
                rasterInputs = ''

                if data[currentline].split()[1] == 'Raster':
                    Raster =True
                    fr = open(rasterFile, "r")
                    datar = fr.read().splitlines()
                    rows =  int(datar[0].split()[1])
                    columns = int(datar[1].split()[1])
                    for lines in range(0, 6):
                         rasterInputs = rasterInputs + datar[lines] +"\n"
            #    print rasterInputs

                # A_LU=3
                # B_LU=4
                # C_LU=5
                # D_LU=6
                # E_LU=7
                # cSUIT=11
                # cNoChange=9
                # #id2idx = []
                # #idx2id = []
                # id2idx = {}
                # idx2id = {}
                # id2idx2 = {}
                # idx2id2 ={}
                # minA = {}
                # maxA = {}
                # suit=[]
                # olt = {}
                # for i in range(50000):
                #         suit.append(0)
                        #olt.append(0)

                # olt2nlt = {}
                # olt2nlt["AIR"] = 1
                # olt2nlt["CIV"] = 2
                # olt2nlt["HIC"] = 3
                # olt2nlt["LIC"] = olt2nlt["HCC"] = 4
                # olt2nlt["LLRN"] = olt2nlt["ER"] = 5
                # olt2nlt["MFRN"] = 6
                # olt2nlt["MHP"] = 7
                # olt2nlt["MRN"] = 8
                # olt2nlt["MUN"] =  9
                # olt2nlt["NCC"] = 10
                # olt2nlt["POS"]= 11
                # olt2nlt["RCR"]= 12
                # olt2nlt["RL"] = 13
                # olt2nlt["SCC"]= 14
                # olt2nlt["SLRN"] = 15
                # olt2nlt["SOC"] = 16
                # olt2nlt["TC"] = 17
                # olt2nlt["UC"] = 18
                # olt2nlt["UN"] = 19
                # olt2nlt["VC"] = olt2nlt["HRR"] = 20
                # olt2nlt["WF"] = 21
                # olt2nlt["MUC"] = 22
                # olt2nlt["MC"] = 23
                # olt2nlt["TOD"] = 24


                #Loading adj list for each cell
                # f= open("Adj_List_Final.gal","r")
                # data = f.read().splitlines()[1:]
                # adj_List = {}
                # for line in data:
                #         l = line.split(' ')
                #         if not l[0] is '':
                #                 k = int(l[0])
                #                 for i in range(len(l)):
                #                         #print i, k
                #                         j = int(l[i])
                #                         if (i==0):
                #                                 if not k in adj_List:
                #                                         adj_List[k]=[]
                #                         else:
                #                                 adj_List[k].append(j)
                #
                #                         if not j in adj_List:
                #                                 adj_List[j] =[]
                #                         if not k in adj_List[j]:
                #                                 adj_List[j].append(k)
                #print adj_List[20][1]
                

                #Loading areas, landtype for each cell
                # g=open("Refined_Swas_E_Updated2.csv","r")
                # dim=0
                # area = {}

                # for i in range(0,25):
                #         sumIndArea.append(0)
                # #print sumIndArea[21]
                # datag = g.readlines()[1:]
                # indxMap = {}
                # areaMap = {}
                # landType = []
                # for line in datag:
                #         line = line.split('\t')
                #         pt = int(line[0])
                #         ar = float(line[2]) #area
                #         tee = line[1] # landtype
                #         temp_lt = olt2nlt[tee]
                #         landType.append(temp_lt)
                #         # indxMap : contains decision (change/nochange), and four preferred land types
                #         indxMap[pt] = (int(line[cNoChange]),olt2nlt[line[B_LU]] ,olt2nlt[line[C_LU]],olt2nlt[line[D_LU]],olt2nlt[line[E_LU]])
                #         areaMap[pt] = ar
                #         #print temp_lt
                #         sumIndArea[temp_lt] += ar
                #print indxMap[20]

                sumIndArea = defaultdict(float)
                sumIndArea = typeArea
                landType = currentTypes
                copyLandType = copy.deepcopy(currentTypes)
                copySumIndArea =  copy.deepcopy(sumIndArea)



                area_sum=0.00
                for i in range(43278):
                        if not i in areaMap:
                                areaMap[i]=0
                for pt in areaMap.keys():
                        area_sum = area_sum + areaMap[pt]



                for i in range(5):
                    print 'Type********' ,i
                    print minA[i]
                    print maxA[i]
                    print sumIndArea[i]
                # Loading area targets
                # gh = open("SWAS_E_LU_PERCENT.csv","r")
                # datagh = gh.readlines()
                # for line in datagh:
                #         line = line.split('\t')
                #         #print line[0], line[1], line[2]
                #         minA[int(line[0])] = float(line[1]) * area_sum
                #         maxA[int(line[0])] = float(line[2]) * area_sum
                        #print line[0], minA[int(line[0])], maxA[int(line[0])], area_sum



                #43151
                self.dimensions = parcels
                self.objectives = 25
                Benchmark.__init__(self, parcels, 25) #numobj=3, dimensions=numcells=6
                #self.bounder = ec.Bounder([0] * self.dimensions, [3.0] * self.dimensions)
                self.bounder = ec.DiscreteBounder([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
                self.maximize = True

                #self.candidatesArea = {0:10,1:10,2:10,3:10,4:10,5:10}
                #self.total_area = 60
                #self.adjList = {0:[1,2],1:[0,2],2:[0,1,3],3:[2,4,5],4:[3,5],5:[3,4]}
                self.adjList = adj_List
                # self.candidatesArea = area
                self.landType = landType
                self.copyLandType = copyLandType
                self.areaMap = areaMap
                self.indxMap = indxMap
                self.sumIndArea = sumIndArea
                self.copySumIndArea = copySumIndArea
                self.total_area = area_sum
                self.minA = minA
                self.maxA = maxA
                self.attractiveness = attractiveness
                self.devDistance =devDistance
                self.conversion = conversion
                # self.suit = suit
                self.Raster = Raster
                self.rasterVal =rasterInputs
                self.rows = rows
                self.columns =columns
                # http://people.hofstra.edu/geotrans/eng/ch6en/conc6en/ch6c2en.html
                
                

        def generator(self, random, args):
                
            p = random.uniform(0,1)
         #   print "here"
            # 80% of the times allow the randomness to choose any of the 4 land types
            # 20% of the times consider the Base case E
         #   print p
            if (p < 0.2):

                X = copy.copy(self.landType)
              #  for i in range(len(self.landType)):
               #         if self.indxMap[i][1] == 1:
                #            xchoice = 4
                            #self.sumIndArea[self.landType[i]] = self.sumIndArea[self.landType[i]] - self.areaMap[i]
                 #           X[i] = self.indxMap[i][xchoice]

               # self.generator_count += 1
                # printing just to know whether job is executing for all the genrations, and changes happening
                print "1"
                return X

            else:
                X = copy.copy(self.landType)
             #   print len(self.landType)
                for i in range(len(self.landType)):
                        if self.indxMap[i][1] == 1:
                              #  l = random.uniform(0,1)
                         #   if (p < 0.1):
                              #  se
                            #    print "Index"
                          #      print self.indxMap[i]
                         #       print self.indxMap[i][2:]
                                xchoice = random.choice(self.indxMap[i][2:])
                                #self.sumIndArea[self.landType[i]] = self.sumIndArea[self.landType[i]] - self.areaMap[i]
                                self.indxMap[i][2:]
                                X[i] = xchoice
                                #self.sumIndArea[self.landType[i]] = self.sumIndArea[self.landType[i]] + self.areaMap[i]

                return X


        def attractive(self,c):
                f1 = 0.00 # for attractiveness
                p = range(len(c))
                for i in p:

                        #print "i",i, "idx2id:", self.idx2id[i],"c[i]", c[i]

                        if self.copyLandType[i] == 0 and c[i] >0:
                            f1 += (1-self.attractiveness[i])

                return f1

        def newDevelopment(self,c):
                f1 = 0.00 # for development
                p = range(len(c))
                for i in p:

                        #print "i",i, "idx2id:", self.idx2id[i],"c[i]", c[i]

                        if self.copyLandType[i] == 0 and c[i] >0:
                            f1 += self.devDistance

                return f1

        def conversion(self,c):
                f1 = 0.00 # for attractiveness
                p = range(len(c))
                for i in p:
                     f1 += self.conversion[self.copyLandType[i]][c[i]]

                return f1
                #print count
        def contiguity(self,c):
                f1 = 0.00 # for contiguity
                count = 0
                tempSumArea = []
                for i in range(0,25):
                        tempSumArea.append(0)
           #     print 'here1'
                sumIndArea = copy.deepcopy(self.sumIndArea)
                p = range(len(c))
                for i in p:

                        #print "i",i, "idx2id:", self.idx2id[i],"c[i]", c[i]
                        #Used for Limits -- To be moved in limits
                     #   print self.indxMap[i]
                        if self.indxMap[i][1] == 1:
                     #   if self.copyLandType[i] == 0 and c[i] >0:
                                sumIndArea[self.copyLandType[i]] = sumIndArea[self.copyLandType[i]] - self.areaMap[i]
                                sumIndArea[c[i]] = sumIndArea[c[i]] + self.areaMap[i]
                           #     print 'here'
                            #    if c[i] == self.indxMap[i][-1]:

                             #           count +=1

                             #   if count == 6570:
                              #          print "these are X:", sumIndArea


                        for val in self.adjList[i]:
                                if c[i] == c[val]:
                                        f1 += 0.01
                return f1,sumIndArea
                #print count
        def staticContiguity(self,c):
                f1 = 0.00 # for contiguity
                count = 0
                tempSumArea = []
                for i in range(0,25):
                        tempSumArea.append(0)
           #     print 'here1'
                sumIndArea = copy.deepcopy(self.sumIndArea)
                p = range(len(c))
                for i in p:

                        #print "i",i, "idx2id:", self.idx2id[i],"c[i]", c[i]
                        #Used for Limits -- To be moved in limits
                        if self.indxMap[i][1] == 1:
                     #   if self.copyLandType[i] == 0 and c[i] >0:
                                sumIndArea[self.copyLandType[i]] = sumIndArea[self.copyLandType[i]] - self.areaMap[i]
                                sumIndArea[c[i]] = sumIndArea[c[i]] + self.areaMap[i]
                           #     print 'here'
                                if c[i] == self.indxMap[i][-1]:

                                        count +=1

                                if count == 6570:
                                        print "these are X:", sumIndArea


                        for val in self.adjList[i]:
                                if c[i] == self.landType[val]:
                                        f1 += 0.01
                return f1,sumIndArea
        def limits(self,numTarget,sumIndArea):

             f=[]
             penalty = 1000
             scaler =10
             objDir=[]
             for i in range(0,numTarget):
                        f.append(0)
                        objDir.append(False)
             for ltidx in range(1,numTarget):

                        objDir[ltidx]=False
                      #  print "limit"
                     #   print sumIndArea[ltidx]
                        if (sumIndArea[ltidx] - self.minA[ltidx] < 0 ):
                                f[ltidx] = -1*(sumIndArea[ltidx] - self.minA[ltidx])*10 +penalty
                     #   else:
                      #      f[ltidx] = -(sumIndArea[ltidx] - self.minA[ltidx])
                        elif (sumIndArea[ltidx] - self.maxA[ltidx] > 0 ):
                                f[ltidx] = (sumIndArea[ltidx] - self.maxA[ltidx])*10 +penalty
                        else:
                             #f[ltidx] =0
                                f[ltidx] = -1 * min(math.fabs(sumIndArea[ltidx] - self.maxA[ltidx]),math.fabs(sumIndArea[ltidx] - self.minA[ltidx]))
#
#                          f[ltidx] = (self.maxA[ltidx] + self.minA[ltidx])/2 - abs(sumIndArea[ltidx
             return objDir, f

        def evaluatorSol(self, c):
                
                numTarget = len(self.minA)

                f=[]

                objDir=[]
             ##  print numTarget
                f1,sumIndArea = self.staticContiguity(c)
                objDir,f = self.limits(numTarget,sumIndArea)
                fa= self.attractive(c)

                self.landType = self.copyLandType
                self.sumIndArea = self.copySumIndArea
                #print f
                #flist = [-i for i in f]
                #flist.append(-f1)
           #     f[0]=f1

             #   objDir[0]=True
                f = [f1, sum(f[0:]),fa]
                objDir = [True, False,False]
           #     f = [f1,f[1][0],f[1][1],f[1][2],f[1][3],f[1][4],fa]
              #  f = [f1, sum(f[1:])]
             #   f = [f1, f[0],f[1],f[2],f[3],f[4],fa]
             #   objDir = [True, False,False,False,False,False,False]
                #f[1] = f2
                #flist.append(-f)
                #print f

                return emo.Pareto(f,objDir)
                
        def evaluator(self, candidates, args):
                fitness = []
                
                
                for c in candidates:
                        par = self.evaluatorSol(c)
                        fitness.append(par)

                
                #print "fintess are:", fitness  
                return fitness



def main(prng=None, display=True):
        if prng is None:
                prng = Random()
                prng.seed(time()) 

        #problem = inspyred.benchmarks.Kursawe(3)
        problem = NSGA2MOSO(10)
        ea = inspyred.ec.emo.NSGA2(prng)

        sol =problem.copyLandType
        mys = "myout/original1"  + ".txt"
        mfl = open(mys,"w")
        mfl.write(problem.rasterVal)
        for r in range(problem.rows):
            for c in range(problem.columns):
                    mfl.write(str(sol[10*r+c]))
                    mfl.write("\t")
            mfl.write("\n")

        @inspyred.ec.variators.mutator
        def My_gaussian_mutation(random, candidate, args):

            mut_rate = args.setdefault('mutation_rate', 0.1)
            mean = args.setdefault('gaussian_mean', 0.0)
            stdev = args.setdefault('gaussian_stdev', 1.0)
            bounder = args['_ec'].bounder
            mutant = copy.copy(candidate)
            for i, m in enumerate(mutant):
                if random.random() < mut_rate:
                 #   mutant[i] += random.gauss(mean, stdev)
                  #  print mutant[i]
                    xchoice = random.choice(problem.indxMap[i][2:])
                #                #self.sumIndArea[self.landType[i]] = self.sumIndArea[self.landType[i]] - self.areaMap[i]
                    mutant[i] = xchoice
          #  mutant = bounder(mutant, args)
            return mutant

        ea.variator = [inspyred.ec.variators.blend_crossover, My_gaussian_mutation]
                             #      inspyred.ec.variators.gaussian_mutation]
        ea.terminator = inspyred.ec.terminators.generation_termination
        
        X = problem.copyLandType
        print X
        X_total_area = 0
        #X_area =

        for i in range(len(problem.landType)):
              #  if problem.indxMap[i][0] == 1:
                        #self.sumIndArea[self.landType[i]] = self.sumIndArea[self.landType[i]] - self.areaMap[i]
                     #   X[i] = problem.indxMap[i][-1]
                X_total_area += problem.areaMap[i]


        print "X_area total is ",X_total_area
                        #self.sumIndArea[self.landType[i]] = self.sumIndArea[self.landType[i]] + self.areaMap[i]
                        
        
        fGOLD = problem.evaluatorSol(X)
        print "fGold/Original is", fGOLD


        sol =problem.copyLandType
        mys = "myout/original"  + ".txt"
        mfl = open(mys,"w")
        mfl.write(problem.rasterVal)
        for r in range(problem.rows):
            for c in range(problem.columns):
                    mfl.write(str(sol[10*r+c]))
                    mfl.write("\t")
            mfl.write("\n")



        final_pop = ea.evolve(generator=problem.generator, 
                                                  evaluator=problem.evaluator, 
                                                  pop_size=100,
                                                  maximize=problem.maximize,
                                                  bounder=problem.bounder,
                                                  max_generations=40)
        
        if display:
                final_arc = ea.archive
                print "final Solutions", len(final_arc)
                print('Best Solutions: \n')
                solutions =[]
                for f in range(len(final_arc)):
                        print("Finals")
                     #   print final_arc[f]
                   #     if final_arc[f].fitness[1]>0:
                   #         continue
                   #     else:
                        limit=0
                        for i in range(1,len(final_arc[f].fitness)-1):
                                if final_arc[f].fitness[i]>0:
                                    limit=1
                  #      if limit==0:
                        solutions.append(final_arc[f])
                   #     else:
                   #         continue
                        Sum = 0
                        for i in final_arc[f].fitness:
                                Sum += i
                        print Sum, final_arc[f].fitness

                        sol = final_arc[f].candidate
                        s = "out/rsol" + str(f) + ".txt"
                        mys = "report/multsol" + str(f) + ".txt"
                        #p = "out_best_sol/sol" + str(f) + ".txt"
                        fl = open(s,"w")
                        mfl = open(mys,"w")
                        if problem.Raster:
                            mfl.write(problem.rasterVal)
                        for r in range(problem.rows):
                            for c in range(problem.columns):
                                mfl.write(str(sol[10*r+c]))
                                mfl.write("\t")
                            mfl.write("\n")

                        for j in range(len(sol)):
                                fl.write(str(j))
                                fl.write("\t")
                                fl.write(str(sol[j]))
                                fl.write("\n")

                import pylab
                x = []
                y = []
                for f in solutions:
                        x.append(f.fitness[0])
                        temp=0
                        for i in range(1,len(f.fitness)):
                                temp += f.fitness[i]
                        
                       # y.append(temp)
                        y.append(f.fitness[len(f.fitness)-1])

                maxX =True
                maxY =True
                sorted_list = sorted([[x[i], y[i]] for i in range(len(x))], reverse=maxY)
                print sorted_list
                pareto_front = [sorted_list[0]]
                print pareto_front
                for pair in sorted_list[1:]:
                         if pair[1] <= pareto_front[-1][1]:
                                 pareto_front.append(pair)

            #    pylab.scatter(Xs,Ys)



                pylab.scatter(x, y, color='b')
                pf_X = [pair[0] for pair in pareto_front]
                pf_Y = [pair[1] for pair in pareto_front]
                pylab.plot(pf_X, pf_Y,color='g')
                pylab.xlabel("Continuity(Maximize)")
                pylab.ylabel("Attractiveness(Minimize)")
                x1 = fGOLD[0]
                x2 = 0
                for i in range(1,len(fGOLD)):
                        x2 += fGOLD[i]
                #print x1,x2
                #print "test"
                x2=fGOLD[len(fGOLD)-1]
             #   pylab.scatter(x1,x2,color='r')
                pylab.axvline(x1)
                pylab.savefig('{0} Example ({1}).pdf'.format(ea.__class__.__name__, 
                                                                                                         problem.__class__.__name__), 
                                          format='pdf')
                pylab.show()
        return ea
                
if __name__ == '__main__':
        main(display=True)    



