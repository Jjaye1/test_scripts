import smact.core as smact
def is_neutral(a,b,range_a = 4, range_b = 4):
    is_neutral = False ; stoic_a = 0 ; stoic_b = 0
    for i in range(1,range_a):
        for j in range(1,range_b):
            if i*a == -j*b:
                is_neutral = True
                stoic_a = i
                stoic_b = j
		return is_neutral,stoic_a,stoic_b
#    for i in range(1,min(stoic_a,stoic_b)):
#	if max(stoic_a,stoic_b)/i == min(stoic_a,stoic_b):
#	    is_neutral = False
    return is_neutral,stoic_a,stoic_b 
 
def neutral_combo_exists(x,y):
    elea = smact.Element(a)
    for a_ox in elea.oxidation_states:
        for b in our_list:                            
            eleb = smact.Element(b)
            if eleb.number > elea.number:
                for b_ox in eleb.oxidation_states:
                    neutral_exists, stoic_a, stoic_b = is_neutral(a_ox,b_ox)
                    if neutral_exists:
                        cov = 0 ; polar_covalent = 0 ; polar_ionic = 0
                        elecnx = smact.Element(x)
                        elecny = smact.Elements(y)
                            for pauling in elecnx.pauling_eneg:


print our_list
print list
