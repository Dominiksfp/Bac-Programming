import random
from itertools import combinations 
import Matrix_reduc
import copy

def rSubset(size, dimension): 

     
    arr = [x for x in range(size)]
    arr = list(combinations(arr, dimension))
    arr = [list(x) for x in arr]
    
    
    return random.sample(arr,len(arr))

def eucdistsqar(x,y):
    return sum([(a - b) ** 2 for a, b in zip(x, y)])

def sorted_edges(points):
    size = len(points)
    y = []
    for i in range(size):
        for j in range(i):
           y.append([j,i])
           
    
    return sorted(y, key = lambda x: eucdistsqar(points[x[0]],points[x[1]]))


def rips_f(points):
    size = len(points)
    edges = sorted_edges(points)
    boundary = [[]]*size
    neighbourhood= [set() for i in range(size)]
    count = size
    edgepos = {}
    for x in edges:
        boundary.append(x)
        edgepos[tuple(x)] = count
        count +=1
        for y in neighbourhood[x[0]].intersection(neighbourhood[x[1]]):
            z = sorted([x[0],x[1],y])
            boundary.append(sorted([edgepos[(z[0],z[1])], edgepos[(z[0],z[2])],edgepos[(z[1],z[2])]]))
            count +=1
            
            
            
        neighbourhood[x[0]].add(x[1])
        neighbourhood[x[1]].add(x[0])
        
    
    return boundary


    

def erdoes_renyi(points):
    size = len(points)
    edges = rSubset(size,2)
    boundary = [[]]*size
    neighbourhood= [set() for i in range(size)]
    count = size
    edgepos = {}
    for x in edges:
        boundary.append(x)
        edgepos[tuple(x)] = count
        count +=1
        for y in neighbourhood[x[0]].intersection(neighbourhood[x[1]]):
            z = sorted([x[0],x[1],y])
            boundary.append(sorted([edgepos[(z[0],z[1])], edgepos[(z[0],z[2])],edgepos[(z[1],z[2])]]))
            count +=1
            
            
            
        neighbourhood[x[0]].add(x[1])
        neighbourhood[x[1]].add(x[0])
        
    
    return boundary

def shuffled_filtration(points):
    size = len(points)
    
    edgepos = {}
    
    perm = [x for x in range(size)]
    random.shuffle(perm)
    edges = rSubset(size,2)
    triangles = rSubset(size,3)
    count = size
    boundary = [[]]*size
    for x in edges:
        boundary.append(sorted([perm.index(x[0]),perm.index(x[1])]))
        edgepos[tuple(x)] = count
        count +=1
    for x in triangles:
        z = sorted([x[0],x[1],x[2]])
        boundary.append(sorted([edgepos[(z[0],z[1])], edgepos[(z[0],z[2])],edgepos[(z[1],z[2])]]))
        count +=1
    

    return boundary
    
    
def lower_star(points):
    size = len(points)
    
#    perm = [x for x in range(size)]
#    random.shuffle(perm)
    count = 0
    indices = {}
    boundary = []
    for i in range(size):
        boundary.append([])
        indices[i] = count
        count +=1
        for j in range(i):
            boundary.append(sorted([indices[j],indices[i]]))
            indices[(j,i)] = count
            count +=1
            for k in range(j):
                boundary.append(sorted([indices[k,i],indices[k,j],indices[j,i]]))
                count +=1
      
    return boundary





