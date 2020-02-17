from tkinter import *
from ttkthemes import themed_tk as theme
from tkinter.ttk import *
import mysql.connector
import functools

class connect(object):
    def __init__(self,user_name,password,database='None'):
        self.conn_success=0
        try:
            if database=='None':
                self.conn=mysql.connector.connect(host='localhost',user=user_name,passwd=password)
            else:
                self.conn=mysql.connector.connect(host='localhost',user=user_name,passwd=password,database=database)
        except :
            messagebox.showwarning(title='Connection Error',message='Error While connecting to MySql')
        else:
            self.cursor=self.conn.cursor()
            self.conn_success=1
            
    def return_conn_success(self):
        return self.conn_success
                    
    def close_conn(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

class alter_table(object):
    def __init__(self,user_name,password,database,table,root):
        self.root=root
        self.user_name=user_name
        self.password=password
        self.database=database
        self.table=table
        self.Alter_Table_menu=Toplevel()
        self.Alter_Table_menu.title('Alter Table Menu')
        self.Alter_Table_menu.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        self.Alter_Table_menu.geometry('380x580')
        
        self.frame_at=Frame(self.Alter_Table_menu)      #frame_at=table alter table     
        self.frame_at.grid(row=0,column=0)
        
        #Blank Labels for centering widgets
        Label(self.frame_at,text='').grid(row=0,column=0,pady=10,sticky='n')
        Label(self.frame_at,text='').grid(row=1,column=0,sticky='w',padx=30)
        
        #Alter Table Menu Buttons
        Button(self.frame_at,text='Add Column',width=30,command=self.add_column).grid(row=1,column=1,ipady=10,pady=10)
        Button(self.frame_at,text='Delete Column',width=30,command=self.delete_column).grid(row=3,column=1,ipady=10,pady=10)
        Button(self.frame_at,text='Change Column Type',width=30,command=self.modify_column).grid(row=5,column=1,ipady=10,pady=10)
        Button(self.frame_at,text='Rename Column',width=30,command=self.rename_column).grid(row=8,column=1,ipady=10,pady=10)
        Button(self.frame_at,text='Rename Table',width=30,command=self.rename_table).grid(row=11,column=1,ipady=10,pady=10)
        Button(self.frame_at,text='Back',width=30,command=self.back_to_Datamenu).grid(row=13,column=1,ipady=10,pady=10)

   
    def add_column(self):
        def col_add(event):
            col_to_add=ef_add_col.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            try:
                sqlconn.cursor.execute('ALTER TABLE '+self.table+' ADD '+col_to_add)
            except:
                messagebox.showwarning(title='Syntax error',message='Please add datatype with columnname\ne.g.: newcolumn varchar(25)')
            else:
                messagebox.showinfo(title='Added',message='Column added successfully')
                forget(ef=ef_add_col,b=c_ef_add_col)
                sqlconn.close_conn()

        ef_add_col=Entry(self.frame_at,justify=RIGHT,width=30,font='times 12 italic')
        ef_add_col.insert(0,'Column Name with DataType:')
        ef_add_col.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_add_col.get(),e=ef_add_col))
        ef_add_col.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_add_col.get(),e=ef_add_col))
        ef_add_col.bind('<Return>',col_add)
        ef_add_col.grid(row=2,column=1,ipady=5)
        c_ef_add_col=Button(self.frame_at,text='X',width=3,command=lambda:forget(ef=ef_add_col,b=c_ef_add_col))
        c_ef_add_col.grid(row=2,column=2)
        
    def delete_column(self):
        def col_del(event):
            col_to_del=ef_del_col.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            m=messagebox.askquestion(title='Delete Column?',message=col_to_del)
            if m=='yes':
                try:
                    sqlconn.cursor.execute('ALTER TABLE '+self.table+' DROP COLUMN '+col_to_del)
                except:
                    messagebox.showwarning(title='Error',message='Deletion Unsuccessfull\nColumn '+col_to_del+' does not exist')
                else:
                    messagebox.showinfo(title='Deleted',message='Column deleted successfully')
                    forget(ef=ef_del_col,b=c_ef_del_col)
                    sqlconn.close_conn()
        
        ef_del_col=Entry(self.frame_at,justify=RIGHT,width=30,font='times 12 italic')
        ef_del_col.insert(0,'Column Name:')
        ef_del_col.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_del_col.get(),e=ef_del_col))
        ef_del_col.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_del_col.get(),e=ef_del_col))
        ef_del_col.bind('<Return>',col_del)
        ef_del_col.grid(row=4,column=1,ipady=5)
        c_ef_del_col=Button(self.frame_at,text='X',width=3,command=lambda:forget(ef=ef_del_col,b=c_ef_del_col))
        c_ef_del_col.grid(row=4,column=2)
        
    def modify_column(self):
        def col_mod(event):
            col_to_mod=ef_mod_col.get()
            def type_mod(event):
                new_type=ef_mod_type.get()
                sqlconn=connect(self.user_name,self.password,self.database)
                arg='ALTER TABLE '+self.table+' MODIFY COLUMN '+col_to_mod+' '+new_type
                m=messagebox.askquestion(title='Modify?',message='Modify Column '+col_to_mod+'?')
                if m=='yes':
                    try:
                        sqlconn.cursor.execute(arg)
                    except:
                        messagebox.showwarning(title='Error',message='No such column found\nOR\ncheck for syntax error')
                    else:
                        messagebox.showinfo(title='Modified',message='Datatype of Column '+col_to_mod+' modified successfully')
                        forget(ef=ef_mod_type,b=c_ef_mod_type)
                        forget(ef=ef_mod_col,b=c_ef_mod_col)
                        sqlconn.close_conn()
                        
            ef_mod_type=Entry(self.frame_at,justify=RIGHT,width=30,font='times 12 italic')
            ef_mod_type.insert(0,'New Type:')
            ef_mod_type.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_mod_type.get(),e=ef_mod_type))
            ef_mod_type.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_mod_type.get(),e=ef_mod_type))
            ef_mod_type.bind('<Return>',type_mod)
            ef_mod_type.grid(row=7,column=1,ipady=5)
            c_ef_mod_type=Button(self.frame_at,text='X',width=3,command=lambda:forget(ef=ef_mod_type,b=c_ef_mod_type))
            c_ef_mod_type.grid(row=7,column=2)
        
        ef_mod_col=Entry(self.frame_at,justify=RIGHT,width=30,font='times 12 italic')
        ef_mod_col.insert(0,'Column Name:')
        ef_mod_col.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_mod_col.get(),e=ef_mod_col))
        ef_mod_col.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_mod_col.get(),e=ef_mod_col))
        ef_mod_col.bind('<Return>',col_mod)
        ef_mod_col.grid(row=6,column=1,ipady=5)
        c_ef_mod_col=Button(self.frame_at,text='X',width=3,command=lambda:forget(ef=ef_mod_col,b=c_ef_mod_col))
        c_ef_mod_col.grid(row=6,column=2)
        
    def rename_table(self):
        def tb_mod(event):
            new_tb_name=ef_mod_tb.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            arg='RENAME TABLE '+self.table+' TO '+new_tb_name
            m=messagebox.askquestion(title='Rename?',message='Rename Table '+self.table+'?')
            if m=='yes':
                try:
                    sqlconn.cursor.execute(arg)
                except:
                     messagebox.showwarning(title='Error',message='Cannot Rename Table')
                else:
                    messagebox.showinfo(title='Modified',message='Table Renamed successfully')
                    forget(ef=ef_mod_tb,b=c_ef_mod_tb)
                    sqlconn.close_conn()
               
        ef_mod_tb=Entry(self.frame_at,justify=RIGHT,width=30,font='times 12 italic')
        ef_mod_tb.insert(0,'New Name:')
        ef_mod_tb.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_mod_tb.get(),e=ef_mod_tb))
        ef_mod_tb.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_mod_tb.get(),e=ef_mod_tb))
        ef_mod_tb.bind('<Return>',tb_mod)
        ef_mod_tb.grid(row=12,column=1,ipady=5)
        c_ef_mod_tb=Button(self.frame_at,text='X',width=3,command=lambda:forget(ef=ef_mod_tb,b=c_ef_mod_tb))
        c_ef_mod_tb.grid(row=12,column=2)
        
    def rename_column(self):
        def col_old(event):
            old_col_name=ef_old_col.get()
            def col_mod(event):
                new_col_name=ef_mod_col.get()
                sqlconn=connect(self.user_name,self.password,self.database)
                arg='ALTER TABLE '+self.table+' RENAME COLUMN '+old_col_name+' TO '+new_col_name
                m=messagebox.askquestion(title='Rename?',message='Rename column '+old_col_name+' to '+new_col_name+'?')
                if m=='yes':
                     try:
                          sqlconn.cursor.execute(arg)
                     except:
                          messagebox.showwarning(title='Error',message='Cannot Rename Column')
                     else:
                         messagebox.showinfo(title='Modified',message='Column Renamed successfully')
                         forget(ef=ef_mod_col,b=c_ef_mod_col)
                         forget(ef=ef_old_col,b=c_ef_old_col)
                         sqlconn.close_conn()
                   
            ef_mod_col=Entry(self.frame_at,justify=RIGHT,width=30,font='times 12 italic')
            ef_mod_col.insert(0,'New Column Name:')
            ef_mod_col.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_mod_col.get(),e=ef_mod_col))
            ef_mod_col.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_mod_col.get(),e=ef_mod_col))
            ef_mod_col.bind('<Return>',col_mod)
            ef_mod_col.grid(row=10,column=1,ipady=5)
            c_ef_mod_col=Button(self.frame_at,text='X',width=3,command=lambda:forget(ef=ef_mod_col,b=c_ef_mod_col))
            c_ef_mod_col.grid(row=10,column=2)
            
        ef_old_col=Entry(self.frame_at,justify=RIGHT,width=30,font='times 12 italic')
        ef_old_col.insert(0,'Old Column Name:')
        ef_old_col.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_old_col.get(),e=ef_old_col))
        ef_old_col.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_old_col.get(),e=ef_old_col))
        ef_old_col.bind('<Return>',col_old)
        ef_old_col.grid(row=9,column=1,ipady=5)
        c_ef_old_col=Button(self.frame_at,text='X',width=3,command=lambda:forget(ef=ef_old_col,b=c_ef_old_col))
        c_ef_old_col.grid(row=9,column=2)
        
        
    def back_to_Datamenu(self):
        self.Alter_Table_menu.destroy()
        Datamenu_back=data(self.user_name,self.password,self.database,self.table,self.root)
       
