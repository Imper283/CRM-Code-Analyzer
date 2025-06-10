import customtkinter as ctk
from tkinter import filedialog
import components.lib.scanner as scanner
import components.lib.configInit as configInit
import components.lib.analyze as analyze
import time

class Controls(ctk.CTkFrame):
    def __init__(self, master, console, status, analysis):
        super().__init__(master, border_width=2)
        self.elementsGap = 5
        self.label = ctk.CTkLabel(self, text="Controls", font=("Arial",21)); self.label.pack(pady=2)
        self.container = ctk.CTkScrollableFrame(self, border_width=1); self.container.pack(pady=2, expand=True, fill="both")
        
        self.projectSelectBtn = ctk.CTkButton(self.container, text="Select Project", command=self.__select_project); self.__enableBtn(self.projectSelectBtn)
        self.projectRunAnalyze = ctk.CTkButton(self.container, text="Analyze", state="disabled", command=self.__analyzeProject)
        self.projectSetupBtn = ctk.CTkButton(self.container, text="Auto setup", state="disabled", command=self.__initConfig)
        self.projectRunDBScan = ctk.CTkButton(self.container, text="Check DB", state="disabled")

        self.projectCheckState = ctk.CTkButton(self.container, text="Check ESLint", state="disabled", command=lambda: self.__scanDir(self.projectDir))

        self.console = console
        self.status = status
        self.analysis = analysis.list
        self.prognosis = analysis.prognosis
    
    def __disableBtn(self, element):
        element.configure(state="disabled"); element.pack_forget()
    
    def __enableBtn(self, element):
        element.configure(state="normal"); element.pack(pady=self.elementsGap, fill="x")
    
    def __initConfig(self):
        dir = self.status.projDir
        if dir == "":
            self.console.error("No project directory, to init config at!")
        else:
            if not self.status.es:
                configInit.initEslintAt(dir,self.console)
            if not self.status.configState:
                configInit.initConfigAt(f"{dir}/",self.console)
            self.__scanDir(dir)

    def __scanDir(self, dir):
        #Начало отсчёта времени сканирования папки на корректность
        start_time = time.perf_counter()
        scanResult = scanner.scan(dir)
        #Оканчание отсчёта времени исполнения
        self.console.log(f"Directory scanning finished in {time.perf_counter()-start_time}")
        if scanResult[3]:
            self.console.error(scanResult[0])
            return
        else:
            self.console.log(f"{scanResult[0]}")
            self.__disableBtn(self.projectSelectBtn)
            self.__enableBtn(self.projectCheckState)

            if not self.status.es or not self.status.configState:
                self.__enableBtn(self.projectSetupBtn)
            else:
                self.__enableBtn(self.projectRunAnalyze)
                self.__disableBtn(self.projectSetupBtn)

            # self.projectRunDBScan.configure(state="normal")
            self.status.projDir = dir
            self.status.es = scanResult[1]
            self.status.configState = scanResult[2]
            self.status.updateStatus()
        return scanResult

    def __select_project(self):
        project_path = filedialog.askdirectory()
        scanResult = self.__scanDir(project_path)
        if not scanResult[3]:
            self.projectDir = project_path
    
    def __analyzeProject(self):
        results = analyze.analyze(self.status.projDir, self.console)
        if results != []:
            self.analysis.addElems(results[0])
            self.prognosis.prognose(results[1])
            self.status.issues = results[2]
            self.status.updateStatus()
        else:
            self.console.warn("Cant load analysis results")