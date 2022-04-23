#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import*
import sqlite3

ctable=Tk()
ctable.title('Customer  Table')
ctable.geometry("500x700")
#Background colour
ctable['bg']='#FFFAF0'
#Creating/Accesing a Database
conn=sqlite3.connect('garment_retail.db')

c=conn.cursor()

#Creating a function to go to main page
def mainpage():
 ctable.destroy()
 import mainpage
    
#Creating a function to go to customer table    
def producttable():
 ctable.destroy()
 import producttable

#creating an update function
def update():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute(""" UPDATE customer SET
    c_id=:c_id,
    c_name=:c_name,
    contact=:contact,
    address=:address, 
    no_of_items=:no_of_items,
    total=:total
    
    WHERE oid=:oid""",
    {
        'c_id':c_id_edit.get(),
        'c_name':c_name_edit.get(),
        'contact':contact_edit.get(),
        'address':address_edit.get(),
        'no_of_items':no_of_items_edit.get(),
        'total':total_edit.get(),
        'oid':record_id
        
    }

    )
    conn.commit()
    conn.close()
    edit.destroy()
    
    

def edit():
 global edit   
 #Create edit function to update
 edit=Tk()
 edit.title('Update a Record')
 edit.geometry("500x700")
 edit['bg']='#FFFAF0'
    
 conn=sqlite3.connect('garment_retail.db')
 c=conn.cursor()
 #query the database 
 record_id=delete_box.get()
 c.execute("SELECT*FROM customer where oid = " + record_id)
 records=c.fetchall()
 #create global 
 global c_id_edit
 global c_name_edit
 global contact_edit
 global address_edit
 global no_of_items_edit
 global total_edit
 
#Text Boxes

 c_id_edit=Entry(edit,width=30)
 c_id_edit.grid(row=0,column=1,padx=20,pady=(20,0))

 c_name_edit=Entry(edit,width=30)
 c_name_edit.grid(row=1,column=1,pady=(10,0))

 contact_edit=Entry(edit,width=30)
 contact_edit.grid(row=2,column=1,pady=(10,0))

 address_edit=Entry(edit,width=30)
 address_edit.grid(row=3,column=1,pady=(10,0))

 no_of_items_edit=Entry(edit,width=30)
 no_of_items_edit.grid(row=4,column=1,pady=(10,0))

 total_edit=Entry(edit,width=30)
 total_edit.grid(row=5,column=1,pady=(10,0))




#Labels

 c_id_label= Label(edit,text="Customer ID")
 c_id_label.grid(row=0,column=0,pady=(20,0))

 c_name_label= Label(edit,text="Customer Name")
 c_name_label.grid(row=1,column=0,pady=(10,0))

 contact_label= Label(edit,text="Contact")
 contact_label.grid(row=2,column=0,pady=(10,0))

 address_label= Label(edit,text="Address")
 address_label.grid(row=3,column=0,pady=(10,0))

 no_of_items_label= Label(edit,text="No. of Items")
 no_of_items_label.grid(row=4,column=0,pady=(10,0))

 total_label= Label(edit,text="Total Amount")
 total_label.grid(row=5,column=0,pady=(10,0))

                      

 for record in records:
    c_id_edit.insert(0,record[0])
    c_name_edit.insert(0,record[1])
    contact_edit.insert(0,record[2])
    address_edit.insert(0,record[3])
    no_of_items_edit.insert(0,record[4])
    total_edit.insert(0,record[5])
    
 #Create an Save Button
 save_btn=Button(edit,text="Save Record",command=update)
 save_btn.grid(row=6,column=0,columnspan=2,pady=15,padx=10,ipadx=145)

 


 



 #create Function to delete a record
def delete():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    #Delete a record
    c.execute("DELETE FROM customer WHERE oid="+  delete_box.get())
    conn.commit()
    conn.close()

