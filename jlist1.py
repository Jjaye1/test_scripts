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
proton_2 = [] ; crustal_2 = [] ; HHI_P_2 = [] ; HHI_r_2 = []
proton_3 = [] ; crustal_3 = [] ; HHI_P_3 = [] ; HHI_r_3 = []
proton_4 = [] ; crustal_4 = [] ; HHI_P_4 = [] ; HHI_r_4 = []
proton_5 = [] ; crustal_5 = [] ; HHI_P_5 = [] ; HHI_r_5 = []
proton_6 = [] ; crustal_6 = [] ; HHI_P_6 = [] ; HHI_r_6 = []
proton_7 = [] ; crustal_7 = [] ; HHI_P_7 = [] ; HHI_r_7 = []
proton_8 = [] ; crustal_8 = [] ; HHI_P_8 = [] ; HHI_r_8 = []
proton_9 = [] ; crustal_9 = [] ; HHI_P_9 = [] ; HHI_r_9 = []

for element in our_list:
    a = smact.Element(element)
    if a.crustal_abundance and a.HHI_p:
        if a.trivialname == 'alkali_metals':
            proton_1.append(a.number)
            crustal_1.append(a.crustal_abundance)
            HHI_P_1.append(a.HHI_p)
            HHI_r_1.append(a.HHI_R)
        elif a.trivialname == 'alkaline_earth_metals':
            proton_2.append(a.number)
            crustal_2.append(a.crustal_abundance)
            HHI_P_2.append(a.HHI_p)
            HHI_r_2.append(a.HHI_R)
        elif a.trivialname == 'group_d_metals':
             proton_3.append(a.number)
             crustal_3.append(a.crustal_abundance)
             HHI_P_3.append(a.HHI_p)
             HHI_r_3.append(a.HHI_R)
        elif a.trivialname == 'pnictogens':
             proton_4.append(a.number)
             crustal_4.append(a.crustal_abundance)
             HHI_P_4.append(a.HHI_p)
             HHI_r_4.append(a.HHI_R)
        elif a.trivialname == 'chalcogens':
             proton_5.append(a.number)
             crustal_5.append(a.crustal_abundance)
             HHI_P_5.append(a.HHI_p)
             HHI_r_5.append(a.HHI_R)
        elif a.trivialname == 'halogens':
            proton_6.append(a.number)
            crustal_6.append(a.crustal_abundance)
            HHI_P_6.append(a.HHI_p)
            HHI_r_6.append(a.HHI_R)
        elif a.trivialname == 'group_3':
            proton_7.append(a.number)
            crustal_7.append(a.crustal_abundance)
            HHI_P_7.append(a.HHI_p)
            HHI_r_7.append(a.HHI_R)
        elif a.trivialname == 'group_4':
            proton_8.append(a.number)
            crustal_8.append(a.crustal_abundance)
            HHI_P_8.append(a.HHI_p)
            HHI_r_8.append(a.HHI_R)
        elif a.trivialname == 'noble_gases':
            proton_9.append(a.number)
            crustal_9.append(a.crustal_abundance)
            HHI_P_9.append(a.HHI_p)
            HHI_r_9.append(a.HHI_R)
