import tkinter as tk
import search
from search import see
import time
import tkinter.messagebox
from buddy import talk
#from support import themer, fontier, enablevoice
from collect_db import read
import threading
from tkinter import *
#import tensorflow as tf
#from tensorflow import *
from PIL import ImageTk, Image, ImageOps
#from neuralnets import *
#from voicerec import *
#from neuralnes import *
#from collect_db import insert
#from search import *
#import pyttsX3 
#import js2py
import os  
from buddy import test
import random
from random import choice
import re 
import datetime
from datetime import datetime
from tkinter import messagebox
from tkinter.font import Font
import textwrap
from tkinter.filedialog import askopenfilename
#from voicerec import font_change_default,font_change_times,font_change_system,font_change_helvetica,color_theme_default,color_theme_dark, color_theme_turquoise,color_theme_dark_blue,color_theme_hacker,default_format,road_image_theme

#from buddy import ava

cheight=610
cwidth=440
fheight=0.8
fwidth=0.8

#Button confirming data stored

def listconfirm():
    print('so  your name is', name, ' You want to use the system for ' ,whyuse  ,'  correct ? ')


'''   
#new window
def home_window():
     class workenvironment():
          def __init__(self):
             global backimage 

  
 
             '''

           
def user_manual():
    def ans():
       global image
       image = ImageTk.PhotoImage(Image.open("manim/Answering.PNG"))
       onscreen = tk.Label(im, image=image)
       onscreen.pack()

    def prog():
       global image
       image = ImageTk.PhotoImage(Image.open("manim/progress.PNG"))
       onscreen = tk.Label(im, image=image)
       onscreen.pack()

    def cques():
       global image
       image = ImageTk.PhotoImage(Image.open("manim/seequestions.PNG"))
       onscreen = tk.Label(im, image=image)
       onscreen.pack()


    def reg():
       global image
       image = ImageTk.PhotoImage(Image.open("manim/fmanimage.PNG"))
       onscreen = tk.Label(im, image=image)
       onscreen.pack()
       

    global backg
    global image
    browse = Toplevel()
    browse.geometry('600x600')
    browse.iconbitmap("images/Processing.ico")
    browse.title("User manual Images")
    backg = ImageTk.PhotoImage(Image.open("manim/frustration.jpg"))
    im = tk.Label(browse, image=backg)
    im.pack()




    buddymenu = Menu(canvas)
    browse.config(menu=buddymenu)
   
    

    user_man = Menu(buddymenu)
    
    buddymenu.add_cascade(menu=user_man,label="user manual images")
    user_man.add_command(label="How to insert Answer",command=ans)
    user_man.add_command(label="How to select quesion",command= cques)
    user_man.add_command(label="See Progress made", command=prog)
    user_man.add_command(label="registration", command=reg)

def home_window():

    '''
    import pyodbc
    cntn=pyodbc.connect('Driver={SQL Server};Server=LAPTOP-DG9KS6R0\SQLEXPRESS2019;Database=Buddydb;Trusted_Connection=yes;')
    #############print("INSERTING DATA INTO THE TABLE")
    cur = cntn.cursor()
    uname = entryname.get()
    usecase = entry.get()
    sql =  " INSERT into dbo.UserRelated(id,username, usepuporrelation) values(?,?,?);"
    cur.execute(sql,(18,uname,usecase))
    cntn.commit()
    cntn.close()
    '''
    global backimage
    global fileimage
    global search
    global buddychatIm
    global imagegif

    top = Toplevel()
    top.geometry('600x600')
    top.iconbitmap("images/Processing.ico")
    top.title("Buddy Environment")
    backimage = ImageTk.PhotoImage(Image.open("images/4d94fc29f00946f0ac8b4d37550f9f43.jpg"))
    onscreen = tk.Label(top, image=backimage)
    onscreen.pack()
    
    
    # including icons to home  
    home = tk.Label(onscreen, text="coding navigates the way to the future",bg='#1B2631' ,fg='#F0F3F4')
    home.place(relheight=0.05 ,relwidth=0.6 , relx=0.1, rely=0.1)
    # welcome text
    wtext = tk.Label(onscreen, text="Welcome ..."+name.get(),bg='#1B2631' ,fg='#F0F3F4')
    wtext.place(relheight=0.05 ,relwidth=0.6 , relx=0.1, rely=0.2)

    fileimage = ImageTk.PhotoImage(Image.open("images/fileicon.jpg"))
    filebtn = tk.Button(onscreen , image=fileimage, command=chatfile)
    filebtn.place(relheight=0.125 ,relwidth=0.125 , relx=0.66, rely=0.48)
    
    search = ImageTk.PhotoImage(Image.open("images/search.jpg"))
    searchbutton = tk.Button(onscreen, image=search, command=user_manual)
    searchbutton.place(relheight=0.125 ,relwidth=0.125 , relx=0.8, rely=0.28)

  

    imagegif = ImageTk.PhotoImage(Image.open("images/imageedit_3_4278289948.gif"))
    giflabel = tk.Label(onscreen, image=imagegif)
    giflabel.place(relheight=0.3 ,relwidth=0.3, relx=0.35, rely=0.689)
     

  #  chat to buddy
    buddychatIm = ImageTk.PhotoImage(Image.open("images/imag.jpeg"))
    chatbut = tk.Button(onscreen ,image=buddychatIm ,command = chat)
    chatbut.place(relheight=0.125 ,relwidth=0.125 ,relx=0.8 ,rely=0.1)
  


