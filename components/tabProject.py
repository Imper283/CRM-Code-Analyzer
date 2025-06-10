import customtkinter as ctk
from .subcomponents.project.compStatus import Status as compStatus
from .subcomponents.project.compControls import Controls as compControls
from .subcomponents.project.compAnalyse import Analysis as compAnalysis

class Project(ctk.CTkFrame):
    def __init__(self, master, console):
        super().__init__(master)
        self.projectLabel = ctk.CTkLabel(self, text="Initialize your project first", font=("Arial",28)); self.projectLabel.grid()
        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=2, uniform="a")
        self.rowconfigure((0,1), weight=1, uniform="a")
        self.console = console
        self.status = compStatus(self); self.status.grid(row=0, column=0, sticky="nsew")
        self.analysis = compAnalysis(self,self.console,self.status); self.analysis.grid(row=0, column=1, rowspan=2, sticky="nsew", pady=4)
        self.controls = compControls(self,self.console,self.status, self.analysis); self.controls.grid(row=1, column=0, sticky="nsew", pady=4)
        self.pack(expand=True,fill="both")