from tkinter import *
from tkinter.font import Font

#Создание окна
window = Tk()
window.title("Volleyball Scoreboard")
window.geometry('700x400')

#Первичная инициализация значений очков
myvar_score_left = StringVar()
myvar_score_right = StringVar()
myvar_score_left.set('0')
myvar_score_right.set('0')

#Первичная инициализация значений сетов
myvar_set_left = StringVar()
myvar_set_right = StringVar()
myvar_set_left.set('0')
myvar_set_right.set('0')


def UpdateSpin():
#Обновляем сеты команд
    set1 = spin_left.get()
    my_file = open("set1.txt", "w")
    my_file.write(set1)
    my_file.close()

    set2 = spin_right.get()
    my_file = open("set2.txt", "w")
    my_file.write(set2)
    my_file.close()
#Обновляем количество очков
    team_score_left = spin_big_left.get()
    my_file = open("score1.txt", "w")
    my_file.write(team_score_left)
    my_file.close()


    team_score_right = spin_big_right.get()
    my_file = open("score2.txt", "w")
    my_file.write(team_score_right)
    my_file.close()

def UpdateConnandName():
    #Обновляем название команд
    team_left = message_left.get()
    my_file = open("team1.txt", "w", encoding='utf-8')
    my_file.write(team_left)
    my_file.close()

    team_right = message_right.get()
    my_file = open("team2.txt", "w", encoding='utf-8')
    my_file.write(team_right)
    my_file.close()


def ResetSet():
    #Обновляем сеты нулями
    set1 = "0"
    my_file = open("set1.txt", "w")
    my_file.write(set1)
    my_file.close()

    set2 = "0"
    my_file = open("set2.txt", "w")
    my_file.write(set2)
    my_file.close()
    myvar_set_left.set("0")
    myvar_set_right.set('0')
    

def ResetScore():
    #Обновляем очки нулями
    team_score_left = "0"
    my_file = open("score1.txt", "w")
    my_file.write(team_score_left)
    my_file.close()


    team_score_right = "0"
    my_file = open("score2.txt", "w")
    my_file.write(team_score_right)
    my_file.close()
    myvar_score_left.set('0')
    myvar_score_right.set('0')
    
    


# Кнопки и их позиционирование
btn_update_all = Button(window, text="Обновить название команд", bg="white", fg="blue", command = UpdateConnandName)
btn_update_all.place(x=50, y=300, relwidth=0.2, relheight=0.1)

btn_reset_score = Button(window, text="Сбросить очки", bg="white", fg="blue", comman = ResetScore)
btn_reset_score.place(x=250, y=300, relwidth=0.2, relheight=0.1)

btn_reset_set = Button(window, text="Сбросить сеты", bg="white", fg="blue", command = ResetSet)
btn_reset_set.place(x=450, y=300, relwidth=0.2, relheight=0.1)





# Спины БОЛЬШИЕ боковые

spin_big_left = Spinbox(window, from_= 0, to=100, textvariable=myvar_score_left, width=3,
               font=Font(family='Helvetica', size=36, weight='bold'), command = UpdateSpin)
spin_big_left.place(x=50, y=100)
    #spin.pack()
spin_big_right = Spinbox(window, from_=0, to=100, textvariable=myvar_score_right, width=3,
               font=Font(family='Helvetica', size=36, weight='bold'), command = UpdateSpin)
spin_big_right.place(x=520, y=100)







#Спины МАЛЕНЬКИЕ посередине
#Левый
spin_left = Spinbox(window, from_=0, to=5, textvariable=myvar_set_left, width=3,
               font=Font(family='Helvetica', size=28, weight='bold'), command = UpdateSpin)
spin_left.place(x=250, y=50)
#Правый
spin_right = Spinbox(window, from_=0, to=5, textvariable=myvar_set_right, width=3,
               font=Font(family='Helvetica', size=28, weight='bold'), command = UpdateSpin)
spin_right.place(x=350, y=50)




#Левое текстовое поле
message_left = StringVar()
 
message_entry_left = Entry(textvariable = message_left)
message_entry_left.place(x = 110, y = 40,rely=.1, anchor="c")

label_team_left = Label(text="Название команды 1")
label_team_left.place(x = 50,y = 50)


#Правое текстовое поле

message_right = StringVar()
 
message_entry_right = Entry(textvariable = message_right)
message_entry_right.place(x = 580, y = 40,rely=.1, anchor="c")

label_team_right = Label(text="Название команды 2")
label_team_right.place(x = 520,y = 50)

 
#Надпись Сеты посередине

label_set = Label(text="Сеты",padx="20", pady="6", font="15")
label_set.pack(side = TOP )

#spin_big_left.update_idletasks()

window.mainloop()