# menu 
    buddymenu = Menu(onscreen)
    top.config(menu=buddymenu)
 
# cascades
    userinfo = Menu(buddymenu,tearoff=0)
    buddymenu.add_cascade(menu=userinfo, label= "User Info")
    userinfo.add_command(label="Update my info" )
    userinfo.add_command(label="Manage Buddy" )
    userinfo.add_command(label="exit", command=top.quit )
    user_man = Menu(userinfo, tearoff=0)
    userinfo.add_cascade(menu=user_man, label= "User Manual")
    user_man.add_command(label="using training",command=user_manual)
    user_man.add_command(label="using testing")


    files = Menu(buddymenu)
    buddymenu.add_cascade(menu=files, label= "Files")
    files.add_command(label="last search" )
    files.add_command(label="All files" )
    files.add_command(label="images" )
    files.add_command(label="Docs" )
    files.add_command(label="Vids")
    files.add_command(label="exit", command=top.quit )

    helper = Menu(buddymenu)
    buddymenu.add_cascade(menu=helper, label= "Help")
    helper.add_command(label="About Buddy" )
    helper.add_command(label="Using functions")
    helper.add_command(label="Updates" )
    helper.add_command(label="exit", command=top.quit )
     

    

    

'''
             self.fileicon = tk.Button(self.top, image=filephoto, command=open_file)
             filephoto = ImageTk.PhotoImage(Image.open("images/fileicon.jpg"))
'''

# define open file button
#def open_file():
   # print('open file successful')


'''
     #say the user name ... call variable from different file
          def speak(self, name) :
               # dependency pyttsX3 needs to be installed
               engine.say(name)
               engine.runAndWait()
          def clicked(self) :
              name = entryname.get()  
              self.speak(name)    

             
    if __name__=='__main__':
            widget = workenvironment()
    
'''


def chat():
    # chat to user
    global photo
    topchat = Toplevel()
    topchat.title("Buddy Chatter")
    topchat.iconbitmap("images/Processing.ico")
    topchat.geometry('450x600')
    saved_username = ["You"]

    class ChatGround(Frame):
        def __init__(self, master=None):
          Frame.__init__(self, master)
          global photo
          self.master = master
          # sets default bg for top level windows
          self.photo = ImageTk.PhotoImage(Image.open("images/90a4b65d8e7f45e6a959cff29196d1f0.jpg"))
          self.back = tk.Label(self.master, image = self.photo)
          

          self.tl_bg = self.back
          self.tl_bg2 = "#EEEEEE"
          self.tl_fg = "#000000"
          self.font = "Verdana 10"

          menu = Menu(self.master)
          self.master.config(menu=menu, bd=5)


# Menu bar
          

