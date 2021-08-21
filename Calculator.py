
from tkinter import *
expression=""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
	
	try:

		global expression
		total = str(eval(expression))

		equation.set(total)
		expression = ""

	
	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

    
if __name__ == "__main__":    

    window=Tk()


    window.title("Calculator")
    window.geometry=("325x175")
    window.configure(bg="light green")
    equation = StringVar()
    input_field = Entry(window, textvariable=equation)
    input_field.grid(columnspan=4, ipadx=70)

    button1=Button(window,text='1',command=lambda: press(1),height=1,width=7)
    button1.grid(row=1,column=0)
    
    button2=Button(window,text='2',command=lambda: press(2),height=1,width=7)
    button2.grid(row=1,column=1)
    button3=Button(window,text='3',command=lambda: press(3),height=1,width=7)
    button3.grid(row=1,column=2)
    button4=Button(window,text='4',command=lambda: press(4),height=1,width=7)
    button4.grid(row=2,column=0)
    button5=Button(window,text='5',command=lambda: press(5),height=1,width=7)
    button5.grid(row=2,column=1)
    button6=Button(window,text='6',command=lambda: press(6),height=1,width=7)
    button6.grid(row=2,column=2)
    button7=Button(window,text='7',command=lambda: press(7),height=1,width=7)
    button7.grid(row=3,column=0)
    button8=Button(window,text='8',command=lambda: press(8),height=1,width=7)
    button8.grid(row=3,column=1)
    button9=Button(window,text='9',command=lambda: press(9),height=1,width=7)
    button9.grid(row=3,column=2)
    button0=Button(window,text='0',command=lambda: press(0),height=1,width=7)
    button0.grid(row=4,column=1)


    plus = Button(window, text=' + ', fg='black', bg='red',command=lambda: press("+"), height=1, width=7)
    plus.grid(row=1, column=3)
    minus = Button(window, text=' - ', fg='black', bg='red',command=lambda: press("-"), height=1, width=7)
    minus.grid(row=2, column=3)
    multiply = Button(window, text=' x ', fg='black', bg='red',command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=3, column=3)
    division = Button(window, text=' / ', fg='black', bg='red',command=lambda: press("/"), height=1, width=7)
    division.grid(row=4, column=3)
    clear = Button(window, text='Clear', fg='black', bg='red',command=clear, height=1, width=7)
    clear.grid(row=4, column=0)
    equal = Button(window, text=' = ', fg='black', bg='grey',command=equalpress, height=1, width=7)
    equal.grid(row=5, column=3)
    point = Button(window, text=' . ', fg='black', bg='red',command=lambda:press("."), height=1, width=7)
    point.grid(row=4, column=2)











window.mainloop()
