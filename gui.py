import customtkinter as ctk
import components.tabConsole as compConsole
import components.tabProject as projectTab

app = ctk.CTk()
app.title("CRM Code Analyzer")
app.geometry("800x600") 
app.minsize(800,600) 

notebook = ctk.CTkTabview(master=app)
notebook.add("Project")
notebook.add("Console")
notebook.pack(expand=True, fill="both")

console = compConsole.Console(master=notebook.tab("Console"))
projectStatus = projectTab.Project(master=notebook.tab("Project"),console=console)



app.mainloop()