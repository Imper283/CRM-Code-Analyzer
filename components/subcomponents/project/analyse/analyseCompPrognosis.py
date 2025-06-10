from g4f.client import Client
import warnings
import customtkinter as ctk
warnings.filterwarnings("ignore")

class Prognosis(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, border_width=2)
        self.containerLabel = ctk.CTkLabel(self, text="Analyse before get any prognosis and recomendations")
        self.containerLabel.pack(expand=True,fill="both")
        self.pack(expand=True, fill="both")
    
    def prognose(self, dataToAnalyse):
        self.containerLabel.configure(text="Please wait for analyse completion")
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Твоя задача сделать прогнозы и дать советы по поведению проекта, на основе данных переданных тебе в json. Свой ответ давай кратко и чётко, в виде отчёта, с небольшим блоком рекомендаций. В данных у тебя будет статистика найденных в коде ошибок. Json для анализа:{dataToAnalyse}"}],
            web_search=False
        )
        self.containerLabel.configure(anchor="nw", justify="left", text=response.choices[0].message.content, wraplength=400)