def pic_filt(greyvalue):
    temp = copy.deepcopy(greyvalue)
    temp.sort(key = lambda x: x[2])
    
    count = 0
    indices = {}
    boundary = []
    
    for x in temp:
        indices[(x[0],x[1])] = [-1,[False,False,False,False],[0,0,0,0]]
    
    for x in temp:
        boundary.append([])
        #print(Matrix_reduc.restore_M(boundary))
        indices[(x[0],x[1])][0] = count
        count +=1
        
        
        if (x[0],x[1]-1) in indices and  indices[(x[0],x[1]-1)][0] >=0:                      #left edge
            
            boundary.append([indices[x[0],x[1]-1][0],indices[x[0],x[1]][0]])
            temp1 = count
            count +=1
            

            
            if (x[0]-1,x[1]-1) in indices:
                indices[(x[0]-1,x[1]-1)][1][2] = True
                indices[(x[0]-1,x[1]-1)][2][2] = temp1
                
                if indices[(x[0]-1,x[1]-1)][1] == [True,True,True,True]:
                    boundary.append(sorted(indices [(x[0]-1,x[1]-1)][2]))
                    count +=1
            
            
            
            if (x[0],x[1]-1) in indices:
                indices[(x[0],x[1]-1)][1][0] = True
                indices[(x[0],x[1]-1)][2][0] = temp1
         
                if indices[(x[0],x[1]-1)][1] == [True,True,True,True]:
                    boundary.append(sorted(indices [(x[0],x[1]-1)][2]))
                    count +=1
        
        
        
        if (x[0],x[1]+1) in indices and  indices[(x[0],x[1]+1)][0] >=0:               #right  edge
            boundary.append([indices[x[0],x[1]+1][0],indices[x[0],x[1]][0]])
            temp1 = count
            count +=1
            

            if (x[0],x[1]) in indices:
                indices[(x[0],x[1])][1][0] = True
                indices[(x[0],x[1])][2][0] = temp1
            
                if indices[(x[0],x[1])][1] == [True,True,True,True]:
                    boundary.append(sorted(indices[(x[0],x[1])][2]))
                    count +=1
            
            
            
            if (x[0]-1,x[1]) in indices:
                indices[(x[0]-1,x[1])][1][2] = True
                indices[(x[0]-1,x[1])][2][2] = temp1
                
                if indices[(x[0]-1,x[1])][1] == [True,True,True,True]:
                    boundary.append(sorted(indices[(x[0]-1,x[1])][2]))
                    count +=1
                
                
                
        if (x[0]+1,x[1]) in indices and  indices[(x[0]+1,x[1])][0] >=0:         #edge down
            boundary.append([indices[x[0]+1,x[1]][0],indices[x[0],x[1]][0]])
            temp1 = count
            count +=1
            

            if (x[0],x[1]-1) in indices:
                indices[(x[0],x[1]-1)][1][1] = True
                indices[(x[0],x[1]-1)][2][1] = temp1
                
                if indices[(x[0],x[1]-1)][1] == [True,True,True,True]:
                    boundary.append(sorted(indices[(x[0],x[1]-1)][2]))
                    count +=1
                
                
                
            if (x[0],x[1]) in indices:
                indices[(x[0],x[1])][1][3] = True
                indices[(x[0],x[1])][2][3] = temp1
                
                if indices[(x[0],x[1])][1] == [True,True,True,True]:
                    boundary.append(sorted(indices[(x[0],x[1])][2]))
                    count +=1
                
                
                
        if (x[0]-1,x[1]) in indices and  indices[(x[0]-1,x[1])][0] >=0:        #edge up
            boundary.append([indices[x[0]-1,x[1]][0],indices[x[0],x[1]][0]])
            temp1 = count
            count +=1
            

            if (x[0]-1,x[1]-1) in indices:
                indices[(x[0]-1,x[1]-1)][1][1] = True
                indices[(x[0]-1,x[1]-1)][2][1] = temp1
                
                if indices[(x[0]-1,x[1]-1)][1] == [True,True,True,True]:
                    boundary.append(sorted(indices[(x[0]-1,x[1]-1)][2]))
                    count +=1
            
            if (x[0]-1,x[1]) in indices:
                indices[(x[0]-1,x[1])][1][3] = True
                indices[(x[0]-1,x[1])][2][3] = temp1
             
                if indices[(x[0]-1,x[1])][1] == [True,True,True,True]:
                    boundary.append(sorted(indices[(x[0]-1,x[1])][2]))
                    count +=1
    
    
    
    return boundary


def printm(M,filename):
    data = open(filename,"w")
    
    for x in M:
        s=''
        for y in x:
            s += str(y) + " "
        
        data.write(s+"\n")
    data.close()
    return


def readm(filename):
    M = []
    data = open(filename,"r")
    for line in data:
        if line == "\n":
            M.append([])
        else:
       
            M.append([int(x) for x in line.strip().split(' ')])
    
    data.close()
    return M

def print_ran_sample(size_i,amount,step):
    
    size = size_i
    for j in range(amount):
        randpoints = []
        for i in range(size):
           randpoints.append ((random.random(),random.random()))
         
        printm(rips_f(randpoints),"random_"+str(size)+"_rips.txt")
        printm(shuffled_filtration(randpoints),"random_"+str(size)+"_shuffled.txt")
        printm(lower_star(randpoints),"random_"+str(size)+"_lowerstar.txt")
        printm(erdoes_renyi(randpoints),"random_"+str(size)+"_erdoes_renyi.txt")
        size +=step
       
        
