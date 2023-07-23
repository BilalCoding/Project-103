import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/bilal/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path + " has been created!")
    def on_deleted(self, event):
        print(event.src_path + " has been deleted!")
    def on_modified(self, event):
        print(event.src_path + " has been modified!")
    def on_moved(self, event):
        print(event.src_path + " has been moved!")

event_handler = FileEventHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()

try:
    while True:
        print("Running...")
        time.sleep(3)
except KeyboardInterrupt:
    print("The program has been stopped.")
    observer.stop()