# cascades
          subject = Menu(menu)
          subject.add_cascade(menu=subject, label= "User Info")
         

          
          subject.add_command(label="Mathematics", command= maths )
          subject.add_command(label="Physical sciences" )
          subject.add_command(label="Business Studies" )
          subject.add_command(label="Economics" )
          subject.add_command(label="exit", command=topchat.quit )


    
    
    

      # File
          
          files = Menu(menu, tearoff=0)
          menu.add_cascade(label="File", menu=files)
       #   file.add_command(label="Save Chat Log", command=self.save_chat)
          files.add_command(label="Clear Chat", command=self.clear_chat)
       #   file.add_separator()
          files.add_command(label="Exit",command=topchat.quit)

    #  Options
          options = Menu(menu, tearoff=0)
          menu.add_cascade(label="Options", menu=options)
          options.add_command(label="How Buddy was made")
          options.add_command(label="How Buddy was made")

        # username
       

        

     #  font
          font = Menu(options, tearoff=0)
          options.add_cascade(label="Font", menu=font)
          
          font.add_command(label="Default",command=self.font_change_default)
          font.add_command(label="Times",command=self.font_change_times)
          font.add_command(label="System",command=self.font_change_system)
          font.add_command(label="Helvetica",command=self.font_change_helvetica)
          font.add_command(label="Fixedsys",command=self.font_change_fixedsys)

        # color theme
          color_theme = Menu(options, tearoff=0)
          options.add_cascade(label="Color Theme", menu=color_theme)
          color_theme.add_command(label="Default",command=self.color_theme_default) 
          # color_theme.add_command(label="Night",command=self.) 
          color_theme.add_command(label="Grey",command=self.color_theme_grey) 
          color_theme.add_command(label="Blue",command=self.color_theme_dark_blue) 
          color_theme.add_command(label="Road_background",command=self.road_image_theme) 
          
          color_theme.add_command(label="Torque",command=self.color_theme_turquoise)
          color_theme.add_command(label="Hacker",command=self.color_theme_hacker)
       #    color_theme.add_command(label='Mkbhd',command=self.MKBHD)


      
          help_option = Menu(menu, tearoff=0)
          menu.add_cascade(label="Help", menu=help_option)
          #help_option.add_command(label="Features", command=self.features_msg)
          help_option.add_command(label="About buddy", command=self.msg)
          help_option.add_command(label="Develpoers", command=self.about)

          self.text_frame = Frame(self.master, bd=6)
          self.text_frame.pack(expand=True, fill=BOTH)

            # scrollbar for text box
          self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
          self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
          self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
          self.text_box.pack(expand=True, fill=BOTH)
          self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
          self.entry_frame = Frame(self.master, bd=1)
          self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
          self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
          self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
            # self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
          self.send_button_frame = Frame(self.master, bd=0)
          self.send_button_frame.pack(fill=BOTH)

        # send button
          self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
          self.send_button.pack(side=LEFT, ipady=8)
          self.master.bind("<Return>", self.send_message_insert)
        
          self.last_sent_label(date="No messages sent.")
        #t2 = threading.Thread(target=self.send_message_insert(, name='t1')
        #t2.start()
        

  
        def last_sent_label(self, date):
              try:
                 self.sent_label.destroy()
              except AttributeError:
                 pass

              self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
              self.sent_label.pack(side=LEFT, fill=X, padx=3)

        def clear_chat(self):
          self.text_box.config(state=NORMAL)
          self.last_sent_label(date="No messages sent.")
          self.text_box.delete(1.0, END)
          self.text_box.delete(1.0, END)
          self.text_box.config(state=DISABLED)

        def chatexit(self):
          exit()

        def msg(self):
           tkinter.messagebox.showinfo("PyBOT v1.0",'PyBOT is a chatbot for answering python queries\nIt is based on retrival-based NLP using pythons NLTK tool-kit module\nGUI is based on Tkinter\nIt can answer questions regarding python language for new learners')

    
        def about(self):
            tkinter.messagebox.showinfo("PyBOT Developers","1.Abhishek Ezhava\n2.Mayur Kadam\n3.Monis Khot\n4.Raj Vishwakarma")
    
        def send_message_insert(self, message):
            user_input = self.entry_field.get()
            pr1 = "User : " + user_input + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr1)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
        #t1 = threading.Thread(target=self.playResponce, args=(user_input,))
        #t1.start()
            time.sleep(1)
            ob=talk(user_input)
            pr="Buddy.... : " + ob + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)



    
        #t2 = threading.Thread(target=self.playResponce, args=(ob,))
        #t2.start()
        #return ob
    
    


        
        
        def font_change_default(self):
           self.text_box.config(font="Verdana 10")
           self.entry_field.config(font="Verdana 10")
           self.font = "Verdana 10"

        def font_change_times(self):
           self.text_box.config(font="Times")
           self.entry_field.config(font="Times")
           self.font = "Times"






        def font_change_system(self):
           self.text_box.config(font="System")
           self.entry_field.config(font="System")
           self.font = "System"

        def font_change_helvetica(self):
           self.text_box.config(font="helvetica 10")
           self.entry_field.config(font="helvetica 10")
           self.font = "helvetica 10"

        def font_change_fixedsys(self):
            self.text_box.config(font="fixedsys")
            self.entry_field.config(font="fixedsys")
            self.font = "fixedsys"

    # Dark
        def color_theme_dark(self):
            self.master.config(bg="#2a2b2d")
            self.text_frame.config(bg="#2a2b2d")
            self.text_box.config(bg="#212121", fg="#FFFFFF")
            self.entry_frame.config(bg="#2a2b2d")
            self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
            self.send_button_frame.config(bg="#2a2b2d")
            self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
       # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

            self.tl_bg = "#212121"
            self.tl_bg2 = "#2a2b2d"
            self.tl_fg = "#FFFFFF"

    # Grey
        def color_theme_grey(self):
             self.master.config(bg="#444444")
             self.text_frame.config(bg="#444444")
             self.text_box.config(bg="#4f4f4f", fg="#ffffff")
             self.entry_frame.config(bg="#444444")
             self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
             self.send_button_frame.config(bg="#444444")
             self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        #self.emoji_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
             self.sent_label.config(bg="#444444", fg="#ffffff")

             self.tl_bg = "#4f4f4f"
             self.tl_bg2 = "#444444"
             self.tl_fg = "#ffffff"


        def color_theme_turquoise(self):
            self.master.config(bg="#003333")
            self.text_frame.config(bg="#003333")
            self.text_box.config(bg="#669999", fg="#FFFFFF")
            self.entry_frame.config(bg="#003333")
            self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
            self.send_button_frame.config(bg="#003333")
            self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#003333", fg="#FFFFFF")

            self.tl_bg = "#669999"
            self.tl_bg2 = "#003333"
            self.tl_fg = "#FFFFFF"    

    # Blue
        def color_theme_dark_blue(self):
            self.master.config(bg="#263b54")
            self.text_frame.config(bg="#263b54")
            self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
            self.entry_frame.config(bg="#263b54")
            self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
            self.send_button_frame.config(bg="#263b54")
            self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#263b54", fg="#FFFFFF")

            self.tl_bg = "#1c2e44"
            self.tl_bg2 = "#263b54"
            self.tl_fg = "#FFFFFF"

 
    

    # Torque
        def color_theme_turquoise(self):
             self.master.config(bg="#003333")
             self.text_frame.config(bg="#003333")
             self.text_box.config(bg="#669999", fg="#FFFFFF")
             self.entry_frame.config(bg="#003333")
             self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
             self.send_button_frame.config(bg="#003333")
             self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
             self.sent_label.config(bg="#003333", fg="#FFFFFF")

             self.tl_bg = "#669999"
             self.tl_bg2 = "#003333"
             self.tl_fg = "#FFFFFF"

