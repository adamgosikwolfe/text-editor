from tkinter import * 
from tkinter import filedialog
from tkinter import font

root = Tk("Note Pad Basic")
text = Text(root)
text.grid()

def saveas():
	global text
	t = text.get("1.0", "end-1c")
	saveas.location = filedialog.asksaveasfilename()
	file1 = open(saveas.location, "w+")
	file1.write(t)
	file1.close()
	
saveas.location = ""

def save():
	global text
	t = text.get("1.0", "end-1c")
	if not saveas.location:
		saveas.location = filedialog.asksaveasfilename()
	file1 = open(saveas.location, "r")
	file1.write(t)
	file1.close()
	
def load():
	global text
	#t = text.get("1.0", "end-1c")
	loadlocation = filedialog.askopenfilename()
	file1 = open(loadlocation, "r")
	t = file1.read()
	file1.close()
	text.delete("1.0","end-1c")
	text.insert("1.0", t)
	
	
'''		
fonts = list(font.families())
fonts.sort()

font = Menubutton(root, text = "Fonts")
font.grid()
font.menu = Menu(font, tearoff = 0)
font["menu"] = font.menu
for item in fonts:
	font.menu.add_checkbutton(label=str(item), variable=str(item).lower(),command="Font" + str(item))
'''

#Menubar
menubar = Menu(root)

#File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=load)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=saveas)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
	
'''
def FontHelvetica():
    global text
    text.config(font="Helvetica")
def FontCourier():
    global text
    text.config(font="Courier")
font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable='helvetica',
command=FontHelvetica) '''

root.mainloop()

