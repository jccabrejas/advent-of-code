# prompt: https://adventofcode.com/2020/day/19

from collections import defaultdict
import numpy as np
from math import sqrt
import networkx as nx

# import re
import sys

def read_input(filename='input.txt'):
    with open(filename) as f:
        result = list()
        for line in f.readlines():
            result.append(line.rstrip())
        return result

if len(sys.argv) == 2:
    inputText = read_input(sys.argv[1])
else:
    inputText = read_input()

def read_Tile(i, inputText):
    tileName = int(inputText[i][-5:-1])
    sides = list()
    sides.append(inputText[i+1].replace('.','0').replace('#','1')) # top
    sides.append(inputText[i+10].replace('.','0').replace('#','1')) # bottom
    sides.append(''.join([inputText[i+c][0].replace('.','0').replace('#','1') for c in range(1,11)]))
    sides.append(''.join([inputText[i+c][-1].replace('.','0').replace('#','1') for c in range(1,11)]))
    
    edgeSignatures = list()
    for s in sides:
        edgeSignatures.append(int(s,2))
        edgeSignatures.append(int(''.join(reversed(s)),2))
    
    ImageContent = np.array([list(inputText[i+c]) for c in range(1,11)])

    edgeReverseTile = dict()
    for e in edgeSignatures:
        edgeReverseTile[e] = tileName

    return tileName, edgeSignatures, ImageContent, edgeReverseTile

    def vert_flip(imageContent):
        return np.fliplr(imageContent)
    
    def hor_flip(imageContent):
        return np.flipud(imageContent)
    
    def rot_right(imageContent):
        return np.rot90(imageContent, 3)
    
    def rot_left(imageContent):
        return np.rot90(imageContent)

def part_1():
    tiles = defaultdict(dict)
    for i, line in enumerate(inputText):
        if line == '':continue
        if 'Tile' in line:
            tileName, edgeSignatures, imageContent, edgeReverseTile = read_Tile(i, inputText)
            tiles[tileName]['edgeSigs'] = edgeSignatures
            tiles[tileName]['imageContent'] = imageContent
            # todo append edgeReverseTile to image dict

    tileNames = tiles.keys()

    result = 1
    corners = list()
    edges = list()

    for tileName, tileContent in tiles.items():
        adjIDs = list()
        for side in tileContent['edgeSigs']:
            adjIDs += [i for i in tileNames if (i != tileName) and side in tiles[i]['edgeSigs']]
        adjIDs = list(set(adjIDs))
        adjacentsNo = len(adjIDs)
        tiles[tileName]['adjIDs'] = list(set(adjIDs))

    
        if adjacentsNo == 2:
            result *= tileName
            corners.append(tileName)
            edges.append(tileName)
            print(tileName, adjacentsNo)
        elif adjacentsNo == 3: 
            edges.append(tileName)

    return result, corners, edges, tiles


# 20899048083289

def align_Tiles(aligned, toBeAligned):
    for i, j in enumerate(toBeAligned['edgeSigs']):
        if j in aligned['edgeSigs']:
            break
    
    col = aligned['edgeSigs'].index(j)
    row = toBeAligned['edgeSigs'].index(j)

    doNothing = [(2,0), (3,1), (0,2), (1,3), (6,4), (7,5), (4,6), (5,7)]
    UD = [(0,0), (1,1), (2,2), (3,3), (7,4), (6,5), (5,6), (4,7)]
    LR = [(3,0), (2,1), (1,2), (0,3), (4,4), (5,5), (6,6), (7,7)]
    R = [(6,0), (7,1), (5,2), (4,3), (0,4), (1,5), (2,6), (3,7)]
    L = [(4,0), (5,1), (6,2), (7,3), (3,4), (2,5), (1,6), (0,7)]
    UD_LR = [(1,0), (0,1), (3,2), (2,3), (5,4), (4,5), (7,6), (6,7)]
    L_LR = [(5,0), (4,1), (7,2), (6,3)]
    R_LR = [(7,0), (6,1), (4,2), (5,3)]
    R_UD = [(1,4), (0,5), (3,6), (2,7)]
    L_UD = [(2,4), (3,5), (0,6), (1,7)]

    if (row, col) in UD:
        toBeAligned['imageContent'] = np.flipud(toBeAligned['imageContent']) 
    elif (row, col) in LR:
        toBeAligned['imageContent'] = np.fliplr(toBeAligned['imageContent']) 
    elif (row, col) in R:
        toBeAligned['imageContent'] = np.rot90(toBeAligned['imageContent']) 
    elif (row, col) in L:
        toBeAligned['imageContent'] = np.rot90(toBeAligned['imageContent'],3) 
    elif (row, col) in UD_LR:
        toBeAligned['imageContent'] = np.flipud(toBeAligned['imageContent']) 
        toBeAligned['imageContent'] = np.fliplr(toBeAligned['imageContent']) 
    elif (row, col) in L_LR:
        toBeAligned['imageContent'] = np.rot90(toBeAligned['imageContent'],3) 
        toBeAligned['imageContent'] = np.fliplr(toBeAligned['imageContent'])
    elif (row, col) in R_LR:
        toBeAligned['imageContent'] = np.rot90(toBeAligned['imageContent']) 
        toBeAligned['imageContent'] = np.fliplr(toBeAligned['imageContent'])
    elif (row, col) in R_UD:
        toBeAligned['imageContent'] = np.rot90(toBeAligned['imageContent'])
        toBeAligned['imageContent'] = np.flipud(toBeAligned['imageContent']) 
    elif (row, col) in L_UD:
        toBeAligned['imageContent'] = np.rot90(toBeAligned['imageContent'],3)
        toBeAligned['imageContent'] = np.flipud(toBeAligned['imageContent'])

    # recalculate edgeSigs
    toBeAligned['edgeSigs'] = list()
    sides = list()
    sides.append(''.join(toBeAligned['imageContent'][0,:]).replace('.','0').replace('#','1'))
    sides.append(''.join(toBeAligned['imageContent'][-1,:]).replace('.','0').replace('#','1'))
    sides.append(''.join(toBeAligned['imageContent'][:,0]).replace('.','0').replace('#','1'))
    sides.append(''.join(toBeAligned['imageContent'][:,-1]).replace('.','0').replace('#','1'))

    for s in sides:
        toBeAligned['edgeSigs'].append(int(s,2))
        toBeAligned['edgeSigs'].append(int(''.join(reversed(s)),2))

    # print(row, col)
    return toBeAligned, row, col

