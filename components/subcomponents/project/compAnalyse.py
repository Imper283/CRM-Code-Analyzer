import customtkinter as ctk
from .analyse.analyseCompList import AnalysisList as compList
from .analyse.analyseCompPrognosis import Prognosis as compPrognosis


class Analysis(ctk.CTkFrame):
    def __init__(self, master, console, status):
        super().__init__(master, border_width=2)

        self.statusLabel = ctk.CTkLabel(self, text="Analysis", font=("Arial",21)); self.statusLabel.pack(pady=2)
        self.notebook = ctk.CTkTabview(self)
        self.notebook.add("Results")
        self.notebook.add("Prognosis")
        self.notebook.pack(expand=True,fill="both",padx=2,pady=2)
        self.list = compList(self.notebook.tab("Results"))
        self.prognosis = compPrognosis(self.notebook.tab("Prognosis"))
        # self.container = ctk.CTkFrame(self, border_width=1); self.container.pack(pady=2, expand=True, fill="both")



