import tkinter as tk
from PIL import ImageTk, Image
import skinswap


root = tk.Tk()
root.title('osu! SkinSwapper')
root.iconbitmap('C:\\Users\\Matthew\\Downloads\\ChikaAngry.ico')


img = ImageTk.PhotoImage(Image.open('C:\\Users\\Matthew\\Desktop\\Pictures\\weeb shit\\ChikaAngry.png'))
label = tk.Label(image=img)
label.grid(row=0, column=0, columnspan=2)

#canvas = tk.Canvas(root, height=700, width=500, bg='#ff66aa')
#canvas.pack()

run_program_button = tk.Button(root, text='Run', fg='white', bg='red', padx=15)
run_program_button.grid(row=1, column=1, sticky=tk.E)



root.mainloop()