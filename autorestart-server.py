import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from config import NGROK_COMMAND

class Handler(FileSystemEventHandler):
    def on_modified(self):
        print('Change detected, restarting python server and ngrok tunnel...')
        
        # execute command to run 'run-server.py' script
        server_process = subprocess.Popen(["python", "run-server.py"])
        
        # path to ngrok executable
        # ngrok_path = 'C:/Users/arjun/OneDrive/Desktop/CS Projects/FileBrowser/ngrok.exe'
        
        # construct ngrok command -- !!may need to replace "ngrok" with ngrok_path!!
        ngrok_command = NGROK_COMMAND
        
        # execute command to restart ngrok tunnel
        ngrok_process = subprocess.Popen(ngrok_command, shell=True)
        
        server_process.wait()
        ngrok_process.wait()
        
if __name__ == '__main__':
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()