# image theme
        def road_image_theme(self):
            global photo

            self.photo = ImageTk.PhotoImage(Image.open("images/w.jpg"))
            
            self.master.config(bg=self.photo)
            self.text_frame.config(bg=self.photo)
            self.text_box.config(bg="#212121", fg="#FFFFFF")
            self.entry_frame.config(bg="#2a2b2d")
            self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground=self.back)
            self.send_button_frame.config(bg="#2a2b2d")
            self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

            self.tl_bg = self.back
            self.tl_bg2 = self.back
            self.tl_fg = "#FFFFFF"





    # Hacker
        def color_theme_hacker(self):
            self.master.config(bg="#0F0F0F")
            self.text_frame.config(bg="#0F0F0F")
            self.entry_frame.config(bg="#0F0F0F")
            self.text_box.config(bg="#0F0F0F", fg="#33FF33")
            self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
            self.send_button_frame.config(bg="#0F0F0F")
            self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

            self.tl_bg = "#0F0F0F"
            self.tl_bg2 = "#0F0F0F"
            self.tl_fg = "#33FF33"

        def default_format(self):
            self.font_change_default()
            self.color_theme_default()   
          
        def color_theme_default(self):
            self.master.config(bg="#EEEEEE")
            self.text_frame.config(bg="#EEEEEE")
            self.entry_frame.config(bg="#EEEEEE")
            self.text_box.config(bg="#FFFFFF", fg="#000000")
            self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
            self.send_button_frame.config(bg="#EEEEEE")
            self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        #self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
            self.sent_label.config(bg="#EEEEEE", fg="#000000")

            self.tl_bg = "#FFFFFF"
            self.tl_bg2 = "#EEEEEE"
            self.tl_fg = "#000000"

    # Default font and color theme
        def default_format(self):
            self.font_change_default()
            self.color_theme_default()    

    a = ChatGround(topchat)

    



