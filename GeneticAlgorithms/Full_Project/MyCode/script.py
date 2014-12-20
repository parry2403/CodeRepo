from collections import defaultdict, Counter


def Myscript():
    print 'started'

    landtypes = {}
    invertedlandtypes = {}
    adj_List = {}
    indxMap = {}
    typeArea = {}
    roadDistance = {}
    attractiveness = {}
    b = {}

    compatibility = defaultdict(float)
    conversion = defaultdict(float)
    landUseAllowed = 3
    minA = {}  # Minimum area for each land type (1-25)
    maxA = {}  # Max area for each land type

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

        indxMap[k].append(currenttype)

        isallowed = int(allowedTypes[2])
        indxMap[k].append(isallowed)

        if (len(allowedTypes) > 2 ):
            for allowedType in range(landUseAllowed, len(allowedTypes)):
                j = landtypes[allowedTypes[allowedType]]
                indxMap[k].append(j)
    currentline = currentline + parcels
    print indxMap

    n = int(data[currentline]);
    currentline = currentline + 1

    # Land Use with min max areas and b
    for i in range(0, n):
        line = data[currentline + i]
        allowedTypes = line.split()

        currenttype = landtypes[allowedTypes[0]]
        typeArea[currenttype] = 0
        minA[currenttype] = allowedTypes[1]
        maxA[currenttype] = allowedTypes[2]
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

    currentline = currentline + parcels
    print typeArea

    parcels = int(data[currentline]);
    currentline = currentline + 1
    #Road Distance and Attractiveness
    for i in range(0, parcels):
        line = data[currentline + i]
        allowedTypes = line.split()
        pt = int(allowedTypes[0])
        roadDistance[pt] = int(allowedTypes[1])
        attractiveness[pt] = float(allowedTypes[2])

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


Myscript();