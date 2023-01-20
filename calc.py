from tkinter import *
import math
from pygame import mixer
import pygame


mixer.init()
# setting up the click sound for the main buttons and calculator logo
button_click = mixer.Sound('music2.mp3')
equals_click = mixer.Sound('music1.mp3')

def quit(root):
    root.destroy()


def click(value):
    # setting the actions for the buttons pressed within the calculator

    ex = entryField.get()
    answer = ''
    try:

        # getting rid of the last value
        if value == 'C':
            ex = ex[0:len(ex)-1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()
            return

        elif value == 'CE':
            entryField.delete(0, END)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()
            return

        elif value == '√':
            answer = math.sqrt(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'π':
            answer = math.pi
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == '2π':
            answer = 2*math.pi
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'cosh':
            answer = math.cosh(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'tanh':
            answer = math.tanh(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'sinh':
            answer = math.sinh(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'ln':
            answer = math.log2(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'deg':
            answer = math.degrees(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == "rad":
            answer = math.radians(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'e':
            answer = math.e
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()

        elif value == 'Exit':
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()
            answer = quit(root)
            return

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()
            return

        elif value == '=':
            answer = eval(ex)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music1.mp3')
                pygame.mixer.music.play()

        else:
            entryField.insert(END, value)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play()
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except TypeError:
        pass
    except SyntaxError:
        pass


def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()


# setting up the calculator window via tkinter
root = Tk()
root.title('Smart Calculator')
root.config(bg='grey27')
root.geometry('680x486+100+100')


entryField = Entry(root, font = ('arial', 20, 'bold'), bg ='grey27', fg ='white', bd = 10, relief = SUNKEN, width = 30)

# 0 and 0 as they are the first thing being added at the top
entryField.grid(row=0, column=0, columnspan=8)

# adding the calculator logo image
logoImage = PhotoImage(file = 'logo.png')
logoLabel = Button(root, image = logoImage, bd=0, bg = 'grey27', activebackground = 'grey27',
                 command = audio)
logoLabel.grid(row = 0, column = 0)


# the text shown on the calculator buttons themselves
button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "Exit"]

rowvalue = 1
columnvalue = 0

for i in button_text_list:

    button = Button(root, width = 5, height = 2, bd = 2, relief = SUNKEN, text = i, bg ='grey27', fg ='white',
              font = ('arial', 18, 'bold'), activebackground ='grey27',
                    command = lambda button = i: click(button) )
    button.grid(row = rowvalue, column = columnvalue, pady = 1)

    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0


root.mainloop()
