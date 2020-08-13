import tkinter as tk
from tkinter import*
import tkinter.messagebox as tm
from tkinter import ttk
from tkinter import Text, Tk



class recreate(tk.Tk):

    def __init__(self):     
        
        tk.Tk.__init__(self)       

        tk.Tk.iconbitmap(self,default="1.ico")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14,fig15,fig16,fig17,fig18,fig19):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(fig1)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

   
        

class fig1(tk.Frame):
    def __init__(self, parent, controller):
      
        tk.Frame.__init__(self,parent)
        label0=tk.Label(self, text="_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-").pack()
        label0=tk.Label(self, text="_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-").pack()
   
        label = tk.Label(self, text="Welcome !", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label1 = tk.Label(self, text="Re-create is an application software", font=('arial',14),justify=CENTER)
        label1.pack(pady=20,padx=20)
        label2 = tk.Label(self, text="Click the button below to begin..", font=('arial',12),justify=CENTER).pack()
        button1=ttk.Button(self,text="BEGIN" ,
                          command=lambda : controller.show_frame(fig2))
        button1.pack(pady=10,padx=500)  
        label0=tk.Label(self, text="_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-").pack()
        label0=tk.Label(self, text="_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-").pack()
        
        
class fig2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please Select any one :", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        button1=ttk.Button(self,text="Formal" ,
                          command=lambda:controller.show_frame(fig3))
        button1.pack(pady=10,padx=10)
        button2=ttk.Button(self,text="Informal" ,
                          command=lambda:controller.show_frame(fig4))
        button2.pack(pady=10,padx=10)
        button9=ttk.Button(self,text="Query-Reply " ,
                          command=lambda:controller.show_frame(fig19))
        button9.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()

        
        label2 = tk.Label(self, text="For Advanced User ( Institute/Organization) : ", font=('arial',12)).pack()

        
        button4=ttk.Button(self,text="Sign-up" ,
                          command=lambda:controller.show_frame(fig8))
        button4.pack(pady=10,padx=10)
        button5=ttk.Button(self,text="Log-in" ,
                          command=lambda:controller.show_frame(fig6))
        button5.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()

        button5=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig1))
        button5.pack(pady=10,padx=10)

        
        

class fig3(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please Select any one :", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()

        button1=ttk.Button(self,text="Primary Level" ,
                          command=lambda:controller.show_frame(fig12))
        button1.pack(pady=10,padx=10)
        button2=ttk.Button(self,text="Secondary Level" ,
                          command=lambda:controller.show_frame(fig13))
        button2.pack(pady=10,padx=10)
        button3=ttk.Button(self,text="Higher Secondary Level" ,
                          command=lambda:controller.show_frame(fig14))
        button3.pack(pady=10,padx=10)
        button4=ttk.Button(self,text="University Level" ,
                          command=lambda:controller.show_frame(fig15))
        button4.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()

        button5=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig2))
        button5.pack(pady=10,padx=10)

class fig4(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Select appropriate age-group :", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()

        button1=ttk.Button(self,text="Children" ,
                          command=lambda:controller.show_frame(fig5))
        button1.pack(pady=10,padx=10)
        button2=ttk.Button(self,text="Youth" ,
                          command=lambda:controller.show_frame(fig10))
        button2.pack(pady=10,padx=10)
        button3=ttk.Button(self,text="Others" ,
                          command=lambda:controller.show_frame(fig11))
        button3.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()

        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig2))
        button4.pack(pady=10,padx=10)

class fig5(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="For Children : ( Obtained Results.... )", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________" ,font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()
        file="children.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',14)).pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

       
        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig4))
        button4.pack()
        button7=ttk.Button(self,text="Add a Query" ,
                          command=lambda:controller.show_frame(fig16))
        button7.pack()
        