# Plotting of
'''#plt.plot(proton_1[:],crustal_1[:],'H',markersize=10)
#plt.plot(proton_2[:],crustal_2[:] ,'H',markersize=10)
plt.plot(proton_3[:],crustal_3[:] ,'H',markersize=10)
plt.plot(proton_4[:],crustal_4[:] ,'H',markersize=10)
plt.plot(proton_5[:],crustal_5[:] ,'H',markersize=10)
plt.plot(proton_6[:],crustal_6[:] ,'H',markersize=10)
plt.plot(proton_7[:],crustal_7[:] ,'H',markersize=10)
plt.plot(proton_8[:],crustal_8[:] ,'H',markersize=10)
plt.plot(proton_9[:],crustal_9[:] ,'H',markersize=10)
plt.xlabel('Proton number', fontdict=font)
plt.ylabel('Crustal abundance (mg/kg)', fontdict=font)
plt.savefig('crustalvproton.pdf')
plt.show()
plt.plot(HHI_P_1[:],crustal_1[:],'H',markersize=10)
plt.plot(HHI_P_2[:],crustal_2[:],'H',markersize=10)
plt.plot(HHI_P_3[:],crustal_3[:],'H',markersize=10)
plt.plot(HHI_P_4[:],crustal_4[:],'H',markersize=10)
plt.plot(HHI_P_5[:],crustal_5[:],'H',markersize=10)
plt.plot(HHI_P_6[:],crustal_6[:],'H',markersize=10)
plt.plot(HHI_P_7[:],crustal_7[:],'H',markersize=10)
plt.plot(HHI_P_8[:],crustal_8[:],'H',markersize=10)
plt.plot(HHI_P_9[:],crustal_9[:],'H',markersize=10)
plt.xlabel('HHIp', fontdict=font)
plt.ylabel('Crustal abundance (mg/kg)', fontdict=font)
plt.savefig('crustalvHHIp.pdf')
plt.show()
plt.plot(HHI_r_1[:],crustal_1[:], 'H', markersize=10)
plt.plot(HHI_r_2[:],crustal_2[:], 'H', markersize=10)
plt.plot(HHI_r_3[:],crustal_3[:], 'H', markersize=10)
plt.plot(HHI_r_4[:],crustal_4[:], 'H', markersize=10)
plt.plot(HHI_r_5[:],crustal_5[:], 'H', markersize=10)
plt.plot(HHI_r_6[:],crustal_6[:], 'H', markersize=10)
plt.plot(HHI_r_7[:],crustal_7[:], 'H', markersize=10)
plt.plot(HHI_r_8[:],crustal_8[:], 'H', markersize=10)
plt.plot(HHI_r_9[:],crustal_9[:], 'H', markersize=10)
plt.xlabel('HHIR', fontdict=font)
plt.ylabel('Crustal abundance (mg/kg)', fontdict=font)
plt.savefig('crustalvHHIr.pdf')
plt.show()
plt.plot(proton_1[:],HHI_P_1[:],'H', markersize=10)
plt.plot(proton_2[:],HHI_P_2[:],'H', markersize=10)
plt.plot(proton_3[:],HHI_P_3[:],'H', markersize=10)
plt.plot(proton_4[:],HHI_P_4[:],'H', markersize=10)
plt.plot(proton_5[:],HHI_P_5[:],'H', markersize=10)
plt.plot(proton_6[:],HHI_P_6[:],'H', markersize=10)
plt.plot(proton_7[:],HHI_P_7[:],'H', markersize=10)
plt.plot(proton_8[:],HHI_P_8[:],'H', markersize=10)
plt.plot(proton_9[:],HHI_P_9[:],'H', markersize=10)
plt.ylabel('HHIp', fontdict=font)
plt.xlabel('Proton number', fontdict=font)
plt.savefig('protonnumbervHHIp.pdf')
plt.show()
plt.plot(proton_1[:],HHI_r_1[:],'H', markersize=10)
plt.plot(proton_2[:],HHI_r_2[:],'H', markersize=10)
plt.plot(proton_3[:],HHI_r_3[:],'H', markersize=10)
plt.plot(proton_4[:],HHI_r_4[:],'H', markersize=10)
plt.plot(proton_5[:],HHI_r_5[:],'H', markersize=10)
plt.plot(proton_6[:],HHI_r_6[:],'H', markersize=10)
plt.plot(proton_7[:],HHI_r_7[:],'H', markersize=10)
plt.plot(proton_8[:],HHI_r_8[:],'H', markersize=10)
plt.plot(proton_9[:],HHI_r_9[:],'H', markersize=10)
plt.ylabel('HHIR', fontdict=font)
plt.xlabel('Proton number', fontdict=font)
plt.savefig('protonnumbervHHIR.pdf')
plt.show()
plt.plot(HHI_r_1[:],HHI_P_1[:],'H', markersize=10)
plt.plot(HHI_r_2[:],HHI_P_2[:],'H', markersize=10)
plt.plot(HHI_r_3[:],HHI_P_3[:],'H', markersize=10)
plt.plot(HHI_r_4[:],HHI_P_4[:],'H', markersize=10)
plt.plot(HHI_r_5[:],HHI_P_5[:],'H', markersize=10)
plt.plot(HHI_r_6[:],HHI_P_6[:],'H', markersize=10)
plt.plot(HHI_r_7[:],HHI_P_7[:],'H', markersize=10)
plt.plot(HHI_r_8[:],HHI_P_8[:],'H', markersize=10)
plt.plot(HHI_r_9[:],HHI_P_9[:],'H', markersize=10)
plt.ylabel('HHIp', fontdict=font)
plt.xlabel('HHI_r', fontdict=font)
plt.savefig('HHI_rvHHIp.pdf')
plt.show()
'''

# SAVE FIGURE

