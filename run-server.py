from config import NGROK_COMMAND
import os # development
# import subprocess -- production

def start_server():
    os.system('python server.py') # development
    
    '''
    PRODUCTION CODE BELOW -- AUTORESTART WILL NOT BE NEEDED
    '''
    # print('starting localhost server and ngrok tunnel...')
    
    # sleep(1)
        
    # # execute command to run 'run-server.py' script
    # server_process = subprocess.Popen(["python", "run-server.py"])
    
    # # path to ngrok executable
    # # ngrok_path = 'C:/Users/arjun/OneDrive/Desktop/CS Projects/FileBrowser/ngrok.exe'
    
    # # construct ngrok command -- !!may need to replace "ngrok" with ngrok_path!!
    # ngrok_command = NGROK_COMMAND
    
    # # execute command to restart ngrok tunnel
    # ngrok_process = subprocess.Popen(ngrok_command, shell=True)
    
    # server_process.wait()
    # ngrok_process.wait()
    
    '''
    '''
    
if __name__ == '__main__':
    start_server()