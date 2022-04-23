#!/usr/bin/env python
# coding: utf-8

# In[10]:


from tkinter import*
import sqlite3

root=Tk()
root.title('Product Table')
root.geometry("500x700")
#Background colour
root['bg']='#FFFAF0'
#Creating/Accesing a Database
conn=sqlite3.connect('garment_retail.db')

c=conn.cursor()
#Creating a function to go to main page

def mainpage():
 root.destroy()
 import mainpage
    
#Creating a function to go to customer table 

def customertable():
 root.destroy()
 import customertable

#creating an update function
def update():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute(""" UPDATE product SET
    pr_id=:pr_id,
    product=:product,
    vendor=:vendor,
    stock=:stock, 
    cp_price=:cp, 
    sp_price=:sp
    
    WHERE oid=:oid""",
    {
        'pr_id':pr_id_edit.get(),
        'product':product_edit.get(),
        'vendor':vendor_edit.get(),
        'stock':stock_edit.get(),
        'cp':cp_price_edit.get(),
        'sp':sp_price_edit.get(),
        'oid':record_id
        
    }

    )
    conn.commit()
    conn.close()
    editor.destroy()
    
    

def edit():
 global editor   
 #Create edit function to update
 editor=Tk()
 editor.title('Update a Record')
 editor.geometry("500x700")
 editor['bg']='#FFFAF0'
    
 conn=sqlite3.connect('garment_retail.db')
 c=conn.cursor()
 #query the database 
 record_id=delete_box.get()
 c.execute("SELECT*FROM product where oid = " + record_id)
 records=c.fetchall()
 #create global variables 
 global pr_id_edit
 global product_edit
 global vendor_edit
 global stock_edit
 global cp_price_edit
 global sp_price_edit
                        
 #Text Boxes
 pr_id_edit=Entry(editor,width=30)
 pr_id_edit.grid(row=0,column=1,padx=20,pady=(20,0))

 product_edit=Entry(editor,width=30)
 product_edit.grid(row=1,column=1,pady=(10,0))

 vendor_edit=Entry(editor,width=30)
 vendor_edit.grid(row=2,column=1,pady=(10,0))

 stock_edit=Entry(editor,width=30)
 stock_edit.grid(row=3,column=1,pady=(10,0))

 cp_price_edit=Entry(editor,width=30)
 cp_price_edit.grid(row=4,column=1,pady=(10,0))

 sp_price_edit=Entry(editor,width=30)
 sp_price_edit.grid(row=5,column=1,pady=(10,0))

 


#Labels

 pr_id_label= Label(editor,text="Product ID")
 pr_id_label.grid(row=0,column=0,pady=(20,0))

 product_label= Label(editor,text="Product")
 product_label.grid(row=1,column=0,pady=(10,0))

 vendor_label= Label(editor,text="Vendor")
 vendor_label.grid(row=2,column=0,pady=(10,0))

 stock_label= Label(editor,text="Stock")
 stock_label.grid(row=3,column=0,pady=(10,0))

 cp_price_label= Label(editor,text="Cost Price")
 cp_price_label.grid(row=4,column=0,pady=(10,0))

 sp_price_label= Label(editor,text="Sales Price")
 sp_price_label.grid(row=5,column=0,pady=(10,0))
 


 for record in records:
    pr_id_edit.insert(0,record[0])
    product_edit.insert(0,record[1])
    vendor_edit.insert(0,record[2])
    stock_edit.insert(0,record[3])
    cp_price_edit.insert(0,record[4])
    sp_price_edit.insert(0,record[5])
    
 #Create an Save Button
 save_btn=Button(editor,text="Save Record",command=update)
 save_btn.grid(row=6,column=0,columnspan=2,pady=15,padx=10,ipadx=145)

 


 



 # Create Function to delete a record
def delete():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    #Delete a record
    c.execute("DELETE FROM product WHERE oid="+  delete_box.get())
    conn.commit()
    conn.close()

