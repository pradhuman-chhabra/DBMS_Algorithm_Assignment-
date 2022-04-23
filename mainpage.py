#!/usr/bin/env python
# coding: utf-8

# In[32]:


from tkinter import*
import sqlite3
from tkinter import font as tkFont

mpage=Tk()
mpage.title('Database Of Garment Retailer')
mpage.geometry("370x250")
mpage['bg']='#FFFAF0'


def producttable():
 mpage.destroy()
 import producttable

def customertable():
 mpage.destroy()
 import customertable

helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
Main= Label(mpage,text="Welcome!")
Main.grid(row=0,column=0,padx=70,pady=(20,0))
Main['font'] = helv36

pr_btn=Button(mpage,text="Go To Product Table",command=producttable)
pr_btn.grid(row=5,column=0 ,columnspan=2,pady=20,padx=10,ipadx=110)


customer_btn=Button(mpage,text="Go To Customer Table",command=customertable)
customer_btn.grid(row=6,column=0 ,columnspan=2,pady=10,padx=10,ipadx=105)

mpage.mainloop()


# In[ ]:





# In[ ]:




