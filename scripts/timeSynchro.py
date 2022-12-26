import obspython as OBS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import json, threading

data = lambda: ...
data.path = ''
data.code = ''
data.syncTime = False


"""
    TODO: SELECT TIMER FROM WEBSITE BY CLICK
    TODO: ADD COOLDOWN TO TOGGLE BUTTON
"""

def updaterThread():
    print("INFO: Thread started")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get('https://chronograph.io/' + data.code)
    oMinutes = 0
    oSeconds = 0
    sleep(5)
    
    while data.syncTime:
        try:
            minutes = int(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/h3/span[2]").text)
            seconds = int(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/h3/span[2]").text)
            if minutes != oMinutes or seconds != oSeconds:
                with open(data.path, 'w') as fh:
                    sec = str(seconds)
                    if seconds < 10:
                        sec = '0' + str(seconds)
                    fh.write(str(minutes) + ":" + sec)
                    fh.close()
                    oMinutes = minutes
                    oSeconds = seconds
        except NoSuchElementException:
            print("ERROR: Element not found")
        sleep(0.1)
    print("INFO: Thread stopped")





### OBS CALLBACKS

# callback for user setting a file path value in script settings
def cbFilePath(props, prop, settings):
    j = OBS.obs_data_get_json(settings)
    jObj = json.loads(j)
    if "Time File" in j:
        d = str([jObj["Time File"]])
        n = d.replace("[", "")
        m = n.replace("]", "")
        t = m.replace("\"", "")
        k = t.replace("\'", "")
        data.path = k

# callback for setting the chrono code
def cbChronoCode(props, prop, settings):
    j = OBS.obs_data_get_json(settings)
    jObj = json.loads(j)
    if "Chrono Code" in j:
        d = str([jObj["Chrono Code"]])
        n = d.replace("[", "")
        m = n.replace("]", "")
        t = m.replace("\"", "")
        k = t.replace("\'", "")
        data.code = k

# callback for our toggle button
def cbStartButton(props, prop, *args, **kwargs):
    if data.syncTime == False:
        t = threading.Thread(target=updaterThread)
        data.syncTime = True
        t.start()
    else:
        data.syncTime = False



### OBS Functions
        
def script_load(settings):
    print("INFO: timeSynchro loaded.")

def script_unload():
    data.syncTime = False
    print("INFO: timeSynchro unloaded.")

def script_properties():
    sSettings = OBS.obs_properties_create()
    # Time File Selector
    fileSel = OBS.obs_properties_add_path(sSettings, 'Time File', 'Time File', OBS.OBS_PATH_FILE, '', 'C:/')
    OBS.obs_property_set_visible(fileSel, True)
    OBS.obs_property_set_modified_callback(fileSel, cbFilePath)
    # Chronograph.io Code Setter
    chronoCode = OBS.obs_properties_add_text(sSettings, 'Chrono Code', 'Chrono Code', OBS.OBS_TEXT_DEFAULT)
    OBS.obs_property_set_visible(chronoCode, True)
    OBS.obs_property_set_modified_callback(chronoCode, cbChronoCode)
    # Start Button
    startButton = OBS.obs_properties_add_button(sSettings, 'Toggle', 'Toggle', cbStartButton)
    OBS.obs_property_set_visible(startButton, True)
    return sSettings

def script_description():
    return "Select the txt timer file for OBS, then paste your chronograph io code into the text box."