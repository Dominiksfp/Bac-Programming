import func
import timeit
import Matrix_reduc
import phat
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import math

size = 60
acc = 10
lim = 51
norm,mod,normtw,modtw,ex,extw = [0]*(lim-2),[0]*(lim-2),[0]*(lim-2),[0]*(lim-2),[0]*(lim-2),[0]*(lim-2)

for pointdimension in range(2,lim):
    
        
    
    for j in range(acc):
        randpoints = []
        for i in range(size):
                temp = []
                for j in range(pointdimension):
                   temp.append(random.random())
                randpoints.append(tuple(temp))
             
        x = func.rips_f(randpoints)
        out1 = Matrix_reduc.red_alg_count(x)
        out2 = Matrix_reduc.red_alg_mod_count(x,True)
        out3 = Matrix_reduc.exhaustive(x,True)
        norm[pointdimension-2] += out1[0]
        normtw[pointdimension-2] += out1[1]
        mod[pointdimension-2] +=out2[1]
        modtw[pointdimension-2] +=out2[2]
        ex[pointdimension-2] += out3[0]
        extw[pointdimension-2] += out3[1]

    print("Fortschschritt: ",pointdimension-2)


xaxis = [i for i in range(2,lim)]

fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc*10**6) for x in norm])
ax.plot(xaxis,[x/(acc*10**6) for x in mod])
ax.plot(xaxis,[x/(acc*10**6) for x in ex])

ax.set_title('Rips-Filtration without Twist on ~ 50000 simplices')
ax.legend(['Normal', 'Modified', 'Exhaustive'])

ax.set_xlabel('Point-Dimension')
ax.set_ylabel('Operations in Million')
fig.savefig('Ripsdimension_notwist')   
plt.close(fig)





fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc) for x in normtw])
ax.plot(xaxis,[x/(acc) for x in modtw])
ax.plot(xaxis,[x/(acc) for x in extw])

ax.set_title('Rips-Filtration with Twist on ~ 50000 simplices')
ax.legend(['Normal', 'Modified', 'Exhaustive'])

ax.set_xlabel('Point-Dimension')
ax.set_ylabel('Operations ')
fig.savefig('Ripsdimension_twist')   
plt.close(fig)

################################################################################'''



amount = 90
acc = 10
size = 20
pointdimension = 2


################################################################################
norm,mod,normtw,modtw,ex,extw = [0]*amount,[0]*amount,[0]*amount,[0]*amount,[0]*amount,[0]*amount
xaxis = []

for k in range(amount):
    
        
    
    for j in range(acc):
        randpoints = []
        for i in range(size):
                temp = []
                for j in range(pointdimension):
                   temp.append(random.random())
                randpoints.append(tuple(temp))
             
        x = func.rips_f(randpoints)
        out1 = Matrix_reduc.red_alg_count(x)
        out2 = Matrix_reduc.red_alg_mod_count(x,False)
        out3 = Matrix_reduc.exhaustive(x,True)
        norm[k] += out1[0]
        normtw[k] += out1[1]
        mod[k] +=out2[1]
        modtw[k] +=out2[2]
        ex[k] += out3[0]
        extw[k] += out3[1]
    size +=1
    xaxis.append(out2[0])
    print("Fortschschritt: Rips",k)




fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc*10**6) for x in norm],color = 'blue')
ax.plot(xaxis,[x/(acc*10**6) for x in mod],color = 'red')
ax.plot(xaxis,[x/(acc*10**6) for x in ex],color = 'green')


ax.set_title('Comparison of algorithms on a Rips filtration')
ax.legend(['Normal', 'Modified', 'Exhaustive'])

ax.set_xlabel('Simplices')
ax.set_ylabel('Operations in Millions')
fig.savefig('Rips_filt_notwist')   
plt.close(fig)
    


fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc) for x in normtw])
ax.plot(xaxis,[x/(acc) for x in modtw])
ax.plot(xaxis,[x/(acc) for x in extw])

ax.set_title('Rips-Filtration with Twist')
ax.legend(['Normal', 'Modified', 'Exhaustive'])

ax.set_xlabel('Simplices')
ax.set_ylabel('Operations ')
fig.savefig('Rips_filt_twist')   
plt.close(fig)






################################################################################
norm,mod,normtw,modtw,ex,extw = [0]*amount,[0]*amount,[0]*amount,[0]*amount,[0]*amount,[0]*amount
xaxis = []

for k in range(amount):
    
        
    
    for j in range(acc):
        randpoints = []
        for i in range(size):
                temp = []
                for j in range(pointdimension):
                   temp.append(random.random())
                randpoints.append(tuple(temp))
             
        x = func.shuffled_filtration(randpoints)
        out1 = Matrix_reduc.red_alg_count(x)
        out2 = Matrix_reduc.red_alg_mod_count(x,True)
        out3 = Matrix_reduc.exhaustive(x,True)
        norm[k] += out1[0]
        normtw[k] += out1[1]
        mod[k] +=out2[1]
        modtw[k] +=out2[2]
        ex[k] += out3[0]
        extw[k] += out3[1]
    size +=1
    xaxis.append(out2[0])
    print("Fortschschritt: Shuffled",k)

regx1 = np.array([math.log10(x) for x in xaxis]).reshape((-1,1))
regy1 = np.array([math.log10(x) for x in norm])
model1 = LinearRegression().fit(regx1, regy1)

regx2 = np.array([math.log10(x) for x in xaxis]).reshape((-1,1))
regy2 = np.array([math.log10(x) for x in mod])
model2 = LinearRegression().fit(regx2, regy2)

regx3 = np.array([math.log10(x) for x in xaxis]).reshape((-1,1))
regy3 = np.array([math.log10(x) for x in ex])
model3 = LinearRegression().fit(regx3, regy3)




fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc*10**6) for x in norm], color = 'blue')
ax.plot(xaxis,[x/(acc*10**6) for x in mod], color = 'red')
ax.plot(xaxis,[x/(acc*10**6) for x in ex], color = 'green')
ax.plot(xaxis,[(10**model1.intercept_)*x**model1.coef_[0]/(acc*10**6) for x in xaxis],'o', color = 'blue')
ax.plot(xaxis,[(10**model2.intercept_)*x**model2.coef_[0]/(acc*10**6) for x in xaxis],'o', color = 'red')
ax.plot(xaxis,[(10**model3.intercept_)*x**model3.coef_[0]/(acc*10**6) for x in xaxis],'o', color = 'green')

n1 = '\n'+str(r'$y=%.3f x^{%.3f}$' % ((10**model1.intercept_),model1.coef_[0]))
n2 = '\n'+str(r'$y=%.3f x^{%.3f}$' % ((10**model2.intercept_),model2.coef_[0]))
n3 = '\n'+str(r'$y=%.3f x^{%.3f}$' % ((10**model3.intercept_),model3.coef_[0]))

ax.set_title('Comparison of algorithms on a Shuffled filtration')
ax.legend(['Normal ', 'Modified', 'Exhaustive','Power (Normal)'+n1,'Power (Modified)'+n2,'Power (Exhaustive)'+n3])

ax.set_xlabel('Simplices')
ax.set_ylabel('Operations in Millions')
fig.savefig('Shuffled_filt_notwist')   
plt.close(fig)
    
regx1 = np.array([math.log10(x) for x in xaxis]).reshape((-1,1))
regy1 = np.array([math.log10(x) for x in normtw])
model1 = LinearRegression().fit(regx1, regy1)

regx2 = np.array([math.log10(x) for x in xaxis]).reshape((-1,1))
regy2 = np.array([math.log10(x) for x in modtw])
model2 = LinearRegression().fit(regx2, regy2)

regx3 = np.array([math.log10(x) for x in xaxis]).reshape((-1,1))
regy3 = np.array([math.log10(x) for x in extw])
model3 = LinearRegression().fit(regx3, regy3)




fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc*10**6) for x in normtw], color = 'blue')
ax.plot(xaxis,[x/(acc*10**6) for x in modtw], color = 'red')
ax.plot(xaxis,[x/(acc*10**6) for x in extw], color = 'green')
ax.plot(xaxis,[(10**model1.intercept_)*x**model1.coef_[0]/(acc*10**6) for x in xaxis],'o', color = 'blue')
ax.plot(xaxis,[(10**model2.intercept_)*x**model2.coef_[0]/(acc*10**6) for x in xaxis],'o', color = 'red')
ax.plot(xaxis,[(10**model3.intercept_)*x**model3.coef_[0]/(acc*10**6) for x in xaxis],'o', color = 'green')

n1 = '\n'+str(r'$y=%.3f x^{%.3f}$' % ((10**model1.intercept_),model1.coef_[0]))
n2 = '\n'+str(r'$y=%.3f x^{%.3f}$' % ((10**model2.intercept_),model2.coef_[0]))
n3 = '\n'+str(r'$y=%.3f x^{%.3f}$' % ((10**model3.intercept_),model3.coef_[0]))

ax.set_title('Comparison of algorithms combined with the Clearing on a Shuffled filtration')
ax.legend(['Normal ', 'Modified', 'Exhaustive','Power (Normal)'+n1,'Power (Modified)'+n2,'Power (Exhaustive)'+n3])

ax.set_xlabel('Simplices')
ax.set_ylabel('Operations in Millions ')
fig.savefig('Shuffled_filt_twist')   
plt.close(fig)


'''

'''
################################################################################
norm,mod,normtw,modtw,ex,extw = [0]*amount,[0]*amount,[0]*amount,[0]*amount,[0]*amount,[0]*amount
xaxis = []

for k in range(amount):
    
        
    
    for j in range(acc):
        randpoints = []
        for i in range(size):
                temp = []
                for j in range(pointdimension):
                   temp.append(random.random())
                randpoints.append(tuple(temp))
             
        x = func.erdoes_renyi(randpoints)
        out1 = Matrix_reduc.red_alg_count(x)
        out2 = Matrix_reduc.red_alg_mod_count(x,True)
        out3 = Matrix_reduc.exhaustive(x,True)
        norm[k] += out1[0]
        normtw[k] += out1[1]
        mod[k] +=out2[1]
        modtw[k] +=out2[2]
        ex[k] += out3[0]
        extw[k] += out3[1]
    size +=1
    xaxis.append(out2[0])
    print("Fortschschritt: Erdos",k)




fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc*10**6) for x in norm])
ax.plot(xaxis,[x/(acc*10**6) for x in mod])
ax.plot(xaxis,[x/(acc*10**6) for x in ex])

ax.set_title('Erdoes_Renyi-Filtration without Twist')
ax.legend(['Normal', 'Modified', 'Exhaustive'])

ax.set_xlabel('Simplices')
ax.set_ylabel('Operations in Million')
fig.savefig('erdoes_renyi_notwist')   
plt.close(fig)
    


fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(xaxis,[x/(acc) for x in normtw])
ax.plot(xaxis,[x/(acc) for x in modtw])
ax.plot(xaxis,[x/(acc) for x in extw])

ax.set_title('Erdoes_Renyi-Filtration with Twist')
ax.legend(['Normal', 'Modified', 'Exhaustive'])

ax.set_xlabel('Simplices')
ax.set_ylabel('Operations ')
fig.savefig('erdoes_renyi_twist')   
plt.close(fig)





################################################################################