#Create Submit Function for database
def submit():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    #Insert into table
    c.execute("INSERT INTO customer VALUES (:c_id,:c_name,:contact,:address,:no_of_items,:total)",
               {
                 'c_id':c_id.get(),
                 'c_name':c_name.get(),
                 'contact':contact.get(),
                 'address':address.get(),
                 'no_of_items':no_of_items.get(),
                 'total':total.get()
                })

    conn.commit()
    conn.close()
    

    #clear the text boxes
    c_id.delete(0,END)
    c_name.delete(0,END)
    contact.delete(0,END)
    address.delete(0,END)
    no_of_items.delete(0,END)
    total.delete(0,END)
    
#create query function
def query():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    #query the database 
    c.execute("SELECT*,oid FROM customer")
    records=c.fetchall()
    #print(records)
    print_records=''
    for record in records:
        print_records+=str(record[0])+"  "+"\t"+str(record[1])+"  "+"\t"+str(record[2])+"  "+"\t"+str(record[3])+"  "+"\t"+str(record[4])+"  "+"\t"+str(record[5])+"  "+"\t"+str(record[6])+"\t"+"\n"
        
    query_label=Label(ctable,text=print_records) 
    query_label.grid(row=12,column=0,columnspan=2)
    
    conn.commit()
    conn.close()
    
    



#Text Boxes

c_id=Entry(ctable,width=30)
c_id.grid(row=0,column=1,padx=20,pady=(20,0))

c_name=Entry(ctable,width=30)
c_name.grid(row=1,column=1,pady=(10,0))

contact=Entry(ctable,width=30)
contact.grid(row=2,column=1,pady=(10,0))

address=Entry(ctable,width=30)
address.grid(row=3,column=1,pady=(10,0))

no_of_items=Entry(ctable,width=30)
no_of_items.grid(row=4,column=1,pady=(10,0))

total=Entry(ctable,width=30)
total.grid(row=5,column=1,pady=(10,0))

delete_box=Entry(ctable,width=30)
delete_box.grid(row=9,column=1,pady=(10,0))





#Labels

c_id_label= Label(ctable,text="Customer ID")
c_id_label.grid(row=0,column=0,pady=(20,0))

c_name_label= Label(ctable,text="Customer Name")
c_name_label.grid(row=1,column=0,pady=(10,0))

contact_label= Label(ctable,text="Contact")
contact_label.grid(row=2,column=0,pady=(10,0))

address_label= Label(ctable,text="Address")
address_label.grid(row=3,column=0,pady=(10,0))

no_of_items_label= Label(ctable,text="No. of Items")
no_of_items_label.grid(row=4,column=0,pady=(10,0))

total_label= Label(ctable,text="Total")
total_label.grid(row=5,column=0,pady=(10,0))

del_box_label= Label(ctable,text="Select ID")
del_box_label.grid(row=9,column=0,pady=(10,0))


#Buttons

submit_btn=Button(ctable,text="Add Record to database",command=submit)
submit_btn.grid(row=6,column=0 ,columnspan=2,pady=10,padx=10,ipadx=110)

#Create a query button
query_btn=Button(ctable,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=135)

#CREATE A DELETE BUTTON
del_btn=Button(ctable,text="Delete Record",command=delete)
del_btn.grid(row=10,column=0,columnspan=2,pady=15,padx=10,ipadx=136)

#Create an Update Button
edit_btn=Button(ctable,text="Update Record",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,pady=15,padx=10,ipadx=136)

#create an main page button
mainpage_btn=Button(ctable,text="Back to Main Page",command=mainpage)
mainpage_btn.grid(row=12,column=0,columnspan=2,pady=15,padx=10,ipadx=126)

#create an Product button
p_page_btn=Button(ctable,text="Go To Product Page",command=producttable)
p_page_btn.grid(row=13,column=0,columnspan=2,pady=15,padx=10,ipadx=124)



# c.execute(""" CREATE TABLE customer (
#   c_id int,
#   c_name text,
#   contact integer,
#   address text,
#   no_of_items integer,
#   total integer
#   )""")

conn.commit()
conn.close()

ctable.mainloop()


# In[ ]:




