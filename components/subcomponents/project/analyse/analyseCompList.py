import customtkinter as ctk
import components.lib.analyze as analyze

class AnalysisList(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, border_width=2)
        self.pack(expand=True, fill="both")
    
    def addElems(self, AnalysisResult: analyze.AnalysedFile):
        for file in AnalysisResult:
            FileAnalysisResult(self, file)

class ListElem(ctk.CTkFrame):
    def __init__(self, master, label, isScrollable=True):
        super().__init__(master)
        self.isCollapsed = True
        self.header = ctk.CTkFrame(self)
        self.headerLabel = ctk.CTkLabel(self.header, text=label, justify="left"); self.headerLabel.grid(row=0, column=0, sticky="nsew", pady=4)
        self.headerExpandBtn = ctk.CTkButton(self.header, text="Expand", command=self.toggle); self.headerExpandBtn.grid(row=0, column=2, sticky="nsew", pady=4)
        self.deleteBtn = ctk.CTkButton(self.header, text="Delete", command=lambda: self.destroy()); self.deleteBtn.grid(row=0, column=1, sticky="nsew", pady=4)

        if isScrollable:
            self.content = ctk.CTkScrollableFrame(self)
        else:
            self.content = ctk.CTkFrame(self)
        
        self.header.columnconfigure(0, weight=4, uniform="a")
        self.header.columnconfigure(1, weight=1, uniform="a")
        self.header.columnconfigure(2, weight=1, uniform="a")
        self.header.rowconfigure(0, weight=1, uniform="a")
        self.header.pack(expand=True,fill="x",pady=2)
        self.pack(expand=True,fill="x",pady=2)
    
    def toggle(self):
        if self.isCollapsed:
            self.isCollapsed = False
            self.headerExpandBtn.configure(text="Collapse")
            self.content.pack(expand=True,fill="x")
        else:
            self.isCollapsed = True
            self.headerExpandBtn.configure(text="Expand")
            self.content.pack_forget()

class FileAnalysisResult(ListElem):
        def __init__(self, master, analysedFile: analyze.AnalysedFile):
            if not isinstance(analysedFile, analyze.AnalysedFile):
                return
            if len(analysedFile.messages) > 0:
                super().__init__(master, analysedFile.path)
                for i in analysedFile.messages:
                    if len(i.suggestions)>0:
                        msg = ListElem(self.content, i.id)
                        ctk.CTkLabel(msg.content, text=f"Issue: {i.message} at line {i.line}", anchor="nw", justify="left").pack()
                        for j in i.suggestions:
                            label = ctk.CTkLabel(msg.content, text=f"Suggestion: {j}", anchor="nw", justify="left"); label.pack()
                        msg.pack()
                    else:
                        msg = ListElem(self.content, i.id, False)
                        ctk.CTkLabel(msg.content, text=f"Issue: {i.message} at line {i.line}", anchor="nw", justify="left").pack()
                        msg.pack()