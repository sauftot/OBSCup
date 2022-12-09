import obspython as OBS
import json

data = lambda: ...
data.path = ''
data.running = False
data.syncTime = False


### THREADS







### OBS CALLBACKS

# callback for user setting a file path value in script settings
def cbFilePath(props, prop, settings):
    j = OBS.obs_data_get_json(settings)
    jObj = json.loads(j)
    if "Time File" in j:
        d = str([jObj["Time File"]])
        n = d.replace("[", "")
        m = n.replace("]", "")
        k = m.replace("\'", "")
        data.path = k
        print("INFO.PATH: " + data.path)

# callback for setting the chrono code
def cbChronoCode(props, prop, settings):
    None

# callback for our toggle button
def cbStartButton(props, prop, settings):
    None




### OBS Functions
        
def script_load(settings):
    print("INFO: timeSynchro loaded.")

def script_unload():
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
    startButton = OBS.obs_properties_add_button(sSettings, 'Start', 'Start')
    OBS.obs_property_set_visible(startButton, True)
    OBS.obs_property_set_modified_callback(startButton, cbStartButton)
    return sSettings

def script_description():
    return "Select the txt timer file for OBS, then paste your chronograph io link into the text box."