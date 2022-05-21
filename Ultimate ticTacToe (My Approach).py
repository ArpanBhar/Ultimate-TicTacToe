from tkinter import *
root = Tk()
lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1,10)]) for x in range(1,10)]).split(",")
def make_grid(r,c):
    global count
    for i in range(r,r+3):
        for j in range(c,c+3):
            eval(f"{lbutt[count]}.grid(row={i},column={j})")
            count+=1
dic = dict(map(lambda e: (e," "),lbutt))
last_move = "O"
disabled = []
def change(x):
    global last_move
    z = list(x)[-1]
    for i in lbutt:
        if "button"+ z in i and i not in disabled:
            exec(i+"[\"state\"] = ACTIVE")
        elif "button"+ z not in i:
            exec(i+"[\"state\"] = DISABLED")
    if last_move == "O":
        exec(x+"[\"text\"] = \"X\"")
        exec(x+"[\"state\"] = DISABLED")
        disabled.append(x)
        dic["button"+x] = "X"
        last_move = "X"
    else:
        exec(x+"[\"text\"] = \"O\"")
        exec(x+"[\"state\"] = DISABLED")
        disabled.append(x)
        dic["button"+x] = "O"
        last_move = "O"

for i in range(1,10):
    for j in range(1,10):
        exec(f"button{i}{j} = Button(text=\" \",padx=20,pady=10,command=lambda :change(\"button{i}{j}\"),state = NORMAL)")
count = 0
for i in range(0,10,4):
    for j in range(0,10,4):
        make_grid(i,j)
for i in [(0,3),(3,0),(0,7),(7,0)]:
    exec(f"l{i[0]+i[1]} = Label(text=\"\", padx=10)")
    eval(f"l{i[0]+i[1]}.grid(row=i[0],column=i[1])")
root.mainloop()