class data(object):
    def __init__(self,user_name,password,database,table,root):
        self.root=root
        self.user_name=user_name
        self.password=password
        self.database=database
        self.table=table
        self.Datamenu=Toplevel()
        self.Datamenu.title('Data Menu')
        self.Datamenu.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        self.Datamenu.geometry('380x580')
        
        self.frame_data=Frame(self.Datamenu)           
        self.frame_data.grid(row=0,column=0)
        
        #Blank Labels for centering widgets
        Label(self.frame_data,text='').grid(row=0,column=0,pady=5,sticky='n')
        Label(self.frame_data,text='').grid(row=1,column=0,sticky='w',padx=30)
        
        #Data Menu Buttons
        Button(self.frame_data,text='Update Table',width=30,command=self.update_table).grid(row=1,column=1,ipady=10,pady=10)
        Button(self.frame_data,text='Add Record',width=30,command=self.add_data).grid(row=2,column=1,ipady=10,pady=10)
        Button(self.frame_data,text='Show Records',width=30,command=self.show_data).grid(row=5,column=1,ipady=10,pady=10)
        Button(self.frame_data,text='Update Record',width=30,command=self.update_data).grid(row=6,column=1,ipady=10,pady=10)
        Button(self.frame_data,text='Delete Record',width=30,command=self.delete_data).grid(row=10,column=1,ipady=10,pady=10)
        Button(self.frame_data,text='Back',width=30,command=self.back_to_TBmenu).grid(row=12,column=1,ipady=10,pady=10)

        
    def add_data(self):
        def setcol_name(event):
            col_name=ef_add_col_name.get()
            def set_data(event):
                data=ef_add_data.get()
                sqlconn=connect(self.user_name,self.password,self.database)
                arg='INSERT INTO '+self.table+'('+col_name+') VALUES ('+data+');'
                try:
                    sqlconn.cursor.execute(arg)
                except:
                    messagebox.showwarning(title='Error',message='Unknown Column name')
                else:
                    messagebox.showinfo(title='Added',message='Record added successfully')
                    forget(ef=ef_add_data,b=c_ef_add_data)
                    forget(ef=ef_add_data,b=c_ef_add_data)
                    sqlconn.close_conn()
                    
            ef_add_data=Entry(self.frame_data,width=30,justify=LEFT,font='times 12 italic')
            ef_add_data.insert(0,'Data:(each value in quotes)')
            ef_add_data.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_add_data.get(),e=ef_add_data))
            ef_add_data.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_add_data.get(),e=ef_add_data))
            ef_add_data.bind('<Return>',set_data)
            ef_add_data.grid(row=4,column=1,ipady=5)
            c_ef_add_data=Button(self.frame_data,text='X',width=3,command=lambda:forget(ef=ef_add_data,b=c_ef_add_data))
            c_ef_add_data.grid(row=4,column=2)
    
        ef_add_col_name=Entry(self.frame_data,width=30,justify=LEFT,font='times 12 italic')
        ef_add_col_name.insert(0,'Column Names:')
        ef_add_col_name.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_add_col_name.get(),e=ef_add_col_name))
        ef_add_col_name.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_add_col_name.get(),e=ef_add_col_name))
        ef_add_col_name.bind('<Return>',setcol_name)
        ef_add_col_name.grid(row=3,column=1,ipady=5)
        c_ef_add_col_name=Button(self.frame_data,text='X',width=3,command=lambda:forget(ef=ef_add_col_name,b=c_ef_add_col_name))
        c_ef_add_col_name.grid(row=3,column=2)
        
    def show_data(self):
        top=Toplevel()
        top.title('Recorded Data')
        top.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        
        sqlconn=connect(self.user_name,self.password,self.database)
        sqlconn.cursor.execute('SELECT * FROM '+self.table)
        records=sqlconn.cursor.fetchall()
        
        sqlconn.cursor.execute('SHOW COLUMNS FROM '+self.table )
        column_names=sqlconn.cursor.fetchall()

        c=0
        for col in range(len(records[0])):
            Label(top,text=column_names[col][0]+'\t').grid(row=0,column=c)
            c=c+1
            
        r=1
        for r_c in range(len(records)):
            c=0
            for r_r in range(len(records[0])):
                Label(top,text=str(records[r_c][r_r])+'\t').grid(row=r,column=c)
                c=c+1
            r=r+1
        sqlconn.close_conn()
        
    def update_data(self):
        def updt(event):
            v_id=ef_updata_vid.get()
            def up_col(event):
                col_up=ef_up_colname.get()
                def up_val(event):
                    newv=ef_new_val.get()
                    sqlconn=connect(self.user_name,self.password,self.database)
                    try:
                        sqlconn.cursor.execute('UPDATE '+self.table+' SET '+col_up+'= \''+newv+'\' WHERE virtual_id='+v_id)
                    except:
                        messagebox.showwarning(title='Error',message='Column '+col_up+' does not exist\nOr is immutable.')
                    else:
                        messagebox.showinfo(title='Updated',message='Record Updated successfully')
                        forget(ef=ef_new_val,b=c_ef_new_val)
                        forget(ef=ef_up_colname,b=c_ef_up_colname)
                        forget(ef=ef_updata_vid,b=c_ef_updata_vid)
                        sqlconn.close_conn()
    
                ef_new_val=Entry(self.frame_data,justify=RIGHT,width=30,font='times 12 italic')
                ef_new_val.insert(0,'New Value:')
                ef_new_val.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_new_val.get(),e=ef_new_val))
                ef_new_val.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_new_val.get(),e=ef_new_val))
                ef_new_val.bind('<Return>',up_val)
                ef_new_val.grid(row=9,column=1,ipady=5)
                c_ef_new_val=Button(self.frame_data,text='X',width=3,command=lambda:forget(ef=ef_new_val,b=c_ef_new_val))
                c_ef_new_val.grid(row=9,column=2)
            
            ef_up_colname=Entry(self.frame_data,justify=RIGHT,width=30,font='times 12 italic')
            ef_up_colname.insert(0,'Column Name:')
            ef_up_colname.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_up_colname.get(),e=ef_up_colname))
            ef_up_colname.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_up_colname.get(),e=ef_up_colname))
            ef_up_colname.bind('<Return>',up_col)
            ef_up_colname.grid(row=8,column=1,ipady=5)
            c_ef_up_colname=Button(self.frame_data,text='X',width=3,command=lambda:forget(ef=ef_up_colname,b=c_ef_up_colname))
            c_ef_up_colname.grid(row=7,column=2)
    
        ef_updata_vid=Entry(self.frame_data,justify=RIGHT,width=30,font='times 12 italic')
        ef_updata_vid.insert(0,'Virtual id:')
        ef_updata_vid.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_updata_vid.get(),e=ef_updata_vid))
        ef_updata_vid.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_updata_vid.get(),e=ef_updata_vid))
        ef_updata_vid.bind('<Return>',updt)
        ef_updata_vid.grid(row=7,column=1,ipady=5)
        c_ef_updata_vid=Button(self.frame_data,text='X',width=3,command=lambda:forget(ef=ef_updata_vid,b=c_ef_updata_vid))
        c_ef_updata_vid.grid(row=7,column=2)
    
    def delete_data(self):
        def d_data(event):
            v_id=ef_delete_data.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            try:
                sqlconn.cursor.execute('SELECT * FROM '+self.table+' WHERE virtual_id='+v_id)
            except:
                messagebox.showwarning(title='Error',message='No such record found')
            else:
                record=sqlconn.cursor.fetchone()
                m=messagebox.askquestion(title='Delete record?',message=record)
                if m=='yes':    
                    arg='DELETE FROM '+self.table+' WHERE virtual_id='+v_id
                    sqlconn.cursor.execute(arg)
                    messagebox.showinfo(title='Deleted',message='Record Deleted successfully')
                    forget(ef=ef_delete_data,b=c_ef_delete_data)
                    sqlconn.close_conn()
            
        ef_delete_data=Entry(self.frame_data,justify=RIGHT,width=30,font='times 12 italic')
        ef_delete_data.insert(0,'Virtual_id')
        ef_delete_data.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_delete_data.get(),e=ef_delete_data))
        ef_delete_data.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_delete_data.get(),e=ef_delete_data))
        ef_delete_data.bind('<Return>',d_data)
        ef_delete_data.grid(row=11,column=1,ipady=5)
        c_ef_delete_data=Button(self.frame_data,text='X',width=3,command=lambda:forget(ef=ef_delete_data,b=c_ef_delete_data))
        c_ef_delete_data.grid(row=11,column=2)
        
    def update_table(self):
        self.Datamenu.destroy()
        Alter_Table=alter_table(self.user_name,self.password,self.database,self.table,self.root)
        
    def back_to_TBmenu(self):
        self.Datamenu.destroy()
        Tablemenu_back=Table(self.user_name,self.password,self.database,self.root)

        