######################################################################################################################################################################################################    
####                              file chat

def chatfile():
    # chat to user
    global photo
    topchat = Toplevel()
    topchat.title("Buddy Chatter")
    topchat.iconbitmap("images/Processing.ico")
    topchat.geometry('450x600')
    saved_username = ["You"]

    class ChatGround(Frame):
        def __init__(self, master=None):
          Frame.__init__(self, master)
          global photo
          self.master = master
          # sets default bg for top level windows
          self.photo = ImageTk.PhotoImage(Image.open("images/90a4b65d8e7f45e6a959cff29196d1f0.jpg"))
          self.back = tk.Label(self.master, image = self.photo)
          

          self.tl_bg = self.back
          self.tl_bg2 = "#EEEEEE"
          self.tl_fg = "#000000"
          self.font = "Verdana 10"

          menu = Menu(self.master)
          self.master.config(menu=menu, bd=5)


# Menu bar
          

# cascades
          subject = Menu(menu)
          subject.add_cascade(menu=subject, label= "User Info")
          subject.add_command(label="Mathematics")
          subject.add_command(label="Physical sciences" )
          subject.add_command(label="Business Studies" )
          subject.add_command(label="Economics" )
          subject.add_command(label="exit", command=topchat.quit )


    
    
    

      # File
          
          files = Menu(menu, tearoff=0)
          menu.add_cascade(label="File", menu=files)
       #   file.add_command(label="Save Chat Log", command=self.save_chat)
          files.add_command(label="Clear Chat", command=self.clear_chat)
       #   file.add_separator()
          files.add_command(label="Exit",command=topchat.quit)

    #  Options
          options = Menu(menu, tearoff=0)
          menu.add_cascade(label="Options", menu=options)
          options.add_command(label="How Buddy was made")
          options.add_command(label="How Buddy was made")

        # username
       

        

     #  font
          font = Menu(options, tearoff=0)
          options.add_cascade(label="Font", menu=font)
          
          font.add_command(label="Default",command=self.font_change_default)
          font.add_command(label="Times",command=self.font_change_times)
          font.add_command(label="System",command=self.font_change_system)
          font.add_command(label="Helvetica",command=self.font_change_helvetica)
          font.add_command(label="Fixedsys",command=self.font_change_fixedsys)

        # color theme
          color_theme = Menu(options, tearoff=0)
          options.add_cascade(label="Color Theme", menu=color_theme)
          color_theme.add_command(label="Default",command=self.color_theme_default) 
          # color_theme.add_command(label="Night",command=self.) 
          color_theme.add_command(label="Grey",command=self.color_theme_grey) 
          color_theme.add_command(label="Blue",command=self.color_theme_dark_blue) 
          color_theme.add_command(label="Road_background",command=self.road_image_theme) 
          
          color_theme.add_command(label="Torque",command=self.color_theme_turquoise)
          color_theme.add_command(label="Hacker",command=self.color_theme_hacker)
       #    color_theme.add_command(label='Mkbhd',command=self.MKBHD)


      
          help_option = Menu(menu, tearoff=0)
          menu.add_cascade(label="Help", menu=help_option)
          #help_option.add_command(label="Features", command=self.features_msg)
          help_option.add_command(label="About buddy", command=self.msg)
          help_option.add_command(label="Develpoers", command=self.about)

          self.text_frame = Frame(self.master, bd=6)
          self.text_frame.pack(expand=True, fill=BOTH)

            # scrollbar for text box
          self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
          self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
          self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
          self.text_box.pack(expand=True, fill=BOTH)
          self.text_box_scrollbar.config(command=self.text_box.yview)
          self.send_button_frame = Frame(self.master, bd=0)
          self.send_button_frame.pack(fill=BOTH)
         
         # see progress button

          
          self.see =  Button(self.send_button_frame,text = "READY ?",relief=GROOVE, bd=1, command =self.tellmyprog,activebackground="#FFFFFF",bg='blue')
          self.see.pack(side=RIGHT, ipady=8)

          #list of data button
          self.label =  Button(self.send_button_frame,text = "see questions", bd=1, command =self.list_insert,activebackground="#FFFFFF",bg='white')
          self.label.pack(side=RIGHT, ipady=8)
        # frame containing user entry field
          self.entry_frame = Frame(self.master, bd=1)
          self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
          self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
          self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
            # self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
          

        # send button
          self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
          self.send_button.pack(side=LEFT, ipady=8)
          self.master.bind("<Return>", self.send_message_insert)
          self.master.bind("<Return>", self.list_insert)
        
          self.last_sent_label(date="No messages sent.")
        #t2 = threading.Thread(target=self.send_message_insert(, name='t1')
        #t2.start()
        

  
        def last_sent_label(self, date):
              try:
                 self.sent_label.destroy()
              except AttributeError:
                 pass

              self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
              self.sent_label.pack(side=LEFT, fill=X, padx=3)

        def clear_chat(self):
          self.text_box.config(state=NORMAL)
          self.last_sent_label(date="No messages sent.")
          self.text_box.delete(1.0, END)
          self.text_box.delete(1.0, END)
          self.text_box.config(state=DISABLED)

        def chatexit(self):
          exit()

        def msg(self):
           tkinter.messagebox.showinfo("PyBOT v1.0",'PyBOT is a chatbot for answering python queries\nIt is based on retrival-based NLP using pythons NLTK tool-kit module\nGUI is based on Tkinter\nIt can answer questions regarding python language for new learners')

    
        def about(self):
            tkinter.messagebox.showinfo("PyBOT Developers","andrew sindane")


            #### my progress function

        def tellmyprog(self):
            import pyodbc
            cntn=pyodbc.connect('Driver={SQL Server};Server=LAPTOP-DG9KS6R0\SQLEXPRESS2019;Database=Buddydb;Trusted_Connection=yes;')
            time.sleep(1)
            ob= see(cntn)

            pr = "Buddy...:" + str(ob) + "\n"

            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)

        def send_message_insert(self, message):
            user_input = self.entry_field.get()
            pr1 = "User : " + user_input + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr1)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
        #t1 = threading.Thread(target=self.playResponce, args=(user_input,))
            
        #t1.start()
            time.sleep(1)
            ob=test(user_input)
            pr="Questions.... : " + ob + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)

        def list_insert(self):
            import pyodbc
            cntn=pyodbc.connect('Driver={SQL Server};Server=LAPTOP-DG9KS6R0\SQLEXPRESS2019;Database=Buddydb;Trusted_Connection=yes;')
        #t1 = threading.Thread(target=self.playResponce, args=(user_input,))
            p = read(cntn)
            listy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25]
            import random
            ind1 = p[random.choice(listy)]
            ind2 = p[random.choice(listy)]
            ind3 =  p[random.choice(listy)]
            ind4 =  p[random.choice(listy)]
            ind5 =  p[random.choice(listy)]
        #t1.start()
            time.sleep(1)
            #ob=talk(user_input)
            pr1=".... : " + ind1 + "\n"
            pr2=".... : " + ind2 + "\n"
            pr3=".... : " + ind3 + "\n"
            pr4=".... : " + ind4 + "\n"
            pr5=".... : " + ind5 + "\n"

            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr1)
            self.text_box.insert(END, pr2)
            self.text_box.insert(END, pr3)
            self.text_box.insert(END, pr4)
            self.text_box.insert(END, pr5)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)
           
    
        #t2 = threading.Thread(target=self.playResponce, args=(ob,))
        #t2.start()
        #return ob
    
    


        
        
        def font_change_default(self):
           self.text_box.config(font="Verdana 10")
           self.entry_field.config(font="Verdana 10")
           self.font = "Verdana 10"

        def font_change_times(self):
           self.text_box.config(font="Times")
           self.entry_field.config(font="Times")
           self.font = "Times"






        def font_change_system(self):
           self.text_box.config(font="System")
           self.entry_field.config(font="System")
           self.font = "System"

        def font_change_helvetica(self):
           self.text_box.config(font="helvetica 10")
           self.entry_field.config(font="helvetica 10")
           self.font = "helvetica 10"

        def font_change_fixedsys(self):
            self.text_box.config(font="fixedsys")
            self.entry_field.config(font="fixedsys")
            self.font = "fixedsys"

        def color_theme_default(self):
            self.master.config(bg="#EEEEEE")
            self.text_frame.config(bg="#EEEEEE")
            self.entry_frame.config(bg="#EEEEEE")
            self.text_box.config(bg="#FFFFFF", fg="#000000")
            self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
            self.send_button_frame.config(bg="#EEEEEE")
            self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        #self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
            self.sent_label.config(bg="#EEEEEE", fg="#000000")

            self.tl_bg = "#FFFFFF"
            self.tl_bg2 = "#EEEEEE"
            self.tl_fg = "#000000"

    # Dark
        def color_theme_dark(self):
            self.master.config(bg="#2a2b2d")
            self.text_frame.config(bg="#2a2b2d")
            self.text_box.config(bg="#212121", fg="#FFFFFF")
            self.entry_frame.config(bg="#2a2b2d")
            self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
            self.send_button_frame.config(bg="#2a2b2d")
            self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
       # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

            self.tl_bg = "#212121"
            self.tl_bg2 = "#2a2b2d"
            self.tl_fg = "#FFFFFF"

    # Grey
        def color_theme_grey(self):
             self.master.config(bg="#444444")
             self.text_frame.config(bg="#444444")
             self.text_box.config(bg="#4f4f4f", fg="#ffffff")
             self.entry_frame.config(bg="#444444")
             self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
             self.send_button_frame.config(bg="#444444")
             self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        #self.emoji_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
             self.sent_label.config(bg="#444444", fg="#ffffff")

             self.tl_bg = "#4f4f4f"
             self.tl_bg2 = "#444444"
             self.tl_fg = "#ffffff"


        def color_theme_turquoise(self):
            self.master.config(bg="#003333")
            self.text_frame.config(bg="#003333")
            self.text_box.config(bg="#669999", fg="#FFFFFF")
            self.entry_frame.config(bg="#003333")
            self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
            self.send_button_frame.config(bg="#003333")
            self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#003333", fg="#FFFFFF")

            self.tl_bg = "#669999"
            self.tl_bg2 = "#003333"
            self.tl_fg = "#FFFFFF"    

    # Blue
        def color_theme_dark_blue(self):
            self.master.config(bg="#263b54")
            self.text_frame.config(bg="#263b54")
            self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
            self.entry_frame.config(bg="#263b54")
            self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
            self.send_button_frame.config(bg="#263b54")
            self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#263b54", fg="#FFFFFF")

            self.tl_bg = "#1c2e44"
            self.tl_bg2 = "#263b54"
            self.tl_fg = "#FFFFFF"

 
    

    # Torque
        def color_theme_turquoise(self):
             self.master.config(bg="#003333")
             self.text_frame.config(bg="#003333")
             self.text_box.config(bg="#669999", fg="#FFFFFF")
             self.entry_frame.config(bg="#003333")
             self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
             self.send_button_frame.config(bg="#003333")
             self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
             self.sent_label.config(bg="#003333", fg="#FFFFFF")

             self.tl_bg = "#669999"
             self.tl_bg2 = "#003333"
             self.tl_fg = "#FFFFFF"

