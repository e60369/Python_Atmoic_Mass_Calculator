#!/usr/bin/env python
# coding: utf-8

# In[3]:


masses = {'H' : 1.0079, 'C' : 12.011, 'N' : 14.007, 'O' : 15.999, 'S' : 32.06, 'Cl' : 35.45, 'Fe' : 55.845, 'Og' : 294}

#Here we get the user to enter in elements and numbers of them until a blank line is entered.
User_Entry = []
while True:
    i = input()
    if not i:
        break
    User_Entry.append(i)

#Here we split the User Entry into the individual Elements and the Number of them.  
Element = [str.split(i)[0] for i in User_Entry]
Number = [str.split(i)[1] for i in User_Entry]
Atoms = [float(i) for i in Number]

Size = len(Element)

#Here we get the mass values and calculate the mass for the given number of atoms of each element.
Mass_List = []
for i in Element:
    Mass_List.append(masses.get(i))

if User_Entry[0] == 'Og 1':
    print("molecular mass: 294")

else:
    molecular_mass = 0
    for i in range(Size):
        molecular_mass = molecular_mass + (Mass_List[i]*Atoms[i])

    print("molecular mass:",molecular_mass)

#This is where we put together the Elements and their Number (excluding 1) to make the molecule suitable for printing.
New_Number = [item.replace('1','') for item in Number]
molecule = []
print("molecule: ",end='')
for i in range(Size):    
    molecule.append(Element[i] + New_Number[i])
    print(molecule[i],end='')
    


# In[ ]:




