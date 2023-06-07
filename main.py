# -*- coding: utf-8 -*-

import tkinter as tk
#FUNCTION_____
import os
def shutdown():
   os.system("shutdown /s /t 1")
def restart():
   os.system("shutdown /r /t 1")
def logout():
    os.system("shutdown -l")
#GUI_________________
root=tk.Tk()
window=tk.Canvas(root,height=480,width=600,)
window.pack()

#FRAME____
frame=tk.Frame(root)
frame.place(relwidth=1,relheight=1)

#LABELS____
back_img=tk.PhotoImage(file='background.png')
win_img=tk.PhotoImage(file='windows.png')
label_back=tk.Label(frame,image=back_img)
label_win=tk.Label(frame,image=win_img)

label_s=tk.Label(frame,text='SHUTDOWN',font=("Arial"))
label_r=tk.Label(frame,text='RESTART',font=("Arial"))
label_l=tk.Label(frame,text='LOGOUT',font=("Arial"))
label_back.place(relwidth=1,relheight=1)

label_s.place(x=200,y=155)
label_r.place(x=200,y=265)
label_l.place(x=200,y=375)
label_win.place(x=40,y=2)

#BUTTONS____
shut_img=tk.PhotoImage(file='shutdown.png')
rest_img=tk.PhotoImage(file='restart.png')
log_img=tk.PhotoImage(file='logout.png')

shut=tk.Button(frame,image=shut_img,command=shutdown)
rest=tk.Button(frame,image=rest_img,command=restart)
log=tk.Button(frame,image=log_img,command=logout)
exit_button=tk.Button(frame,text="CANCEL",command=root.destroy)

shut.place(x=400,y=140,height=50,width=50)
rest.place(x=400,y=250,height=50,width=50)
log.place(x=400,y=360,height=50,width=50)
exit_button.place(x=530,y=444)

root.resizable(False,False)
root.mainloop()