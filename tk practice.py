import tkinter as tk

window = tk.Tk()
window.title("배르주아")
window.geometry("700x500+100+150")
window.resizable(False, False)

label1 = tk.Label(window, text = "부피", width = 5)
label1.grid(row = 1, column = 0, sticky = tk.E)
button1 = tk.Button(window, text = "입력")
button1.grid(row = 1, column = 2)
entry1 = tk.Entry(window)
entry1.grid(row = 1, column = 1)

label2 = tk.Label(window, text = "투입량")
label2.grid(row = 3, column = 0, sticky = tk.E)
button2 = tk.Button(window, text = "입력")
button2.grid(row = 3, column = 2)
entry2 = tk.Entry(window)
entry2.grid(row = 3, column = 1)

image_path = r"C:\Users\FEELCOM\Desktop\코딩\tk test\a.png"
img = tk.PhotoImage(file = image_path)
label3 = tk.Label(window, image = img)
label3.grid(row = 6, column = 0)

window.mainloop()