class Table(object):
    def __init__(self,user_name,password,database,root):
        self.root=root
        self.user_name=user_name
        self.password=password
        self.database=database
        self.TBmenu=Toplevel()
        self.TBmenu.title('Table Menu')
        self.TBmenu.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        self.TBmenu.geometry('380x580')
        
        self.frame_t=Frame(self.TBmenu)           #frame_t=table frame
        self.frame_t.grid(row=0,column=0)
        
        #Blank Labels for centering widgets
        Label(self.frame_t,text='').grid(row=0,column=0,pady=5,sticky='n')
        Label(self.frame_t,text='').grid(row=1,column=0,sticky='w',padx=30)
        
        #Table Menu Buttons
        Button(self.frame_t,text='Create Table',width=30,command=self.create_t).grid(row=1,column=1,ipady=10,pady=10)
        Button(self.frame_t,text='Show Table',width=30,command=self.show_t).grid(row=3,column=1,ipady=10,pady=10)
        Button(self.frame_t,text='Choose Table',width=30,command=self.choose_t).grid(row=4,column=1,ipady=10,pady=10)
        Button(self.frame_t,text='Delete Table',width=30,command=self.delete_t).grid(row=6,column=1,ipady=10,pady=10)
        Button(self.frame_t,text='Perform Querry',width=30,command=self.perform_querry).grid(row=8,column=1,ipady=10,pady=10)
        Button(self.frame_t,text='Back',width=30,command=self.back_to_dbmenu).grid(row=9,column=1,ipady=10,pady=10)

        
    def create_t(self):
        def new_t(event):
            table=ef_create_t.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            arg='CREATE TABLE '+table+'(virtual_id int NOT NULL AUTO_INCREMENT PRIMARY KEY )'
            try:
                sqlconn.cursor.execute(arg)
            except:
                messagebox.showwarning(title='Cannot create',message='Table '+table+' already exists')
            else:
                messagebox.showinfo(title='Created',message='Table \''+table+'\' created successfully')
                forget(ef=ef_create_t,b=c_ef_create_t)
                sqlconn.close_conn()
                
        ef_create_t=Entry(self.frame_t,width=30,justify=RIGHT,font='times 12 italic')
        ef_create_t.insert(0,'Table Name:')
        ef_create_t.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_create_t.get(),e=ef_create_t))
        ef_create_t.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_create_t.get(),e=ef_create_t))
        ef_create_t.bind('<Return>',new_t)
        ef_create_t.grid(row=2,column=1,ipady=5)
        c_ef_create_t=Button(self.frame_t,text='X',width=3,command=lambda:forget(ef=ef_create_t,b=c_ef_create_t))
        c_ef_create_t.grid(row=2,column=2)
    
    def show_t(self):
        top=Toplevel()
        top.title('Tables In Database '+self.database)
        top.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        
        sqlconn=connect(self.user_name,self.password,self.database)
        sqlconn.cursor.execute('SHOW TABLES')
        
        Label(top,text='').grid(row=0,column=0,pady=10,sticky='n')
        Label(top,text='').grid(row=1,column=0,sticky='w',padx=30)
        Label(top,text='').grid(row=1,column=2,sticky='e',padx=30)
        
        r=1
        for tab in sqlconn.cursor:
            Label(top,text=tab,font=('courier', 13,'')).grid(row=r,column=1)
            r=r+1
            
        Label(top,text='').grid(row=r+1,column=0,pady=10,sticky='s')
        sqlconn.close_conn()
        
    def delete_t(self):
        def delt_t(event):
            deltb=ef_delete_t.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            m=messagebox.askquestion(title='Delete?',message='Delete Table '+deltb+'?')
            if m=='yes':
                 try:
                     sqlconn.cursor.execute('DROP TABLE '+ deltb)
                 except:
                     messagebox.showwarning(title='Error',message='Cannot Delete\nTable '+deltb+' Does not exist')
                 else:
                     messagebox.showinfo(title='Deleted',message='Table \''+deltb+'\' deleted successfully')
                     forget(ef=ef_delete_t,b=c_ef_delete_t)
                     sqlconn.close_conn()
    
        ef_delete_t=Entry(self.frame_t,width=30,justify=RIGHT,font='times 12 italic')
        ef_delete_t.insert(0,'Table Name:')
        ef_delete_t.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_delete_t.get(),e=ef_delete_t))
        ef_delete_t.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_delete_t.get(),e=ef_delete_t))
        ef_delete_t.bind('<Return>',delt_t)
        ef_delete_t.grid(row=7,column=1,ipady=5)
        c_ef_delete_t=Button(self.frame_t,text='X',width=3,command=lambda:forget(ef=ef_delete_t,b=c_ef_delete_t))
        c_ef_delete_t.grid(row=7,column=2)
        
    def choose_t(self):
        def chosen_t(event):
            t_choosing_success=-1
            table=ef_choose_t.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            sqlconn.cursor.execute('SHOW TABLES')
            for tab in sqlconn.cursor:
                if tab[0]==table:
                    t_choosing_success=1
                    break
                
            if t_choosing_success==1:
                self.TBmenu.destroy()
                Datamenu=data(self.user_name,self.password,self.database,table,self.root)
            else:
                messagebox.showwarning(title='Error',message='Table \''+table+'\' does not exist')
        
        ef_choose_t=Entry(self.frame_t,width=30,justify=RIGHT,font='times 12 italic')
        ef_choose_t.insert(0,'Table Name:')
        ef_choose_t.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_choose_t.get(),e=ef_choose_t))
        ef_choose_t.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_choose_t.get(),e=ef_choose_t))
        ef_choose_t.bind('<Return>',chosen_t)
        ef_choose_t.grid(row=5,column=1,ipady=5)
        c_ef_choose_t=Button(self.frame_t,text='X',width=3,command=lambda:forget(ef=ef_choose_t,b=c_ef_choose_t))
        c_ef_choose_t.grid(row=5,column=2)
        
    def perform_querry(self):
        top=Toplevel()
        top.title('Perform Querry')
        top.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        
        def execq():
            arg=ef_pq.get()
            sqlconn=connect(self.user_name,self.password,self.database)
            try:
                sqlconn.cursor.execute(arg)
            except:
                messagebox.showwarning(title='Error',message='Querry cannot be executed,\ncheck for syntax errors')
            else:
                q_results=sqlconn.cursor.fetchall()
                Label(top,text='').grid(row=0,column=0,pady=10,sticky='n')
                Label(top,text='').grid(row=1,column=0,sticky='w',padx=30)
                Label(top,text='').grid(row=1,column=2,sticky='e',padx=30)
                r=3
                for res in q_results:
                    Label(top,text=res,font=('courier', 13,'')).grid(row=r,column=1)
                    r=r+1
                Label(top,text='').grid(row=r+1,column=0,pady=10,sticky='s')
                forget(ef=ef_pq,b=ef_pq_b)
            
        ef_pq=Entry(top,width=30,font='times 12 italic',justify=LEFT)
        ef_pq.insert(0,'Querry:')
        ef_pq.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_pq.get(),e=ef_pq))
        ef_pq.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_pq.get(),e=ef_pq))
        ef_pq.grid(row=1,column=1,ipady=20)
        ef_pq_b=Button(top,text='Execute',width=30,style='TButton',command=execq)
        ef_pq_b.grid(row=2,column=1)
        
    def back_to_dbmenu(self):
        self.TBmenu.destroy()
        DatabaseMenu_back=DBman(self.user_name,self.password,self.root)
        
    