# image theme
        def road_image_theme(self):
            global photo

            self.photo = ImageTk.PhotoImage(Image.open("images/w.jpg"))
            
            self.master.config(bg=self.photo)
            self.text_frame.config(bg=self.photo)
            self.text_box.config(bg="#212121", fg="#FFFFFF")
            self.entry_frame.config(bg="#2a2b2d")
            self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground=self.back)
            self.send_button_frame.config(bg="#2a2b2d")
            self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        # self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

            self.tl_bg = self.back
            self.tl_bg2 = self.back
            self.tl_fg = "#FFFFFF"





    # Hacker
        def color_theme_hacker(self):
            self.master.config(bg="#0F0F0F")
            self.text_frame.config(bg="#0F0F0F")
            self.entry_frame.config(bg="#0F0F0F")
            self.text_box.config(bg="#0F0F0F", fg="#33FF33")
            self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
            self.send_button_frame.config(bg="#0F0F0F")
            self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
            self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

            self.tl_bg = "#0F0F0F"
            self.tl_bg2 = "#0F0F0F"
            self.tl_fg = "#33FF33"

    

    # Default font and color theme
        def default_format(self):
            self.font_change_default()
            self.color_theme_default()   
          
        def color_theme_default(self):
            self.master.config(bg="#EEEEEE")
            self.text_frame.config(bg="#EEEEEE")
            self.entry_frame.config(bg="#EEEEEE")
            self.text_box.config(bg="#FFFFFF", fg="#000000")
            self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
            self.send_button_frame.config(bg="#EEEEEE")
            self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        #self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
            self.sent_label.config(bg="#EEEEEE", fg="#000000")

            self.tl_bg = "#FFFFFF"
            self.tl_bg2 = "#EEEEEE"
            self.tl_fg = "#000000"
      

    a = ChatGround(topchat)

    



    



























