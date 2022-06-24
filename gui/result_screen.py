import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 1200
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_363 = tk.Button(root)
        GButton_363["bg"] = "#f0f0f0"
        GButton_363["cursor"] = "spraycan"
        ft = tkFont.Font(family='Times', size=10)
        GButton_363["font"] = ft
        GButton_363["fg"] = "#000000"
        GButton_363["justify"] = "center"
        GButton_363["text"] = "Сохранить разбиение"
        GButton_363.place(x=30, y=210, width=264, height=81)
        GButton_363["command"] = self.GButton_363_command

        c = tk.Canvas(root, width=700, height=500, bg='white')
        c.place(x=300, y=40)

    def GButton_363_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
