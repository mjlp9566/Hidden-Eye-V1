import subprocess
import sys,os
import xmltodict

py_path=sys.executable
cap_path=os.getcwd()
path = os.path.expanduser('~')
final_path='''"'''+py_path+" "+cap_path+"capture.py"+'''"'''
print(final_path)
    
def update(xml_file_path):
    try:
        with open(xml_file_path, 'r') as xml_file:
            task_dict = xmltodict.parse(xml_file.read())

        task_dict['Task']['Settings']['ExecutionTimeLimit'] = 'PT0S'    #Setting Execution limit->0 (by default the windows task will have execution limit of 3days)

        if 'Task' in task_dict and 'Settings' in task_dict['Task']:
            settings = task_dict['Task']['Settings']
            if 'DisallowStartIfOnBatteries' in settings:
                settings['DisallowStartIfOnBatteries'] = 'false'  
            if 'StopIfGoingOnBatteries' in settings:
                settings['StopIfGoingOnBatteries']='false'              #setting this as false to run the task even if the laptop runs in batteries (by default this will be true so when the laptop is not connected with charger(AC power) the task will not be active)

        updated_xml = xmltodict.unparse(task_dict,encoding="UTF-16", pretty=True)
        with open(xml_file_path, 'w') as updated_file:
            updated_file.write(updated_xml)

        print(f"The 'DisallowStartIfOnBatteries' setting has been updated in '{xml_file_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")



   
while(True):
    print("""
     1.)ENABLE
     2.)DISABLE
     3.)EXIT
     """)
    a=int(input("Enter Option:"))
    if(a==1):
     subprocess.run("""schtasks /Create /TN "MONITOR"  /TR """+final_path+""" /SC ONEVENT /EC Security /MO *[System[EventID=4625]] /F""")
     with open("TaskSettings.xml", "w") as file:
      process = subprocess.Popen("""schtasks /Query /TN "MONITOR" /XML""", shell=True, text=True, stdout=file, stderr=subprocess.PIPE)
      process.wait()    
     update(cap_path+"TaskSettings.xml")
     print("success")
     subprocess.run("""schtasks /Create /XML """+"TaskSettings.xml" +""" /TN "MONITOR" /F""")

    elif(a==2):
     subprocess.run('''schtasks /Change /TN "MONITOR" /DISABLE''')
     subprocess.run('''schtasks /Change /TN "MONITOR1" /DISABLE''')
    else:
        break


#The task property editor dialouge can't be called using python
#schtasks command can't edit the power setting
#so that a task is created
#the xml is extracted and modified for the above changes
#new task is created using the modified xml.
