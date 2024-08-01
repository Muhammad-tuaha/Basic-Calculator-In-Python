import tkinter as tk

#Creating window frame named calculator
Calculator=tk.Tk()

display_var=tk.StringVar()
dis_scrn = tk.Label(Calculator, textvariable=display_var, font=('Helvetica', 20), bg='lightblue', anchor='e', height=2)
dis_scrn.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

expression=""
display_var.set("Welcome to my\nfirst py project")

#defining button click function handling button event
def btn_clk(event):
    global expression
    

    btn=event.widget.cget("text") #extracting text of the pressed button
    

    if btn== "=":
       try:
        result=str(eval(expression))
        display_var.set("= "+result)
        expression=result
       except Exception as e:

        display_var.set("ERROR")
        expression="" 


    elif btn=="CLS":
       expression=""
       display_var.set(expression)


    else :   
        expression +=btn
        display_var.set(expression)

        


btns=["9","8","7","6",
      "5","4","3","2",
      "1","0","*","/",
      ".","-","+","=",
      "CLS"
      ]

col=0
row=1


for btn in btns:
    button =tk.Button(Calculator,text=btn,height=5,width=8,bg="lightgrey")
    button.grid(column=col,row=row ,padx=4,pady=4)
    button.bind("<Button-1>",btn_clk) # calling btn_clk function on right muse btn event

    col +=1
    if col>3:
      col=0
      row +=1


Calculator.mainloop() # starting the program
