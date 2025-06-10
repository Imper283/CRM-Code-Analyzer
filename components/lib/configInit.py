import subprocess
import os
import shutil
import time

def initEslintAt(dir, console):
    #Начало отсчёта времени исполнения анализа
    start_time = time.perf_counter()
    try:
        subprocess.run(["npm", "install", "eslint", "--save-dev"], cwd=dir, shell=True)
        console.log(f"Inited npm dependency {dir}")
        #Оканчание отсчёта времени исполнения
        console.log(f"Npm initialization finished for {time.perf_counter()-start_time}")
        return True
    except:
        console.error(f"Failed init npm dependency at {dir}")
        return False

def initConfigAt(dir,console):
    #Начало отсчёта времени исполнения анализа
    start_time = time.perf_counter()
    configPath = os.path.join(os.getcwd(),"components","lib","configData","eslint.config.mjs")
    print(configPath)
    try:
        shutil.copy(configPath,dir)
        console.log(f"Config file created at {dir}")
        #Оканчание отсчёта времени исполнения
        console.log(f"Config initialisation finished in {time.perf_counter()-start_time}")
        return True
    except Exception as error:
        console.error(f"Failed creation of the config file at {dir}, error: {error}")
        return False