def changeentry():
  print("entry changed")





def insert():
    user_input = name.get()
    user_input1 = whyuse.get()
    pr1 = "name : " + user_input + "\n"
    pr2 = "Purpose : " + user_input1 + "\n"
    listbox.configure(state=NORMAL)
    listbox.insert(END, pr1)
    listbox.insert(END, pr2)
    listbox.configure(state=DISABLED)
    listbox.see(END)
    time.sleep(1)






         




def maths():
# close chAT
  print('')


root = tk.Tk()
root.title('Buddy Artificial Application')
root.geometry('450x600')
root.iconbitmap("images/Processing.ico")
canvas = tk.Canvas(root, height= cheight, width=cwidth, bg='#1B2631')
canvas.pack()

frame = tk.Frame(canvas, bg="#1B2631" )
frame.place( relheight=fheight ,relwidth=fwidth , relx=0.1, rely=0.1)

labelw= tk.Label(frame, text ="HEY THERE..." , fg='#F0F3F4'  ,bg='#1B2631')
labelw.grid(row=0 , column=1 )

labeln= tk.Label(frame, text="What is your name ... " ,bg='#1B2631' ,fg='#F0F3F4')
labeln.grid(row=1, column=0 ,sticky=W )
#variable initialisation
name = StringVar()
entryname = tk.Entry(frame, textvariable=name,bg='#1B2631' ,fg='#F0F3F4')
entryname.grid(row=2, column=0 , sticky=W, pady=10,padx=20)


