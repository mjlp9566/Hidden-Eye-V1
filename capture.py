import pygame,os,datetime
import pygame.camera


path = os.path.expanduser('~')
print( path )

t=str(datetime.datetime.now())
time=str(datetime.datetime.now()).replace(":","_")
pygame.init()
pygame.camera.init()
camera_list = pygame.camera.list_cameras()
if not camera_list:
    print("No cameras found.")
    pygame.quit()
    exit()
camera = pygame.camera.Camera(camera_list[0],(640,480))
camera.start()
pygame.time.delay(1000)  
image = camera.get_image()
image_path = path+r"\captured_image_"+time+".png"
pygame.image.save(image, image_path)
print(f"Image captured and saved as {image_path}")
camera.stop()
pygame.quit()

file=open(path+r"\third_eye_log.txt","a")
file.write(t+" "+"Invalid login detected"+"\n")
file.close()





