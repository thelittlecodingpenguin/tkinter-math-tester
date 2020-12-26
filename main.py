# Imports
from tkinter import *
from tkinter import messagebox
from random import *

root = Tk()
root.geometry("650x650") 
root.title("Math Tester")

eq = ["*", "%", "-", "+", "/", "**"]
  
def Take_input(e, q1, q2, inputtxt, Output):
  answer = int(eval(str(q1) + e + str(q2)))

  try:
    input_answer = int(inputtxt.get("1.0", "end-1c").strip()) 
  except:
    messagebox.showerror("Error", "Invalid number")
    exit()

  if input_answer == answer: 
    Output.insert(END, 'Correct') 
    Output.pack()
  else: 
    Output.insert(END, "Wrong answer")
    Output.pack()
  
  answer = messagebox.askquestion("Continue", "Continue? ")
  if answer.lower() == "yes":
    main()
  else:
    root.destroy()
    exit()

def destroy():
  for child in root.winfo_children():
    child.destroy()

def main():
  destroy()
  
  # Pick random things
  num1 = randint(0, 10)
  num2 = randint(0, 10)

  e = choice(eq)
        
  l = Label(text = "What is " + str(num1) + e + str(num2) + " ? ")
  
  inputtxt = Text(root, height = 10, 
                  width = 25, 
                  bg = "light yellow") 
    
  Output = Text(root, height = 5,  
                width = 25,  
                bg = "light cyan")
    
  Display = Button(root, height = 2, 
                  width = 20,  
                  text ="Show", bg="green",
                  command = lambda: Take_input(e, num1, num2, inputtxt, Output))
  
  exit = Button(root, height = 2, width = 20, text="EXIT", fg="yellow", bg="red", command=root.destroy)
                  
    
  # Pack buttons and labels/texts
  l.pack() 
  exit.pack()
  
  inputtxt.pack() 
  Display.pack()

start_game = Button(root, text="Start", height=2, width=20, fg="white", bg="purple", command=main)
start_game.pack()

root.mainloop()