class fig6(tk.Frame):

     
         
     def __init__(self, parent, controller):
       
        tk.Frame.__init__(self,parent)  
        label = tk.Label(self, text="Log-in", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        lambda : controller.delentry(entry1,entry2)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        button2=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig2))
        button2.pack()
        label1 = tk.Label(self, text="Enter name", font=('arial',16,'bold'))
        label1.pack(pady=20,padx=10)
        self.entry1=tk.Entry(self)
       
        self.entry1.pack()
        label2 = tk.Label(self, text="Enter password", font=('arial',16,'bold'))
        label2.pack(pady=30,padx=10)
        self.entry2=tk.Entry(self,show="*")
        
        self.entry2.pack()
        button3=ttk.Button(self,text="Forgot password" ,
                          command=lambda:controller.show_frame(fig1))
        button3.pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        button9=ttk.Button(self,text="Go",command=self.check_print)
        button9.pack()
      
         
     def check_print(self):
        if(self.entry1.get()=="bish" and self.entry2.get()=="password"):
             app.show_frame(fig7) 
        else:
            tm.showerror("Login error","Incorrect username or password")

        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        


class fig7(tk.Frame):
     
     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Your Profile", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        button=ttk.Button(self,text="View Queries" ,
                          command=lambda:controller.show_frame(fig17))
        button.pack(pady=10,padx=10)
        button1=ttk.Button(self,text="Post Updates" ,
                          command=lambda:controller.show_frame(fig18))
        button1.pack(pady=10,padx=10)
        button2=ttk.Button(self,text="Log-out" ,
                          command=lambda:controller.show_frame(fig1))
        button2.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        button3=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig6))
        button3.pack(pady=10,padx=10)
        

class fig8(tk.Frame):
     def mfileopen(self):
         file1=filedialog.askopenfile()
         label1=Label(text=file1).pack()

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Sign-Up", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label1= tk.Label(self, text="Name", font=('arial',16,'bold'))
        label1.pack()
        self.entry1=tk.Entry(self)
        self.entry1.pack()
        label2= tk.Label(self, text="Password", font=('arial',16,'bold'))
        label2.pack()
        self.entry2=tk.Entry(self,show="*")
        self.entry2.pack()
        label3= tk.Label(self, text="Confirm Password", font=('arial',16,'bold'))
        label3.pack()
        self.entry3=tk.Entry(self,show="*")
        self.entry3.pack()
        label4= tk.Label(self, text="DOB", font=('arial',16,'bold'))
        label4.pack()
        label4= tk.Label(self, text="( dd/mm/yy )", font=('arial',12))
        label4.pack()
        self.entry4=tk.Entry(self)
        self.entry4.pack()
        label5= tk.Label(self, text="Institute/Organization Name :", font=('arial',16,'bold'))
        label5.pack()
        self.entry5=tk.Entry(self)
        self.entry5.pack()
        label6= tk.Label(self, text="Institute/Organization Type :", font=('arial',16,'bold'))
        label6.pack()
        self.entry6=tk.Entry(self)
        self.entry6.pack()
        
        label7= tk.Label(self, text="Upload a copy of your CV here:", font=('arial',16,'bold'))
        label7.pack()
        button7=ttk.Button(self,text="Upload Here" ,
                          command=self.mfileopen)
        button7.pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        button8=ttk.Button(self,text="Done" ,
                          command=self.check_it)
        button8.pack()
       
        button9=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig2))
        button9.pack()

     def check_it(self):
        if(self.entry2.get()=="" or self.entry3.get()=="" or self.entry1.get()=="" or self.entry4.get()=="" or self.entry5.get()=="" or self.entry6.get()=="" ):
          
             tm.showerror("Error" , " Fill the form completely !")

        elif(self.entry2.get()!=self.entry3.get()):
             tm.showerror("Error", " Password didn't match !")
            
              
        else:
              app.show_frame(fig9) 
              tm.showinfo("Done" , " Your Profile has been successfully been created ! \
         \n Now you can Post Updates, View Queries \
        \n and Reply them.  ")
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry5.delete(0, 'end')
        self.entry6.delete(0, 'end')
        
        


    
class fig9(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Thanks !  Your Profile is ready.", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label = tk.Label(self, text="Your Profile has been created temporarily and will \
        \n be checked by the authority.   ", font=('arial',16,'bold'))
        label.pack(pady=10,padx=10)
        
        button1=ttk.Button(self,text="Log-out" ,
                          command=lambda:controller.show_frame(fig1))
        button1.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        button2=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig8))
        button2.pack(pady=10,padx=10)

