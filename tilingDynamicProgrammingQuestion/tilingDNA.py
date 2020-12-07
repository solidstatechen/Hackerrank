#Attack of the clones tiling dna question Dynamic Programming
import sys

T = []
I = []

def findTiling(i, t, k, tiles):
    
    if T[i] != 0: 
        #print("T[i]",T[i])
        return T[i]
    else:
        #reached front of string t
        if i == 0:
            print(t)
            T[i] = True
            return True
        else:
            #interate through tiles and check each to tile to see if it covers the last bit of t 
            for j in range(k):

                if ((len(tiles[j]) <= i) and t[:i].endswith(tiles[j]) and findTiling(i - len(tiles[j]), t, k, tiles)):
                    print(t[:i], tiles[j], j+1)
                    
                    I.append(j+1)

                    T[i] = True
                    return True
            
                
            return False




def getInput(file):
    #READING FROM INPUT FILE
    f = open(file, 'r')
    lines = f.readlines()
    #lines = sys.stdin.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
        

    t = lines[0]
    k = lines[1]
    tiles = lines[2:]
    
    return t, k, tiles

def main():
    #lines, n, m = getInput('tests/test2.in')
    t, k, tiles = getInput('sample0.txt')
    len_t = len(t) + 1
    len_k = int(k) + 1
    #print(t, k, tiles)
    

    #T = [[0] * len_k] * len_t
    global T
    for i in range(len_k):
        T.append(0)



    match_found = findTiling(len(t), t, int(k), tiles)

    if match_found:
        print('match found')
        print(T)

        for k in range(len(I)):
            print('tile indices',tiles[I[k] - 1],I[k])
            

        print(str(len(I)), " ".join(str(x) for x in I))

    else:
        print(0)

        '''
        for j in range(len(T)):
            if T[j] == True:
                print(j)
                print(tiles[j])
        '''

    
        



main()
