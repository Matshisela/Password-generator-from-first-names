#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Password Generator
def password_generator(x, y, z):
    print("Your suggested password is: " + str(x) + str(y) + str(z)) 
    


# In[ ]:


name = input("What is your name?:")
y = len(name)
 
if len(name) < 4:
    z = "$%#"
elif len(name)  > 5 and len(name) < 8:
    z = "%$@"
else :
    z = "$#%"
    
password_generator(name, y, z)


# In[ ]:




