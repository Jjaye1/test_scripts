import smact.core as core
our_list = core.ordered_elements(1,90)
for name in our_list:
    x = core.Element(name)
    print x.name