proton_1 = [] ; ionpoten_1 = [] ; paelectro_1 = [] ; e_affinity_1 = []
proton_2 = [] ; ionpoten_2 = [] ; paelectro_2 = [] ; e_affinity_2 = []
proton_3 = [] ; ionpoten_3 = [] ; paelectro_3 = [] ; e_affinity_3 = []
proton_4 = [] ; ionpoten_4 = [] ; paelectro_4 = [] ; e_affinity_4 = []
proton_5 = [] ; ionpoten_5 = [] ; paelectro_5 = [] ; e_affinity_5 = []
proton_6 = [] ; ionpoten_6 = [] ; paelectro_6 = [] ; e_affinity_6 = []
proton_7 = [] ; ionpoten_7 = [] ; paelectro_7 = [] ; e_affinity_7 = []
proton_8 = [] ; ionpoten_8 = [] ; paelectro_8 = [] ; e_affinity_8 = []
proton_9 = [] ; ionpoten_9 = [] ; paelectro_9 = [] ; e_affinity_9 = []
for element in our_list:
    a= smact.Element(element)
    if a.ionpot and a.pauling_eneg and a.e_affinity:
        if a.trivialname == 'alkali_metals':
            proton_1.append(a.number)
            ionpoten_1.append(a.ionpot)
            paelectro_1.append(a.pauling_eneg)
            e_affinity_1.append(a.e_affinity)
        elif a.trivialname == 'alkaline_earth_metals':
            proton_2.append(a.number)
            ionpoten_2.append(a.ionpot)
            paelectro_2.append(a.pauling_eneg)
            e_affinity_2.append(a.e_affinity)
        elif a.trivialname == 'group_d_metals':
            proton_3.append(a.number)
            ionpoten_3.append(a.ionpot)
            paelectro_3.append(a.pauling_eneg)
            e_affinity_3.append(a.e_affinity)
        elif a.trivialname == 'pnictogens':
            proton_4.append(a.number)
            ionpoten_4.append(a.ionpot)
            paelectro_4.append(a.pauling_eneg)
            e_affinity_4.append(a.e_affinity)
        elif a.trivialname == 'chalcogens':
            proton_5.append(a.number)
            ionpoten_5.append(a.ionpot)
            paelectro_5.append(a.pauling_eneg)
            e_affinity_5.append(a.e_affinity)
        elif a.trivialname == 'halogens':
            proton_6.append(a.number)
            ionpoten_6.append(a.ionpot)
            paelectro_6.append(a.pauling_eneg)
            e_affinity_6.append(a.e_affinity)
        elif a.trivialname == 'group_3':
            proton_7.append(a.number)
            ionpoten_7.append(a.ionpot)
            paelectro_7.append(a.pauling_eneg)
            e_affinity_7.append(a.e_affinity)
        elif a.trivialname == 'group_4':
            proton_8.append(a.number)
            ionpoten_8.append(a.ionpot)
            paelectro_8.append(a.pauling_eneg)
            e_affinity_8.append(a.e_affinity)
        elif a.trivialname == 'noble_gases':
            proton_9.append(a.number)
            ionpoten_9.append(a.ionpot)
            paelectro_9.append(a.pauling_eneg)
            e_affinity_9.append(a.e_affinity)
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.4,0.7])
ax1.plot(proton_1[:],ionpoten_1[:],'H', markersize=10,label='Alkalii Metals')
ax1.plot(proton_2[:],ionpoten_2[:],'H', markersize=10,label='Alkaline Earths')
ax1.plot(proton_3[:],ionpoten_3[:],'H', markersize=10,label='Group D')
ax1.plot(proton_4[:],ionpoten_4[:],'H', markersize=10,label='Pnictogens')
ax1.plot(proton_5[:],ionpoten_5[:],'H', markersize=10,label='Chacogens')
ax1.plot(proton_6[:],ionpoten_6[:],'H', markersize=10,label='Halogens')
ax1.plot(proton_7[:],ionpoten_7[:],'H', markersize=10,label='Group 4')
ax1.plot(proton_8[:],ionpoten_8[:],'H', markersize=10,label='Group 3')
ax1.plot(proton_9[:],ionpoten_9[:],'H', markersize=10,label='Noble Gases')
ax1.legend(loc='upper right', shadow=True)
ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax1.grid(True)
plt.xlabel('Proton number', fontdict=font)
plt.ylabel('Ionisation potential', fontdict=font)
plt.savefig('protonvionpotential.png')
plt.show()

