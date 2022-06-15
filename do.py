import tkinter as tk

f = ("system", 10)
f2 = ('system',40)

def dark_mode():
    try:
        tt_lb.configure(bg='#222222',foreground='white')
    except:
        pass
    bt.pack()
    bt2.place_configure(x=1000,y=1000)
    bt.place_configure(x=590,y=9)
    bt2.configure(bg='#333333',foreground='white')
    window.configure(bg='#222222')
    button5.configure(bg='#333333',foreground="white")
    button2.configure(bg='#333333',foreground="white")
    button.configure(bg='#333333',foreground="white")
    button3.configure(bg='#333333',foreground="white")
    title_label.configure(bg='#222222',foreground="white")
    title_label2.configure(bg='#222222',foreground="white")
    title_label3.configure(bg='#222222',foreground="white")
    title_label4.configure(bg='#222222',foreground="white")
    title_label5.configure(bg='#222222',foreground="white")
    number_input.configure(bg='#222222',foreground="white")
    number_input2.configure(bg='#222222',foreground="white")
    number_input3.configure(bg='#222222',foreground="white")
    number_input4.configure(bg='#222222',foreground="white")
    number_input5.configure(bg='#222222',foreground="white")
    output_lable.configure(bg='#222222',foreground="white")
    output_lable2.configure(bg='#222222',foreground="white")
    textop.configure(bg='#222222',foreground="white")

def white_mode():
    try:
        tt_lb.configure(bg='white',foreground='black')
    except:
        pass
    bt.place_configure(x=1000,y=1000)
    bt2.place_configure(x=590,y=9)
    bt2.configure(bg='white',foreground='black')
    window.configure(bg='white')
    button5.configure(bg='white',foreground="black")
    button2.configure(bg='white',foreground="black")
    button.configure(bg='white',foreground="black")
    button3.configure(bg='white',foreground="black")
    title_label.configure(bg='white',foreground="black")
    title_label2.configure(bg='white',foreground="black")
    title_label3.configure(bg='white',foreground="black")
    title_label4.configure(bg='white',foreground="black")
    title_label5.configure(bg='white',foreground="black")
    number_input.configure(bg='white',foreground="black")
    number_input2.configure(bg='white',foreground="black")
    number_input3.configure(bg='white',foreground="black")
    number_input4.configure(bg='white',foreground="black")
    number_input5.configure(bg='white',foreground="black")
    output_lable.configure(bg='white',foreground="black")
    output_lable2.configure(bg='white',foreground="black")
    textop.configure(bg='white',foreground="black")



def mode1():
    title_label2.pack_forget()
    title_label4.pack_forget()
    title_label5.pack_forget()
    title_label3.pack_forget()
    number_input2.pack_forget()
    number_input3.pack_forget()
    number_input4.pack_forget()
    output_lable2.pack_forget()
    title_label3.pack_forget()
    textop.pack_forget()
    textop.place_configure(x=10000,y=10000)
    tt_lb.destroy()
    button2.pack_forget()
    number_input5.pack_forget()
    number_input5.place_configure(x=10000, y=10000)
    title_label.pack(pady= 10)
    number_input.pack(padx=5)
    button.pack(pady= 10)
    output_lable.pack(pady= 10)

def mode2():
    title_label.pack_forget()
    number_input.pack_forget()
    button.pack_forget()
    output_lable.pack_forget()
    tt_lb.destroy()
    title_label2.pack(pady= 10)
    title_label3.pack(pady=2)
    number_input2.pack()
    title_label4.pack(pady=2)
    number_input3.pack()
    title_label5.pack(pady=2)
    number_input4.pack()
    button2.pack(pady=10)
    output_lable2.pack(pady=40)
    number_input5.pack()
    number_input5.place_configure(x=570,y=100)
    textop.pack()
    textop.place_configure(x=520,y=75)

def mode_3():
    title_label_m3.pack(pady=10)
    number_input_m3.pack(padx=5)
    number_input_m3_2.pack()
    number_input_m3_2.place_configure(x=570,y=100)
    button_m3.pack(pady=10)
    output_lable_m3.pack(pady=10)

    title_label.pack(pady= 10)
    number_input.pack(padx=5)
    button.pack(pady= 10)
    output_lable.pack(pady= 10)

    title_label.pack_forget()
    number_input.pack_forget()
    button.pack_forget()
    output_lable.pack_forget()
    tt_lb.destroy()
    title_label2.pack_forget()
    title_label3.pack_forget()
    number_input2.pack_forget()
    title_label4.pack_forget()
    number_input3.pack_forget()
    title_label5.pack_forget()
    number_input4.pack_forget()
    button2.pack_forget()
    output_lable2.pack_forget()
    number_input5.place_configure(x=10000, y=10000)
    textop.place_configure(x=10000,y=10000)


def spuar():
    number = 0
    number2 = 0
    number3 = 0
    try:
        number = float(number_input2.get())
        if number == 0:
            raise Exception()
        number2 = float(number_input3.get())
        if number2 == 0:
            raise Exception()
        number3 = float(number_input4.get())
        if number3 == 0:
            raise Exception()
        oo = int(number_input5.get())
        if oo == 0:
            raise Exception()
    except:
        output_lable2.configure(text="กรุณากรอกข้อมูลให้ถูกต้อง เพื่อการทำงานที่ถูกต้อง")
        return
    uoy = 1
    la = uoy * number
    uoy = la
    la2 = uoy * number2
    uoy = la2
    la3 = uoy * number3
    p = (f'%.{oo}f' %la3)
    output_lable2.configure(text=p)

def show_output():
    number = 0
    try:
        number = int(number_input.get())
        if number == 0:
            raise Exception()
    except:
        output_lable.configure(text="กรุณากรอกข้อมูลให้ถูกต้อง เพื่อการทำงานที่ถูกต้อง")
        return

    output = ''
    for pong in range(1, 13):
        output += str(number) + " x " + str(pong)
        output += " = " + str(number * pong) + "\n"

    output_lable.configure(text= output)

window = tk.Tk()
window.title("SUPANAT hub help for math")
window.option_add('*Font', 'Times')
window.geometry('700x500')
window.resizable(0,0)
window.configure(background='#222222')

button5 = tk.Button(
    master=window, text= "mode 1",
    command=mode1, width= 5, height= 1,
    bg='#333333',
    foreground='white'
)
button5.pack(padx=5)
button5.place_configure(x=10, y=9)

button3 = tk.Button(
    master=window, text= "mode 2",
    command=mode2, width= 5, height= 1,
    bg='#333333',
    foreground='white'
)
button3.pack(padx=5)
button3.place_configure(x=80, y=9)

button_m3_select = tk.Button(
    master=window, text= "mode 3",
    command=mode_3, width= 5, height= 1,
    bg='#333333',
    foreground='white'
)
button_m3_select.pack(padx=5)
button_m3_select.place_configure(x=150 , y=9)

tt_lb = tk.Label(master=window, text='โปรดเลือกโหมด.',font=f2,bg='#222222',foreground="white")
tt_lb.pack()
tt_lb.place_configure(x=175,y=230)

#mode1
title_label = tk.Label(master=window, text="โปรดใส่แม่สูตรคูณที่ต้องการ",bg='#222222',foreground="white")
number_input = tk.Entry(master=window, width= 20,bg='#222222',foreground="white")
button = tk.Button(
    master=window, text= "ค้นหา",
    command=show_output, width= 15, height= 1,
    bg='#333333',
    foreground="white"
)
output_lable = tk.Label(master=window,bg='#222222',foreground="white")

#mode2
textsp = tk.StringVar()
textsp.set('1')
title_label2 = tk.Label(master=window, text="ปริมาตร ทรงสี่เหลี่ยมมุมฉาก",bg='#222222',foreground="white")
title_label3 = tk.Label(master=window, text="ความกว้าง",bg='#222222', font=f,foreground="white")
number_input2 = tk.Entry(master=window, width= 20,bg='#222222',foreground="white")
title_label4 = tk.Label(master=window, text="ความยาว",bg='#222222', font=f,foreground="white")
number_input3 = tk.Entry(master=window, width= 20,bg='#222222',foreground="white")
title_label5 = tk.Label(master=window, text="ความสูง",bg='#222222', font=f,foreground="white")
number_input4 = tk.Entry(master=window, width= 20,bg='#222222',foreground="white")
number_input5 = tk.Entry(master=window, width= 5,textvariable=textsp,bg='#222222',foreground="white")
textop = tk.Label(master=window,text='จำนวนทศนิยม [อย่างน้อย 1]',bg='#222222', font=f,foreground="white")
button2 = tk.Button(
    master=window, text= "คำนวน",
    command=spuar, width= 15, height= 1,
    bg='#333333',
    foreground="white"
)
output_lable2 = tk.Label(master=window,font=100,bg='#222222',foreground='white')

bt2 = tk.Button(
    master=window, text= "dark mode",
    command=dark_mode, width= 8, height= 1,
    bg='#333333',
    foreground='white'
)
bt2.place_configure(x=590, y=9)

bt = tk.Button(
    master=window, text= "white mode",
    command=white_mode, width= 8, height= 1,
    bg='#333333',
    foreground='white'
)
bt.place_configure(x=590, y=9)

# mode_3
title_label_m3 = tk.Label(master=window, text="โปรดใส่แม่สูตรคูณที่ต้องการ",bg='#222222',foreground="white")
number_input_m3 = tk.Entry(master=window, width= 20,bg='#222222',foreground="white")
number_input_m3_2 = tk.Entry(master=window, width= 5,textvariable=textsp,bg='#222222',foreground="white")
button_m3 = tk.Button(
    master=window, text= "ค้นหา",
    command=mode_3, width= 15, height= 1,
    bg='#333333',
    foreground="white"
)
output_lable_m3 = tk.Label(master=window,bg='#222222',foreground="white")



window.mainloop()