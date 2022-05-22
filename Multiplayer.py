from tkinter import *
import socket
import threading
c = socket.socket()
c.connect(('localhost',9999))
def disable(x):
    z = list(x)[-1]
    for i in lbutt:
        if "button"+z in i:
            exec(i+"[\"bg\"] = \'#e6b3ff'")
            exec(i+"[\"activebackground\"] = \'#e6b3ff'")
        if "button"+ z in i and i not in disabled:
            exec(i+"[\"state\"] = ACTIVE")
        
        elif "button"+ z not in i:
            exec(i+"[\"state\"] = DISABLED")
            exec(i+"[\"bg\"] = \"#ffe6ff\"")
            exec(i+"[\"activebackground\"] = \"#ffe6ff\"")
def listen():
    global last_move
    while True:
        msg = c.recv(2048).decode()
        print(msg)
        enableall()
        if msg == "X":
            last_move = "X"
        elif msg == "O":
            last_move = "O"
        elif "button" in msg:
            disable(msg)
            if last_move == "O":
                exec(msg+"[\"text\"] = \"X\"")
                exec(msg+"[\"state\"] = DISABLED")
                disabled.append(msg)
                dic[msg] = "X"
            elif last_move == "X":
                exec(msg+"[\"text\"] = \"O\"")
                exec(msg+"[\"state\"] = DISABLED")
                disabled.append(msg)
                dic[msg] = "O"
def disableall():
    for i in lbutt:
        exec(f"{i}[\"state\"] = DISABLED")
def enableall():
    for i in lbutt:
        if i not in disabled:
            exec(f"{i}[\"state\"] = ACTIVE")
t = threading.Thread(target=listen)
t.start()
last_move = "X"
root = Tk()
root.configure(bg="black")
lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1,10)]) for x in range(1,10)]).split(",")
def make_grid(r,c):
    global count
    for i in range(r,r+3):
        for j in range(c,c+3):
            eval(f"{lbutt[count]}.grid(row={i},column={j},padx=2,pady=2)")
            count+=1
dic = dict(map(lambda e: (e," "),lbutt))
disabled = []
def change(x):
    global last_move
    c.send(bytes(x,"utf-8"))
    disable(x) 
    if last_move == "O":
        exec(x+"[\"text\"] = \"X\"")
        exec(x+"[\"state\"] = DISABLED")
        disabled.append(x)
        dic[x] = "X"
        last_move = "X"
        c.send(bytes("X","utf-8"))
    else:
        exec(x+"[\"text\"] = \"O\"")
        exec(x+"[\"state\"] = DISABLED")
        disabled.append(x)
        dic[x] = "O"
        last_move = "O"
        c.send(bytes("O","utf-8"))
    disableall()

for i in range(1,10):
    for j in range(1,10):
        exec(f"button{i}{j} = Button(root,text=\" \",font=\"Helvatica 15 bold\",padx=18,pady=8,width = 1,bg=\"#ffe6ff\",bd=0,command=lambda :change(\"button{i}{j}\"),state = NORMAL)")
count = 0
for i in range(0,10,4):
    for j in range(0,10,4):
        make_grid(i,j)
for i in [(0,3),(3,0),(0,7),(7,0)]:
    exec(f"l{i[0]+i[1]} = Label(text=\"\",font = \'Helvatica 1\',bg=\"black\",)")
    eval(f"l{i[0]+i[1]}.grid(row=i[0],column=i[1],pady=0)")

# canvas1 = Canvas(width=10,height=520,bg="red")
# canvas1.grid(row=0,column=4,columnspan=11)  
root.mainloop()
print(dic)
