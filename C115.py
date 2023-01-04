import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Rajesh Reddy/Downloads/test1"
to_dir = "C:/Users/Rajesh Reddy/Downloads/copyFiles-main"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):

    

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extension=os.path.splitext(event.src_path)
        time.sleep(5)
        print(name,extension)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                filename=os.path.basename(event.src_path)
                src = "C:/Users/Rajesh Reddy/Downloads/test1/"+filename
                dest = "C:/Users/Rajesh Reddy/Downloads/copyFiles-main/"+filename
                
                if os.path.exists(dest):
                    print("exists")
                    newfilename = os.path.splitext(filename)[0]+str(random.randint(0,999))+os.path.splitext(filename)[1]
                    newfilename = "C:/Users/Rajesh Reddy/Downloads/copyFiles-main/"+newfilename
                    shutil.move(src,newfilename)
                    print(newfilename)
                    
                else:
                    shutil.move(src,dest)

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()


while True:
    time.sleep(5)
    print("running...")

    
