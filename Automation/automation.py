from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import json
import time
folder_to_track = r'C:\Users\Nish\Desktop\myFolder'
folder_destination = r'C:\Users\Nish\Desktop\newFolder'


# This a child class of PatternMatchingEventHandler.
class MyHandler(PatternMatchingEventHandler):

    # We override a method from the parent class.
    def on_modified(self, event):
        # We iterate through the filenames of the folder to track, and
        # move them over to the destination folder.
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

event_handler = MyHandler()
Observer = Observer()
Observer.schedule(event_handler, folder_to_track, recursive=True)
Observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    Observer.stop()
Observer.join()