def run_tests(size_i,amount,step,pointdimension):
    
    firstline = 'Simulating Points of dimension '+str(pointdimension)+'         OPERATIONS:'+ '\n'+'Simplices: '.ljust(15)+'Normal'.ljust(15) +'Normal_Twist'.ljust(15)+'Modified'.ljust(15)+'Modified_Twist'.ljust(15)+'Exhaustive'.ljust(15)+'Exhaustive_Twist \n'
    
    
    size = size_i
    data1 = open("testsample_rips_d"+str(pointdimension)+".txt","w")
    data2 = open("testsample_shuffled_d"+str(pointdimension)+".txt","w")
    data3 = open("testsample_erdos_renyi_d"+str(pointdimension)+".txt","w")
    
    data1.write(firstline)
    data2.write(firstline)
    data3.write(firstline)
    for j in range(amount):
        print("Fortschritt: "+str(j)+" von "+str(amount))
        randpoints = []
        for i in range(size):
            temp = []
            for k in range(pointdimension):
               temp.append(random.random())
            randpoints.append(tuple(temp))
         
        x = rips_f(randpoints)
        y = shuffled_filtration(randpoints)
        z= erdoes_renyi(randpoints)
        
       
        out2 = Matrix_reduc.red_alg_mod_count(x,True)
        out1 = Matrix_reduc.red_alg_count(x)
        out3 = Matrix_reduc.exhaustive(x,True)
        
        out5 = Matrix_reduc.red_alg_mod_count(y,True)
        out4 = Matrix_reduc.red_alg_count(y)
        out6 = Matrix_reduc.exhaustive(y,True)
        
        out8 = Matrix_reduc.red_alg_mod_count(z,True)
        out7 = Matrix_reduc.red_alg_count(z)
        out9 = Matrix_reduc.exhaustive(z,True)
        
        
        
        
        
        
        data1.write(str(out2[0]).ljust(15)+str(out1[0]).ljust(15)+str(out1[1]).ljust(15)+str(out2[1]).ljust(15)+str(out2[2]).ljust(15)+str(out3[0]).ljust(15)+str(out3[1]).ljust(15)+'\n')
        data2.write(str(out2[0]).ljust(15)+str(out4[0]).ljust(15)+str(out4[1]).ljust(15)+str(out5[1]).ljust(15)+str(out5[2]).ljust(15)+str(out6[0]).ljust(15)+str(out6[1]).ljust(15)+'\n')
        data3.write(str(out2[0]).ljust(15)+str(out7[0]).ljust(15)+str(out7[1]).ljust(15)+str(out8[1]).ljust(15)+str(out8[2]).ljust(15)+str(out9[0]).ljust(15)+str(out9[1]).ljust(15)+'\n')
        
        
        
           
       
        
        
        
        size +=step
        
    data1.close()
    data2.close()
    data3.close()
    return 
    
    
    
def randpic(a,b):
    
    greyval = []
    for i in range(a):
        for j in range(b):
            greyval.append([i,j,random.random()])
    return pic_filt(greyval)
    
    
    
    
    
    
def pic_tests(size_x,size_y,amount,step):
    
     
    firstline = 'Simulating Filtrations on random pictures          OPERATIONS:'+ '\n'+'Simplices: '.ljust(15)+'Normal'.ljust(15) +'Normal_Twist'.ljust(15)+'Modified'.ljust(15)+'Modified_Twist'.ljust(15)+'Exhaustive'.ljust(15)+'Exhaustive_Twist \n'
    
    
    
    a = size_x
    b = size_y
    data1 = open("pic_filt.txt","w")
    data1.write(firstline)
    
    for j in range(amount):
        print("Fortschritt: "+str(j)+" von "+str(amount))
        
        x = randpic(a,b)
        
       
        out2 = Matrix_reduc.red_alg_mod_count(x,True)
        out1 = Matrix_reduc.red_alg_count(x)
        out3 = Matrix_reduc.exhaustive(x,True)
        
        data1.write(str(out2[0]).ljust(15)+str(out1[0]).ljust(15)+str(out1[1]).ljust(15)+str(out2[1]).ljust(15)+str(out2[2]).ljust(15)+str(out3[0]).ljust(15)+str(out3[1]).ljust(15)+'\n')
  
        
        a +=step
        b +=step
        
    data1.close()
    return 
    