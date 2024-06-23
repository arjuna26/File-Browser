from config import NGROK_COMMAND
import subprocess

def start_server():
    print('Change detected, restarting python server and ngrok tunnel...')
        
    # execute command to run 'run-server.py' script
    server_process = subprocess.Popen(["python", "run-server.py"])
    
    # construct ngrok command
    ngrok_command = NGROK_COMMAND
    
    # execute command to restart ngrok tunnel
    ngrok_process = subprocess.Popen(ngrok_command, shell=True)
    
    server_process.wait()
    ngrok_process.wait()
    
if __name__ == '__main__':
    start_server()