class DBman(object):
    def __init__(self,user_name,password,root):
        self.root=root
        self.user_name=user_name
        self.password=password
        self.DBmenu=Toplevel()
        self.DBmenu.title('Database Main Menu')
        self.DBmenu.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        self.DBmenu.geometry('380x520')
        
        self.frame_d=Frame(self.DBmenu)           #frame_d=database frame
        self.frame_d.grid(row=0,column=0)
        
        #Blank Labels for centering widgets
        Label(self.frame_d,text='').grid(row=0,column=0,pady=5,sticky='n')
        Label(self.frame_d,text='').grid(row=1,column=0,sticky='w',padx=30)
        
        #Database Menu Buttons
        Button(self.frame_d,text='Create DataBase',width=30,command=self.create_d).grid(row=1,column=1,ipady=10,pady=10)
        Button(self.frame_d,text='Show Databases',width=30,command=self.show_d).grid(row=3,column=1,ipady=10,pady=10)
        Button(self.frame_d,text='Choose Database',width=30,command=self.choose_d).grid(row=4,column=1,ipady=10,pady=10)
        Button(self.frame_d,text='Delete Database',width=30,command=self.delete_d).grid(row=6,column=1,ipady=10,pady=10)
        Button(self.frame_d,text='Back',width=30,command=self.back_to_login).grid(row=8,column=1,ipady=10,pady=10)


    def create_d(self):
        def new_d(event): 
            database=ef_create_d.get()
            sqlconn=connect(self.user_name,self.password)
            try:
                sqlconn.cursor.execute('CREATE DATABASE '+ database)
            except:
                messagebox.showwarning(title='Error',message='Cannot Create\nDatabase \''+database+'\' already exists')
            else:
                messagebox.showinfo(title='Created',message='Database \''+database+'\' created successfully')
                forget(ef=ef_create_d,b=c_ef_create_d)
                sqlconn.close_conn()

        ef_create_d=Entry(self.frame_d,width=30,justify=RIGHT,font='times 12 italic')
        ef_create_d.insert(0,'Database Name:')
        ef_create_d.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_create_d.get(),e=ef_create_d))
        ef_create_d.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_create_d.get(),e=ef_create_d))
        ef_create_d.bind('<Return>',new_d)
        ef_create_d.grid(row=2,column=1,ipady=5)
        c_ef_create_d=ttk.Button(self.frame_d,text='X',width=3,command=lambda:forget(ef=ef_create_d,b=c_ef_create_d))
        c_ef_create_d.grid(row=2,column=2)
        
    def show_d(self):
        top=Toplevel()
        top.title('Created Databases')
        top.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        
        sqlconn=connect(self.user_name,self.password)
        sqlconn.cursor.execute('SHOW DATABASES')
        
        Label(top,text='').grid(row=0,column=0,pady=10,sticky='n')
        Label(top,text='').grid(row=1,column=0,sticky='w',padx=30)
        Label(top,text='').grid(row=1,column=2,sticky='e',padx=30)
        
        r=1
        for db in sqlconn.cursor:
            Label(top,text=db,font=('courier', 13,'')).grid(row=r,column=1)
            r=r+1
            
        Label(top,text='').grid(row=r+1,column=0,pady=10,sticky='s')
        sqlconn.close_conn()
        
    def delete_d(self):
        def delt_d(event):
            deldb=ef_delete_d.get()
            sqlconn=connect(self.user_name,self.password)
            m=messagebox.askquestion(title='Delete?',message='Delete Database '+deldb+'?')
            if m=='yes':
                try:
                    sqlconn.cursor.execute('DROP DATABASE '+ deldb)
                except:
                    messagebox.showwarning(title='Error',message='Cannot Delete\nDatabase \''+deldb+'\' does not exist')
                else:
                    messagebox.showinfo(title='Deleted',message='Successfully deleted Database \''+deldb+'\'')
                    forget(ef=ef_delete_d,b=c_ef_delete_d)
                    sqlconn.close_conn()
    
        ef_delete_d=Entry(self.frame_d,width=30,justify=RIGHT,font='times 12 italic')
        ef_delete_d.insert(0,'Database Name:')
        ef_delete_d.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_delete_d.get(),e=ef_delete_d))
        ef_delete_d.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_delete_d.get(),e=ef_delete_d))
        ef_delete_d.bind('<Return>',delt_d)
        ef_delete_d.grid(row=7,column=1,ipady=5)
        c_ef_delete_d=Button(self.frame_d,text='X',width=3,command=lambda:forget(ef=ef_delete_d,b=c_ef_delete_d))
        c_ef_delete_d.grid(row=7,column=2)
        
    def choose_d(self):
        def chosen_d(event):
            database=ef_choose_d.get()
            sqlconn=connect(self.user_name,self.password,database)
            chosing_success=sqlconn.return_conn_success()
            if chosing_success==1:
                self.DBmenu.destroy()
                Tablemenu=Table(self.user_name,self.password,database,self.root)
            else:
                messagebox.showwarning(title='Error',message='Database \''+database+'\' does not exist')

                
        ef_choose_d=Entry(self.frame_d,width=30,justify=RIGHT,font='times 12 italic')
        ef_choose_d.insert(0,'Database Name:')
        ef_choose_d.bind('<ButtonRelease-1>',functools.partial(on_click,arg=ef_choose_d.get(),e=ef_choose_d))
        ef_choose_d.bind('<FocusOut>',functools.partial(on_focus_out,arg=ef_choose_d.get(),e=ef_choose_d))
        ef_choose_d.bind('<Return>',chosen_d)
        ef_choose_d.grid(row=5,column=1,ipady=5)
        c_ef_choose_d=Button(self.frame_d,text='X',width=3,command=lambda:forget(ef=ef_choose_d,b=c_ef_choose_d))
        c_ef_choose_d.grid(row=5,column=2)
        
    def back_to_login(self):
        self.DBmenu.destroy()
        user_back=login(self.root)
        
