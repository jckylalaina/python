from app.views.index import *
from app.controllers.application_controller import *
import os

while True:
    
    i = index()
    
    if int(i) == 1:
        application_controller.new()

    elif int(i) == 2:
        application_controller.all_()
    
    elif int(i) == 3:
        application_controller.update()
    
    elif int(i) == 4:
        application_controller.delete()


os.system("black config/root.py")
