import json
import os
import subprocess
import time

class AnalysedFile:
    def __init__(self, path, messages):
        self.path = path
        self.messages = messages

class AnalyseMsg:
    def __init__(self, id, message, line, suggestions = []):
        self.id = id
        self.message = message
        self.line = line
        self.suggestions = suggestions

def analyze(dir, console):
    #Начало отсчёта времени исполнения анализа
    start_time = time.perf_counter()
    subprocess.run(["npx", "eslint", ".", "-f", "json", "--output-file", "eslint-report.json"], cwd=dir, shell=True)
    output = []
    analyzeStatistic = {}
    IssuesTotal = 0
    try:
        with open(f'{dir}/eslint-report.json', 'r', encoding="utf8") as file:
            data = json.load(file)
            for i in data:
                messages = i["messages"]
                analysedMsg = []
                for j in messages:
                    if "suggestions" in j:
                        suggestions = j["suggestions"]
                        finalSuggestions = []
                        for k in suggestions:
                            finalSuggestions.append(k["desc"])
                        analysedMsg.append(AnalyseMsg(j["messageId"],j["message"],j["line"],finalSuggestions))
                        IssuesTotal +=1
                        if not j["messageId"] in analyzeStatistic:
                            analyzeStatistic[j["messageId"]] = 1
                        else:
                            analyzeStatistic[j["messageId"]] += 1
                    else:
                        analysedMsg.append(AnalyseMsg(j["messageId"],j["message"],j["line"]))
                    
                output.append(AnalysedFile(i["filePath"],analysedMsg))
        console.log(f"Analysis complete. Scanned {len(output)} files.")
        #Оканчание отсчёта времени исполнения
        console.log(f"Analysis execution finished for {time.perf_counter()-start_time}")
        return [output, analyzeStatistic, IssuesTotal]
    except Exception as error:
        console.error(f"Error during analysing {dir}, {error}")
        #Оканчание отсчёта времени исполнения
        console.log(f"Analysis execution finished for {time.perf_counter()-start_time}")
        return []
    