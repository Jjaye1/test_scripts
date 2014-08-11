import smact.core as smact 
import numpy as np 
our_list = smact.ordered_elements(1,100)
proton = [] ; crustal = [] ; HHI_P = [] ; HHI_r = []
for element in our_list:
    a = smact.Element(element)
    if  a.crustal_abundance and a.HHI_p:
        proton.append(a.number)
        crustal.append(a.crustal_abundance)
        HHI_P.append(a.HHI_p)
        HHI_r.append(a.HHI_R)  
data = np.empty(shape=(len(proton),4))
for i in range(len(proton)-1):
    data[i,0] = proton[i]
    data[i,1] = crustal[i]
    data[i,2] = HHI_P[i]
   ....:     data[i,3] = HHI_r[i] 


  
	
	