'''
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.4,0.7])
plt.plot(proton_1[:],paelectro_1[:],'H', markersize=10)
plt.plot(proton_2[:],paelectro_2[:],'H', markersize=10)
plt.plot(proton_3[:],paelectro_3[:],'H', markersize=10)
plt.plot(proton_4[:],paelectro_4[:],'H', markersize=10)
plt.plot(proton_5[:],paelectro_5[:],'H', markersize=10)
plt.plot(proton_6[:],paelectro_6[:],'H', markersize=10)
plt.plot(proton_7[:],paelectro_7[:],'H', markersize=10)
plt.plot(proton_8[:],paelectro_8[:],'H', markersize=10)
plt.plot(proton_9[:],paelectro_9[:],'H', markersize=10)
plt.xlabel('Proton number', fontdict=font)
plt.ylabel('Pauling electronegativity', fontdict=font)
plt.savefig('protonvpauling.pdf')
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.4,0.7])
plt.plot(proton_1[:],e_affinity_1[:],'H', markersize=10)
plt.plot(proton_2[:],e_affinity_2[:],'H', markersize=10)
plt.plot(proton_3[:],e_affinity_3[:],'H', markersize=10)
plt.plot(proton_4[:],e_affinity_4[:],'H', markersize=10)
plt.plot(proton_5[:],e_affinity_5[:],'H', markersize=10)
plt.plot(proton_6[:],e_affinity_6[:],'H', markersize=10)
plt.plot(proton_7[:],e_affinity_7[:],'H', markersize=10)
plt.plot(proton_8[:],e_affinity_8[:],'H', markersize=10)
plt.plot(proton_9[:],e_affinity_9[:],'H', markersize=10)
plt.xlabel('Proton number', fontdict=font)
plt.ylabel('Electron affinity', fontdict=font)
plt.savefig('protonvelec.affinity.pdf')
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.4,0.7])
plt.plot(ionpoten_1[:],e_affinity_1[:],'H', markersize=10)
plt.plot(ionpoten_2[:],e_affinity_2[:],'H', markersize=10)
plt.plot(ionpoten_3[:],e_affinity_3[:],'H', markersize=10)
plt.plot(ionpoten_4[:],e_affinity_4[:],'H', markersize=10)
plt.plot(ionpoten_5[:],e_affinity_5[:],'H', markersize=10)
plt.plot(ionpoten_6[:],e_affinity_6[:],'H', markersize=10)
plt.plot(ionpoten_7[:],e_affinity_7[:],'H', markersize=10)
plt.plot(ionpoten_8[:],e_affinity_8[:],'H', markersize=10)
plt.plot(ionpoten_9[:],e_affinity_9[:],'H', markersize=10)
plt.xlabel('Ionisation potential', fontdict=font)
plt.ylabel('Electron affinity', fontdict=font)
plt.savefig('ionpotentialvelec.affinity.pdf')
plt.show()


plt.plot(ionpoten_1[:],paelectro_1[:],'H', markersize=10)
plt.plot(ionpoten_2[:],paelectro_2[:],'H', markersize=10)
plt.plot(ionpoten_3[:],paelectro_3[:],'H', markersize=10)
plt.plot(ionpoten_4[:],paelectro_4[:],'H', markersize=10)
plt.plot(ionpoten_5[:],paelectro_5[:],'H', markersize=10)
plt.plot(ionpoten_6[:],paelectro_6[:],'H', markersize=10)
plt.plot(ionpoten_7[:],paelectro_7[:],'H', markersize=10)
plt.plot(ionpoten_8[:],paelectro_8[:],'H', markersize=10)
plt.plot(ionpoten_9[:],paelectro_9[:],'H', markersize=10)
plt.xlabel('Ionisation potential', fontdict=font)
plt.ylabel('Pauling electronegativity ', fontdict=font)
plt.savefig('ionpotentialvpauling.pdf')
plt.show()

plt.plot(e_affinity_1[:],paelectro_1[:],'H', markersize=10)
plt.plot(e_affinity_2[:],paelectro_2[:],'H', markersize=10)
plt.plot(e_affinity_3[:],paelectro_3[:],'H', markersize=10)
plt.plot(e_affinity_4[:],paelectro_4[:],'H', markersize=10)
plt.plot(e_affinity_5[:],paelectro_5[:],'H', markersize=10)
plt.plot(e_affinity_6[:],paelectro_6[:],'H', markersize=10)
plt.plot(e_affinity_7[:],paelectro_7[:],'H', markersize=10)
plt.plot(e_affinity_8[:],paelectro_8[:],'H', markersize=10)
plt.plot(e_affinity_9[:],paelectro_9[:],'H', markersize=10)
plt.xlabel('Electron affinity', fontdict=font)
plt.ylabel('Pauling electronegativit'|'', fontdict=font)
plt.savefig('paulingvelec.affinity.pdf')
plt.show()
'''







































