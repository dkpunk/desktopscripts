import checkmaker_port_sdp2_telnet
from tkinter import *
top=Tk()
L1=Label(top,text="Port Number")
L1.pack(side=LEFT)
E1=Entry(top, bd =6)
E1.pack(side=RIGHT)
PortUI=E1.get()
print(PortUI)
portlist=PortUI.split(',')
print(portlist)
B=Button(top, text = "Submit", command = checkmaker_port_sdp2_telnet.makecheck(portlist))
B.pack(side=BOTTOM)
top.mainloop()