class login(object):
    def __init__(self,root):
        self.root=root
        self.login_window=Toplevel()
        self.login_window.title('Database Creater and Manager')
        self.login_window.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
        
        frame_r=Frame(self.login_window)           #frame_r=root frame
        frame_r.grid(row=0,column=0)
        
        #Blank Labels for centering widgets
        Label(frame_r,text='').grid(row=0,column=0,pady=10,sticky='n')
        Label(frame_r,text='').grid(row=1,column=0,sticky='w',padx=30)
        Label(frame_r,text='').grid(row=1,column=3,sticky='e',padx=30)
        Label(frame_r,text='').grid(row=6,column=0,sticky='s',pady=10)
        
        User_label=Label(frame_r,text='UserName:',font='times 14 ',width=15,justify=RIGHT).grid(row=1,column=1,columnspan=2,sticky='w',pady=5)
        Pswd_label=Label(frame_r,text='Password:',font='times 14 ',width=15,justify=RIGHT).grid(row=3,column=1,columnspan=2,sticky='w',pady=5)
        
        self.User=Entry(frame_r,width=35,font='times 14 italic',justify=LEFT)
        self.User.grid(row=2,column=1,ipady=20,columnspan=2)
        self.pswrd=Entry(frame_r,width=35,show='*',font='times 14 italic',justify=LEFT)
        self.pswrd.grid(row=4,column=1,ipady=20,columnspan=2)
   
        Connect_button=Button(frame_r,text='Connect',width=15,command=self.log_in).grid(row=5,column=1,pady=10)
        Exit_button=Button(frame_r,text='Exit',width=15,command=self.Exit).grid(row=5,column=2,pady=10,padx=5)
        
    def log_in(self):
        user_name=self.User.get()
        password=self.pswrd.get()
        sqlconn=connect(user_name,password)
        success=sqlconn.return_conn_success()
        if success==1:
            messagebox.showinfo(title='Connected',message='Connection Succesful')
            self.login_window.destroy()
            DatabaseMenu=DBman(user_name,password,self.root)
        
    def Exit(self):
        self.root.destroy()
       
def chronology(root):    #because object gets redefined everytime mainloop() is run, so use function tp define itobly once
        user=login(root)
   
if __name__ == '__main__':
    def on_click(event,arg,e):
        if e.get() == arg:
            e.delete(0, "end") 
            e.insert(0, '')
        
    def on_focus_out(event,arg,e):
        if e.get() == '':
            e.insert(0, arg)
        
    def forget(ef,b):
        ef.grid_forget()
        b.grid_forget()
 
    root=theme.ThemedTk()
    root.get_themes()
    root.set_theme('arc')
    root.title('Database Creater and Manager')
    root.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\project database\icon.ico')
    root.geometry('10x10')
    root.withdraw()

    s=Style()
    s.configure('TButton',font=('times',12,''))
    chronology(root)
    root.mainloop()