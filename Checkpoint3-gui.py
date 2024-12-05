import tkinter as tk
from PIL import ImageTk

# initiallize app
root = tk.Tk()
root.title("Database Station")

# Screen parameters
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.05)
root.geometry('900x900+' + str(x) + '+' + str(y))

# Frame for map
frame1 = tk.Frame(root, width=900, height=900)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# Widget for map
map_img = ImageTk.PhotoImage(file="station-map.png")
map_wid = tk.Label(frame1, image=map_img)
map_wid.image = map_img
map_wid.pack()

# run app
root.mainloop()