class fig10(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="For Youth : ( Obtained Results.... )", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()
        file="youth.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',13)).pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

       
        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig4))
        button4.pack()
        button7=ttk.Button(self,text="Add a Query" ,
                          command=lambda:controller.show_frame(fig16))
        button7.pack()

class fig11(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="For Others : ( Obtained Results.... )", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        file="others.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',14)).pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig4))
        button4.pack()
        button7=ttk.Button(self,text="Add a Query" ,
                          command=lambda:controller.show_frame(fig16))
        button7.pack()

class fig12(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Primary Level: ( Obtained Results.... )", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        file="primary.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',14)).pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig3))
        button4.pack()
        button7=ttk.Button(self,text="Add a Query" ,
                          command=lambda:controller.show_frame(fig16))
        button7.pack()

class fig13(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=" Secondary Level: ( Obtained Results.... )", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        file="secondary.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',14)).pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig3))
        button4.pack()
        button7=ttk.Button(self,text="Add a Query" ,
                          command=lambda:controller.show_frame(fig16))
        button7.pack()


class fig14(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Higher Secondary Level: ( Obtained Results.... )", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        file="higher.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',14)).pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

       
        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig3))
        button4.pack()
        button7=ttk.Button(self,text="Add a Query" ,
                          command=lambda:controller.show_frame(fig16))
        button7.pack()

class fig15(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="University Level: ( Obtained Results.... )", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        file="university.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',14)).pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________",font=('arial',12)).pack()
        label0=tk.Label(self, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=('arial',12)).pack()

        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig3))
        button4.pack()
        button7=ttk.Button(self,text="Add a Query" ,
                          command=lambda:controller.show_frame(fig16))
        button7.pack()

class fig16(tk.Frame):

      def back(self):
         self.entry1.delete(0, 'end')
         self.entry2.delete(0, 'end')
         self.t.delete('1.0','end')
         app.show_frame(fig2)

      def post(self):
         my=open("query.txt","a")
         my.write( "From Student:"+" \n  Name :"+self.entry1.get() + " || To: " +self.entry2.get()+" \t || Query:"+self.t.get("1.0",END) ) 
         my.close()
         self.entry1.delete(0, 'end')
         self.entry2.delete(0, 'end')
         self.t.delete('1.0','end')
         tm.showinfo("Done" , "Posted Successfully !  ")
        
         

      def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
       
        label = tk.Label(self, text="Add your query here :", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text=" Enter your Name : ", font=('arial',14))
        label.pack(pady=10,padx=10)
        self.entry1=tk.Entry(self)
        self.entry1.pack()
        label = tk.Label(self, text=" Enter the name of Institue/Organization : ", font=('arial',14))
        label.pack(pady=10,padx=10)
        self.entry2=tk.Entry(self)
        self.entry2.pack()
        label = tk.Label(self, text=" Enter your Query here : ", font=('arial',14))
        label.pack(pady=10,padx=10)
        
        self.t = tk.Text(self, height=10, width=50)
        self.t.pack()
        button4=ttk.Button(self,text="Post Query" ,
                          command=self.post)
        button4.pack()
        button5=ttk.Button(self,text="BACK" ,
                          command=self.back)
        button5.pack()

        
