# -*- coding: UTF-8 -*-
import tkinter as tk
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, height=100, width=200)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """Bind components and callback functions."""
        self.helloLabel = tk.Label(self, text="数据文件")
        self.helloLabel.pack()
        self.fileNameBox = tk.Entry(self)
        self.fileNameBox.pack()
        self.selectFileButton = tk.Button(
            self, text="选择", command=self.showOpenFileDialog)
        self.selectFileButton.pack()
        self.checkFileButton = tk.Button(
            self, text="检测", command=self.checkFile)
        self.checkFileButton.pack()

    def showOpenFileDialog(self):
        file_name = tk.filedialog.askopenfilename(
            filetypes=(("Data File", "*.csv"),), initialdir="./data")
        if file_name and file_name != "":
            self.fileNameBox.delete(0)
            self.fileNameBox.insert(0, file_name)

    def checkFile(self):
        file_name = self.fileNameBox.get()
        try:
            data = pd.read_csv(file_name)
        except:
            tk.messagebox.showerror("错误！", "文件错误，请重新选择。")
            return
        self.processData(data)

    def processData(self, data):
        print("Data ===========")
        print(data)
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def main():
    """Main function for kylab."""
    app = Application()
    app.master.title("数据处理")
    app.mainloop()


if __name__ == "__main__":
    main()
