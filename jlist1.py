import smact.core as smact
import numpy as np 
import matplotlib.pyplot as plt
our_list = smact.ordered_elements(1,100)
   

# Define our fonts
font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 20,
        }

our_list = smact.ordered_elements(1,100)
proton_1 = [] ; crustal_1 = [] ; HHI_P_1 = [] ; HHI_r_1 = []
for element in our_list:
    a = smact.Element(element)
    if  a.crustal_abundance and a.HHI_p:
		if a.trivialname == 'alkali_metals':
            proton_1.append(a.number)
        	crustal_1.append(a.crustal_abundance)
        	HHI_P_1.append(a.HHI_p)
        	HHI_r_1.append(a.HHI_R) 
		elif a.trivialname == ''

data = np.zeros(shape=(len(proton),4))
for i in range(len(proton)-1):
    data[i,0] = proton[i]
    data[i,1] = crustal[i]
    data[i,2] = HHI_P[i]
    data[i,3] = HHI_r[i]    

# SOME PLOTTING OF DATA 
plt.plot(data[:,0],data[:,1], '*')
plt.xlabel('Proton number', fontdict=font)
plt.ylabel('Crustal abundance (mg/kg)', fontdict=font) 
plt.savefig('crustalvproton.pdf')
plt.show()
plt.plot(data[:,2],data[:,1], '*')
plt.xlabel('HHIp', fontdict=font)
plt.ylabel('Crustal abundance (mg/kg)', fontdict=font) 
plt.savefig('crustalvHHIp.pdf')
plt.show()
plt.plot(data[:,3],data[:,1], '*')
plt.xlabel('HHIR', fontdict=font)
plt.ylabel('Crustal abundance (mg/kg)', fontdict=font) 
plt.savefig('crustalvHHI$_R$.pdf')
plt.show()
plt.plot(data[:,2],data[:,0], '*')
plt.xlabel('HHIp', fontdict=font)
plt.ylabel('Proton number', fontdict=font) 
plt.savefig('protonnumbervHHI$_p$.pdf')
plt.show()
plt.plot(data[:,3],data[:,0], '*')
plt.xlabel('HHIR', fontdict=font)
plt.ylabel('Proton number', fontdict=font) 
plt.savefig('protonvHHIR.pdf')
plt.show()             
plt.plot(data[:,2],data[:,3], '*')
plt.xlabel('HHIp', fontdict=font)
plt.ylabel('HHIR', fontdict=font) 
plt.savefig('HHIRvHHIp.pdf')
plt.show()


# SAVE FIGURE

proton = [] ; ionpoten = [] ; paelectro = [] ; elec_affinity = []

for element in our_list:
	a= smact.Element(element)
	if a.ionpot and a.pauling_eneg and a.e_affinity:
		proton.append(a.number) 
		ionpoten.append(a.ionpot)
        paelectro.append(a.pauling_eneg)
        elec_affinity.append(a.e_affinity) 

data = np.empty(shape=(len(proton),4)) 

for i in range(len(proton)-1):
	data[i,0] = proton[i]
	data[i,1] = ionpoten[i]
	data[i,2] = paelectro[i]
	data[i,3] = elec_affinity[i]