whyuse = StringVar()
label = tk.Label(frame, text ="How would you like to use this sytem ? eg Educational purpose,business ,personal or combination ", bg='#1b2631' ,fg='#F0F3F4')
label.grid(row=3, column=0 , sticky=W)
entry = tk.Entry(frame, textvariable=whyuse,bg='#1B2631' ,fg='#F0F3F4')
entry.grid(row=4, column=0 , sticky=W, pady=10,padx=20)

#list box
#listbox= tk.Listbox(frame, height=8 ,width=50 ,border=0 ,bg='#1B2631' )
#listbox.grid( row=6 , column=0 , rowspan=6 , columnspan =3, pady=10, padx=20 ,sticky=W)
#scrolbar
scrollbar= tk.Scrollbar(frame)


#scrollbar.grid( row=6, column=0 ,padx=10 ,pady=10)
scrollbar.grid( row=6 , column=0 , rowspan=6 , columnspan =3, pady=10, padx=20 ,sticky=W)
listbox = Text(frame, yscrollcommand=scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg='#1B2631', font="Verdana 10", relief=GROOVE,
                             width=50, height=8)
listbox.grid(row=6 , column=0 , rowspan=6 , columnspan =3, pady=10, padx=20 ,sticky=W)

scrollbar.configure(command= listbox.yview)
'''
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command= listbox.yview)
'''

################### working text box




button = tk.Button(frame, text=" done" , width=12, bg='black', fg='#F0F3F4' ,command=insert)
button.grid(row=5 , column=0 ,pady=10 ,padx=20, sticky=W)

button = tk.Button(frame, text=" correct" , width=12, bg='black',fg='#F0F3F4', command=home_window)


button.grid(row=12 , column=0 ,pady=10,padx=20, sticky=W )


change = tk.Button(frame, text="change entry" , width=15, bg= 'black' , fg='#F0F3F4', command=changeentry)
change.grid( row=12, column=0)


'''

# java script calls
welcome = ''' #function hello(name){ console.log( "Hello" + name);}
'''
hello = js2py.eval_js(welcome)
 hello(name)

# request data script
   
request = '''#function datarequest(data){} '''
#request = js2py.eval_js(request)
#datarequest(' enter your data')
# end  java script

'''
'''



#start program 
root.mainloop()
