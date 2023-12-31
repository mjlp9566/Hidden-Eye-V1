# Hidden-Eye-V1👁️



<h2>Description</h2>
A python application for windows that monitor the login failed and success attempts and capture the picture of the intruder who  enters the password.

<h2>Methodology</h2>

In windows, The Login failed event will have an id `4625` and it will be stored in windows logs. By using the event id we can create a task attached to the event, so that whenever the event happens the task will be triggered and this task creation for the event can be done with the windows <b>schtasks</b> command. These process is automated using subprocess module and a python program to capture the image is attached to the task.

<h2>Usage</h2>

> <b>Note:</b> Run these below steps as Administrator. (open cmd/powershell as admin and run)

<ul>
  <li>STEP-1: Clone the repository (or) download it as zip file.
    <br><br>
    
  ```
  git clone https://github.com/mjlp9566/Hidden-Eye-V1.git
  ```
  
  </li>
  
  <li>STEP-2:Install requirements
  <br><br>

   ``` 
   cd Hidden-Eye-V1
   pip install -r requirements.txt
   ```
  </li>

  <li>STEP-3:Run the hidden_eye file
  <br><br>
    
  ```
  python hidden_eye.py
  ```
  </li>

  <li>STEP-4: Choose option-1 to enable the service

   ![271067997-57809855-343e-4730-b371-f4f75da84839](https://github.com/mjlp9566/Hidden-Eye-V1/assets/55002003/bb073101-4930-4894-ba86-ef2da01f087a)


  
  > <b>Note:</b> Once you enabled the program then don't need to start again.
    
  </li>
</ul>

<pre> If need to stop the service then run the <b>hidden_eye.py</b> program again and choose the second option.</pre>

>If your built-in camera notworking so you are using a external camera, Then change these in the capture.py-->camera = pygame.camera.Camera(camera_list[1],(640,480))


<h2>OUTPUT</h2>

![271072511-09ebd226-8b7e-494e-a5b9-b5d63b8a2207](https://github.com/mjlp9566/Hidden-Eye-V1/assets/55002003/041ab259-4899-47d4-b648-2e5c6bacb27f)



<ol>
<li>The logs and pictures will be stored inside the directory of the user  who enabled the service [C:\Users\$user]</li>
<li>If you logged-in as user ABC and enabled the service then the outputs will be under [C:\Users\ABC]</li>
</ol>