#Create Submit Function for database
def submit():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    #Insert into table
    c.execute("INSERT INTO product VALUES (:pr_id,:product,:vendor,:stock,:cp_price,:sp_price)",
               {
                 'pr_id':pr_id.get(),
                 'product':product.get(),
                 'vendor':vendor.get(),
                 'stock':stock.get(),
                 'cp_price':cp_price.get(),
                 'sp_price':sp_price.get()
                })

    conn.commit()
    conn.close()
    

    #clear the text boxes
    pr_id.delete(0,END)
    product.delete(0,END)
    vendor.delete(0,END)
    stock.delete(0,END)
    cp_price.delete(0,END)
    sp_price.delete(0,END)
    
#create query function
def query():
    conn=sqlite3.connect('garment_retail.db')
    c=conn.cursor()
    #query the database 
    c.execute("SELECT*,oid FROM product")
    records=c.fetchall()
    #print(records)
    print_records=''
    for record in records:
        print_records+=str(record[0])+"  "+"\t"+str(record[1])+"  "+"\t"+str(record[2])+"  "+"\t"+str(record[3])+"  "+"\t"+str(record[4])+"  "+"\t"+str(record[5])+"  "+"\t"+str(record[6])+"\t"+"\n"
        
    query_label=Label(root,text=print_records) 
    query_label.grid(row=12,column=0,columnspan=2)
    
    conn.commit()
    conn.close()
    
    



#Text Boxes

pr_id=Entry(root,width=30)
pr_id.grid(row=0,column=1,padx=20,pady=(20,0))

product=Entry(root,width=30)
product.grid(row=1,column=1,pady=(10,0))

vendor=Entry(root,width=30)
vendor.grid(row=2,column=1,pady=(10,0))

stock=Entry(root,width=30)
stock.grid(row=3,column=1,pady=(10,0))

cp_price=Entry(root,width=30)
cp_price.grid(row=4,column=1,pady=(10,0))

sp_price=Entry(root,width=30)
sp_price.grid(row=5,column=1,pady=(10,0))

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=(10,0))





#Labels

pr_id_label= Label(root,text="Product ID")
pr_id_label.grid(row=0,column=0,pady=(20,0))

product_label= Label(root,text="Product")
product_label.grid(row=1,column=0,pady=(10,0))

vendor_label= Label(root,text="Vendor")
vendor_label.grid(row=2,column=0,pady=(10,0))

stock_label= Label(root,text="Stock")
stock_label.grid(row=3,column=0,pady=(10,0))

cp_price_label= Label(root,text="Cost Price")
cp_price_label.grid(row=4,column=0,pady=(10,0))

sp_price_label= Label(root,text="Sales Price")
sp_price_label.grid(row=5,column=0,pady=(10,0))

del_box_label= Label(root,text="Select ID")
del_box_label.grid(row=9,column=0,pady=(10,0))


#Buttons

submit_btn=Button(root,text="Add Record to database",command=submit)
submit_btn.grid(row=6,column=0 ,columnspan=2,pady=10,padx=10,ipadx=110)

#Create a query button
query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=135)

#CREATE A DELETE BUTTON
del_btn=Button(root,text="Delete Record",command=delete)
del_btn.grid(row=10,column=0,columnspan=2,pady=15,padx=10,ipadx=136)

#Create an Update Button
edit_btn=Button(root,text="Update Record",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,pady=15,padx=10,ipadx=136)

#create an main page button
mainpage_btn=Button(root,text="Back to Main Page",command=mainpage)
mainpage_btn.grid(row=12,column=0,columnspan=2,pady=15,padx=10,ipadx=128)

#create an Customer button
c_page_btn=Button(root,text="Go To Customer Page",command=customertable)
c_page_btn.grid(row=13,column=0,columnspan=2,pady=15,padx=10,ipadx=120)



# c.execute(""" CREATE TABLE product (
#   pr_id int PRIMARY KEY,
#   product text,
#   vendor text,
#   stock integer,
#   cp_price integer,
#   sp_price integer
#   )""")

conn.commit()
conn.close()

root.mainloop()


# In[ ]:




