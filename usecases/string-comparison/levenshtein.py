import numpy as np

def levenshtein(seq1, seq2):
    sizeX = len(seq1) + 1
    sizeY = len(seq2) + 1
    matrix = np.zeros ((sizeX, sizeY))
    for x in xrange(sizeX):
        matrix [x,0] = x
    for y in xrange(sizeY):
        matrix [0,y] = y
    
    for x in xrange(1,sizeX):
        for y in xrange(1,sizeY):
            if seq1[x-1] == seq2[x-1]:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1],
                    matrix[x,y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    print (matrix)
    return (matrix[sizeX - 1,sizeY - 1])

pairs = [
	["test", "text"],
	["aa", "ab"],
	["family", "familiar"]
]

for source,target in pairs:
	print ("%s vs %s:" % (source, target))
	print (levenshtein(source, target))
	print (" ")
