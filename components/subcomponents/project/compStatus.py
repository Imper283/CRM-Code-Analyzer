import customtkinter as ctk
class Status(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, border_width=2)

        self.statusLabel = ctk.CTkLabel(self, text="Status", font=("Arial",21)); self.statusLabel.pack(pady=2)
        self.container = ctk.CTkFrame(self, border_width=1); self.container.pack(pady=2, expand=True, fill="both")

        self.projDir = ""
        self.es = False
        self.configState = False
        self.issues = -1

        self.statusContent = ctk.CTkLabel(self.container, justify="left", text="Initialize project at first", font=("Arial",16), anchor="nw"); self.statusContent.pack(pady=5,padx=8, expand=True, fill="both")

    
    def updateStatus(self):
        statusText = ""

        if self.es:
            statusText = "ESLint status: Installed"
        else:
            statusText = "ESLint status: Not installed"
        
        if self.configState:
            statusText = f"{statusText}\nESLint config: Present"
        else:
            statusText = f"{statusText}\nESLint config: Not exist"
        
        if self.issues == -1:
            statusText = f"{statusText}\nIssues: Run analyze first"
        elif self.issues == 0:
            statusText = f"{statusText}\nIssues: No issues has been found!"
        else:
            statusText = f"{statusText}\nIssues: {self.issues} was found"
        
        if self.projDir != "":
            statusText = f"{statusText}\nProject dir: {self.projDir}"

        self.statusContent.configure(text=statusText)