def part_2() -> int:
    _, corners, edges, tiles = part_1()
    
    size = len(tiles)
    length = int(sqrt(size))
    image = np.zeros(size).reshape(length, length)

    G = nx.Graph()
    for tileName in tiles.keys():
        G.add_node(tileName)
        for t in tiles[tileName]['adjIDs']:
            G.add_edge(tileName, t)

    edgeSequence = list()
    edgeSequence.append(corners[0])
    
    startEdges = edges.copy()
    startEdges.remove(corners[0])

    while len(startEdges) > 0:
        for e in startEdges:
            if edgeSequence[-1] in tiles[e]['adjIDs']:
                edgeSequence.append(e)
                break
        startEdges.remove(e)

    print(edgeSequence)
  
    corners = edgeSequence[0::length-1]
    print(corners)

    result = list()

    A = nx.shortest_path(G, corners[0], corners[1])
    B = nx.shortest_path(G, corners[3], corners[2])
    C = nx.shortest_path(G, corners[0], corners[3])
    D = nx.shortest_path(G, corners[1], corners[2])

    result.append(A)

    orientation = list()

    aligned = tiles[A[0]]
    print(A[0])
    for t in A[1:]:
        toBeAligned = tiles[t]
        aligned, row, col = align_Tiles(aligned, toBeAligned)
        print(t)
        tiles[t] = aligned
    if col in [0,1]: orientation.append('Up')
    elif col in [2, 3]: orientation.append('Down')
    elif col in [4, 5]: orientation.append('Left')
    elif col in [6, 7]: orientation.append('Right')

    aligned = tiles[C[0]]
    print(C[0])
    for t in C[1:]:
        toBeAligned = tiles[t]
        aligned, row, col = align_Tiles(aligned, toBeAligned)
        print(t)
        tiles[t] = aligned

    
    if col in [0,1]: orientation.append('Up')
    elif col in [2, 3]: orientation.append('Down')
    elif col in [4, 5]: orientation.append('Left')
    elif col in [6, 7]: orientation.append('Right')

    aligned = tiles[A[-1]]
    print(A[-1])
    for t in D[1:]:
        
        toBeAligned = tiles[t]
        aligned, row, col = align_Tiles(aligned, toBeAligned)
        print(t)
        tiles[t] = aligned

    aligned = tiles[C[-1]]
    print(C[-1])
    for t in B[1:]:
        
        toBeAligned = tiles[t]
        aligned, row, col = align_Tiles(aligned, toBeAligned)
        print(t)
        tiles[t] = aligned

    for i in range(1,len(C)):
        E = nx.shortest_path(G, C[i], D[i])
        result.append(E)
        aligned = tiles[C[i]]
        print(C[i])
        for t in E[1:]:
            
            toBeAligned = tiles[t]
            aligned, row, col = align_Tiles(aligned, toBeAligned)
            print(t)
            tiles[t] = aligned

    print(orientation)

    np.array(result)
    
    if orientation == ['Right', 'Down']:
        pass
    elif orientation == ['Right', 'Up']:
        result = np.flipud(result)
    elif orientation == ['Left', 'Down']:
        result = np.fliplr(result)
    elif orientation == ['Left', 'Up']:
        result = np.fliplr(result)
        result = np.flipud(result)
    elif orientation == ['Up', 'Left']:
        result = np.rot90(result,3)
        result = np.fliplr(result)
    elif orientation == ['Up', 'Right']:
        result = np.rot90(result,3)
    elif orientation == ['Down', 'Right']:
        result = np.rot90(result)
        result = np.fliplr(result)
    elif orientation == ['Down', 'Left']:
        result = np.rot90(result)

    
    [print(r) for r in result]

    row, col = result.shape

    stitched = np.array(list(8*8*row*col*'_')).reshape(8*row,8*col)
    for i in range(row):
        for j in range(col):
            stitched[8*i:8*i+8,8*j:8*j+8] = tiles[result[i,j]]['imageContent'][1:-1,1:-1]

    print(stitched)
    # =====================================
    row, col = stitched.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[stitched[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()

    d = {'.': False, '#': 0, ' ': 1}
    nessy = [list('                  # '), list('#    ##    ##    ###'), list(' #  #  #  #  #  #   ')]
    nessy = np.array([d[nessy[i][j]] for i in range(3) for j in range(20)]).reshape(3,20).tolist()

    import numpy.ma as ma

    # =====================================
    counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)]).reshape(3,20)
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
    print('Normal', counter)
    
    # =====================================
    temp2 = np.flipud(stitched)
    row, col = temp2.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[temp2[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()
    # counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)])
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
    print('FlipUD', counter)

    # =====================================
    temp2 = np.fliplr(stitched)
    row, col = temp2.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[temp2[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()
    # counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)])
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
    print('FlipLR', counter)

    # =====================================
    temp2 = np.rot90(stitched)
    row, col = temp2.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[temp2[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()
    # counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)])
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
                print(i,j)
    print('Rot90', counter)

    # =====================================
    temp2 = np.rot90(stitched,2)
    row, col = temp2.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[temp2[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()
    # counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)])
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
    print('Rot90*2', counter)

    # =====================================
    temp2 = np.rot90(stitched,3)
    row, col = temp2.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[temp2[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()
    # counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)])
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
    print('Rot90*3', counter)

    # =====================================
    temp2 = np.fliplr(stitched)
    temp2 = np.rot90(temp2)
    row, col = temp2.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[temp2[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()
    # counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)])
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
                print(i,j)
    print('LR + Rot90', counter)

    # =====================================
    temp2 = np.rot90(stitched)
    temp2 = np.fliplr(temp2)
    row, col = temp2.shape

    d = {'.': 0, '#': 1}
    temp = np.array([d[temp2[i][j]] for i in range(row) for j in range(col)]).reshape(row,col).tolist()
    # counter = 0
    for i in range(row-3):
        for j in range(col-20):
            window = np.array([temp[k][l] for k in range(i,i+3) for l in range(j,j+20)])
            x = ma.array(window, mask = nessy)
            if sum(x[~x.mask]) == 15:
                counter += 1
    print('Rot90 + LR', counter)

    return sum(sum(np.array(temp))) - 15*counter

    # numpy mask
    # run window around stitched image
    # flip ud
    # flip lr
    # rotate right
    # rotate left



print('\n================\nPart 1: ', part_1()[0:2] )
print('\n================\nPart 2: ', part_2())

# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171

