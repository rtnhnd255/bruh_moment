import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("Сектора")
        # setting window size
        width = 355
        height = 483
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        data_source_button = tk.Button(root)
        data_source_button["bg"] = "#f0f0f0"
        data_source_button["cursor"] = "spraycan"
        ft = tkFont.Font(family='Times', size=10)
        data_source_button["font"] = ft
        data_source_button["fg"] = "#000000"
        data_source_button["justify"] = "center"
        data_source_button["text"] = "Выберите источник данных"
        data_source_button.place(x=50, y=130, width=264, height=81)
        data_source_button["command"] = self.pick_data_source

        start_button = tk.Button(root)
        start_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        start_button["font"] = ft
        start_button["fg"] = "#000000"
        start_button["justify"] = "center"
        start_button["text"] = "Старт"
        start_button.place(x=50, y=290, width=266, height=81)
        start_button["command"] = self.start_computing

    def pick_data_source(self):
        file_name = filedialog.askopenfilename(
            #filetypes=(("TXT files", "*.txt"))
        )
        f = open(file_name, 'r')

    def start_computing(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
