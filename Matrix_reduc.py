import numpy as np
import copy
import bisect 



def store_M(M): # efficient matrix storage for sparse matrizes 
    a = []      # Each column is stored as a list containing the indizes of the corresponding 1 entries
    for i in range(len(M)):
        temp = []
        for j in range(len(M)):
            if M[j][i] == 1:
                temp.append(j)
        a.append(temp)
    return a
              
def restore_M(M):
    a = np.zeros((len(M),len(M)),dtype = int)
    for i in range(len(M)):
        if M[i]== []:
            continue
        for j in M[i]:
            a[j][i] = 1
            
    return a
        
    
def randomtriangm(n): 
     return np.triu(np.random.randint(2,size=(n,n))) # creates random  (0/1) upper triangular matrix 
 
def addcolumns(a,b):
    return sorted(list(set(a).symmetric_difference(b)))


def symmDiff2(arr1,arr2):
    for x in arr1:
        if x in arr2:
            arr2.remove(x)
        else:
            arr2.append(x)
    return sorted(arr2)


def symmDiff(arr1, arr2): 
      
    # Traverse both arrays 
    # simultaneously. 
    n = len(arr1)
    m = len(arr2)
    symmetric_difference = []
    if n ==0:
        return arr2[:]
    if m == 0:
        return arr1[:]
    i = 0
    j = 0
    while (i < n and j < m): 
      
        # Print smaller element 
        # and move ahead in  
        # array with smaller  
        # element 
        if (arr1[i] == arr2[j]): 
            i+=1
            j+=1
          
        elif (arr2[j] < arr1[i]): 
            symmetric_difference.append(arr2[j]) 
            j+=1
        # If both elements 
        # same, move ahead 
        # in both arrays. 
        else: 
            symmetric_difference.append(arr1[i]) 
            i+=1
          
            
      

    return symmetric_difference






def red_alg(A):
    M = copy.deepcopy(A)
    lowone = {} ###dictionary that saves row index of lowest one as key, and corresponding column index with it
    
    for i in range(len(M)):
        
        while M[i] != [] and M[i][-1] in lowone:
            #M[i] = symmDiff(M[lowone[M[i][-1]]],M[i])
            M[i] = addcolumns(M[lowone[M[i][-1]]],M[i])
            
        if M[i] !=[]:
            lowone[M[i][-1]] = i
        
    return M

    
def red_alg_mod(A):
    M = copy.deepcopy(A)
    lowone = {} ###dictionary that saves row index of lowest one as key, and corresponding column index with it
    for i in range(len(M)):

        while M[i] != [] and M[i][-1] in lowone:
            if(len(M[lowone[M[i][-1]]])> len(M[i])):
                M[lowone[M[i][-1]]], M[i] = M[i], M[lowone[M[i][-1]]]  
            M[i] = symmDiff2(M[lowone[M[i][-1]]],M[i])
            #M[i] = addcolumns(M[lowone[M[i][-1]]],M[i])

        if M[i] !=[]:
            lowone[M[i][-1]] = i
            

    return M


def red_alg_count(A):
    bitaddition = 0
    twistaddition = []
    M = copy.deepcopy(A)
    lowone = {} ###dictionary that saves row index of lowest one as key, and corresponding column index with it
    
    for i in range(len(M)):
        
        temp = bitaddition
        while M[i] != [] and M[i][-1] in lowone:
            #M[i] = symmDiff(M[lowone[M[i][-1]]],M[i])
            bitaddition += len(M[lowone[M[i][-1]]])
            
            M[i] = addcolumns(M[lowone[M[i][-1]]],M[i])
            
            
        twistaddition.append(bitaddition -temp)
        if M[i] !=[]:
            lowone[M[i][-1]] = i
            twistaddition[M[i][-1]] = 0
    return [bitaddition,sum(twistaddition)]



def red_alg_mod_count(A,Twist = False):
    bitaddition = 0
    trick_cost = 0
    trick = 0
    max_trick = 0
    M = copy.deepcopy(A)
    lowone = {} ###dictionary that saves row index of lowest one as key, and corresponding column index with it
    for i in range(len(M)):

       
        while M[i] != [] and M[i][-1] in lowone:
            bitaddition += len(M[lowone[M[i][-1]]])
            if(len(M[lowone[M[i][-1]]])> len(M[i])):
                trick +=1
                if len(M[lowone[M[i][-1]]]) > max_trick:
                    max_trick = len(M[lowone[M[i][-1]]])
                M[lowone[M[i][-1]]], M[i] = M[i], M[lowone[M[i][-1]]]
                
                
            #M[i] = symmDiff(M[lowone[M[i][-1]]],M[i])
            
            M[i] = addcolumns(M[lowone[M[i][-1]]],M[i])
            trick_cost +=1
            
        if M[i] !=[]:
            lowone[M[i][-1]] = i

    
    if not Twist:
    
        return [len(A), bitaddition,0,trick_cost, trick, max_trick]
    else:
        
        M_new = copy.deepcopy(A)
        for i in range (len(M)):
            if M[i] == [] and i in lowone:
                M_new[i] = []
        
        return [len(A), bitaddition,red_alg_mod_count(M_new,False)[1],trick_cost, trick, max_trick]
        



def exhaustive(A,count = False):
    M = copy.deepcopy(A)
    lowone = {} ###dictionary that saves row index of lowest one as key, and corresponding column index with it
    bitaddition = 0
    twistaddition = [] 
    for i in range(len(M)):
        
        
        temp = bitaddition
        j = 1
        while j <= len(M[i]):
            if M[i][-j] in lowone:
                #M[i] = symmDiff(M[lowone[M[i][-1]]],M[i])
                bitaddition += len(M[lowone[M[i][-j]]])
                M[i] = addcolumns(M[lowone[M[i][-j]]],M[i])
                
                j = 0
            j +=1
                
        twistaddition.append(bitaddition -temp)  
        if M[i] !=[]:
            lowone[M[i][-1]] = i
            twistaddition[M[i][-1]] = 0
        
    if count:
        return [bitaddition,sum(twistaddition)]
    else:
        return M