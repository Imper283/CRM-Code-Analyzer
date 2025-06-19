import customtkinter as ctk
import time
import clipboard
from tkinter import filedialog
class Console(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=25, uniform="b")
        self.columnconfigure(0, weight=1, uniform="b")

        self.consoleControls = ctk.CTkFrame(self)
        self.consoleControls.rowconfigure(0,weight=1, uniform="c")
        self.consoleControls.columnconfigure(0,weight=5, uniform="c")
        self.consoleControls.columnconfigure(1,weight=5, uniform="c")
        self.consoleControls.columnconfigure(2,weight=5, uniform="c")

        self.consoleControls.grid(row=0, column=0, sticky="nsew")

        self.consoleSaveBtn = ctk.CTkButton(self.consoleControls, corner_radius=10, text="Save", command=self.__saveToFile)
        self.consoleSaveBtn.grid(row=0, column=0, sticky="nsew")

        self.consoleClipboardBtn = ctk.CTkButton(self.consoleControls, corner_radius=10, text="Save to clipboard", command=self.__saveToClipboard)
        self.consoleClipboardBtn.grid(row=0, column=1, sticky="nsew")

        self.consoleClearBtn = ctk.CTkButton(self.consoleControls, corner_radius=10, text="Clear console", command=self.__clearLogs)
        self.consoleClearBtn.grid(row=0, column=2, sticky="nsew")

        self.consoleContainer = ctk.CTkScrollableFrame(self); self.consoleContainer.grid(row=1, column=0, sticky="nsew")
        self.console = ctk.CTkLabel(self.consoleContainer, anchor="nw", text="", justify="left")
        self.consoleData = ""
        self.pack(expand=True, fill="both")
        self.console.pack(expand=True, fill="both")
    
    def __calcTime(self):
        formatTime = lambda a: str(a) if len(str(a)) == 2 else "0"+str(a)
        return f"{formatTime(time.localtime().tm_hour)}:{formatTime(time.localtime().tm_min)}:{formatTime(time.localtime().tm_sec)}"

    def __saveToClipboard(self):
        clipboard.copy(self.consoleData)
    
    def __saveToFile(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        textToSave = str(self.consoleData) # starts from `1.0`, not `0.0`
        f.write(textToSave)
        f.close() # `()` was missing.
        
    def __clearLogs(self):
        self.consoleData = f"[{self.__calcTime()}][LOG]: Console cleared\n"
        self.console.configure(text=self.consoleData)

    def log(self, text):
        self.consoleData = f"{self.consoleData}[{self.__calcTime()}][LOG]: {text}\n"
        self.console.configure(text=self.consoleData)
    
    def error(self, text):
        self.consoleData = f"{self.consoleData}[{self.__calcTime()}][ERROR]: {text}\n"
        self.console.configure(text=self.consoleData)
    
    def warn(self, text):
        self.consoleData = f"{self.consoleData}[{self.__calcTime()}][WARN]: {text}\n"
        self.console.configure(text=self.consoleData)