class fig17(tk.Frame):
     def reply(self):
         my=open("query.txt","a")
         my.write( "From Institute/Org. :"+" \n" +self.entry1.get()+": \t"+"|| To :"+self.entry2.get()+"\t || Reply : "+self.t.get("1.0",END) ) 
         my.close()
         self.entry1.delete(0, 'end')
         self.entry2.delete(0, 'end')
         self.t.delete('1.0','end')
         tm.showinfo("Done" , "Posted Successfully !  ")
         

         
     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Query Results :", font=('arial',16,'bold'))
        label.pack()
        file="query.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',12)).pack()
        label = tk.Label(self, text="Reply Here :", font=('arial',16,'bold'))
        label.pack()
        label = tk.Label(self, text=" Enter Institute/ Organization Name: ", font=('arial',14))
        label.pack(pady=10,padx=10)
        self.entry1=tk.Entry(self)
        self.entry1.pack()
        label = tk.Label(self, text=" To : ", font=('arial',14))
        label.pack(pady=10,padx=10)
        self.entry2=tk.Entry(self)
        self.entry2.pack()
        self.t = tk.Text(self, height=10, width=40)
        self.t.pack()
        button1=ttk.Button(self,text="Reply" ,
                          command=self.reply)
        button1.pack()
        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig7))
        button4.pack()



class fig18(tk.Frame):
      def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=" Select Category to Post : ", font=('arial',29,'bold'))
        label.pack(pady=10,padx=10)
        button1=ttk.Button(self,text="Children" ,
                          command=self.children1)
        button1.pack()
        button2=ttk.Button(self,text="Youth" ,
                          command=self.youth1)
        button2.pack()
        button3=ttk.Button(self,text="Others" ,
                          command=self.others1)
        button3.pack()
        button4=ttk.Button(self,text="Primary Level" ,
                          command=self.primary1)
        button4.pack()
        button5=ttk.Button(self,text="Secondary Level" ,
                          command=self.secondary1)
        button5.pack()
        button6=ttk.Button(self,text="Higher Secondary Level" ,
                          command=self.higher1)
        button6.pack()
        button7=ttk.Button(self,text="University Level" ,
                          command=self.university1)
        button7.pack()
        label = tk.Label(self, text=" Post Here : ", font=('arial',16,'bold'))
        label.pack(pady=10,padx=10)
        self.t = tk.Text(self, height=20, width=40)
        self.t.pack()
        button8=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig7))
        button8.pack()
      def children1(self):
         my=open("children.txt","a")
         my.write( "\n"+self.t.get("1.0",END) ) 
         my.close()
         tm.showinfo("Done" , "Posted Successfully !  ")
         self.t.delete('1.0','end')

      def youth1(self):
         my=open("youth.txt","a")
         my.write("\n"+ self.t.get("1.0",END) ) 
         my.close()
         tm.showinfo("Done" , "Posted Successfully !  ")
         self.t.delete('1.0','end')

      def others1(self):
         my=open("others.txt","a")
         my.write("\n"+self.t.get("1.0",END) ) 
         my.close()
         tm.showinfo("Done" , "Posted Successfully !  ")
         self.t.delete('1.0','end')

      def primary1(self):
         my=open("primary.txt","a")
         my.write( "\n"+self.t.get("1.0",END) ) 
         my.close()
         tm.showinfo("Done" , "Posted Successfully !  ")
         self.t.delete('1.0','end')

      def secondary1(self):
         my=open("secondary.txt","a")
         my.write( "\n"+self.t.get("1.0",END) ) 
         my.close()
         tm.showinfo("Done" , "Posted Successfully !  ")
         self.t.delete('1.0','end')

      def higher1(self):
         my=open("higher.txt","a")
         my.write( "\n"+self.t.get("1.0",END) ) 
         my.close()
         tm.showinfo("Done" , "Posted Successfully !  ")
         self.t.delete('1.0','end')

      def university1(self):
         my=open("university.txt","a")
         my.write( "\n"+self.t.get("1.0",END) ) 
         my.close()
         tm.showinfo("Done" , "Posted Successfully !  ")
         self.t.delete('1.0','end')

         
class fig19(tk.Frame):
      def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Query-Reply Results :", font=('arial',24,'bold'))
        label.pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()

        
        file="query.txt"
        f=open(file)
        label1=tk.Label(self,text=f.read(),font=('arial',12)).pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        label0=tk.Label(self, text="____________________________________________________________________________________________________________________________________________________").pack()
        button4=ttk.Button(self,text="BACK" ,
                          command=lambda:controller.show_frame(fig4))
        button4.pack()

        
app = recreate()
app.title("Re-create")
app.geometry("1366x768")

app.mainloop()

