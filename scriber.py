import time

import paho.mqtt.client as paho
import threading
from scriber.crud import ListOperation

topic = 'a/b'

message_counter = 0

cruder=ListOperation()
# def subscribe(client):
#     msg_count = 0
#     while (True):
#         # time.sleep(1)
#         msg = f"messages: {msg_count}"
#         client.subscribe(topic)
#         msg_count += 1




def on_message(client, userdata, msg):
    # global message_counter
    # message_counter += 1
    # if message_counter % 10 == 0:
    #     print(message_counter)


    # print(msg)
    msg=msg.payload.decode()
    cruder.add(msg)
    print(cruder.list)



clear_thread=threading.Thread(target=cruder.clear2)
clear_thread.start()
# clear_thread.join()


client = paho.Client("", True, None, paho.MQTTv31)
client.on_message = on_message
client.username_pw_set('admin', 'admin')
print(client.connect('127.0.0.1', port=1883, keepalive=300))
client.subscribe(topic, qos=0, options=None, properties=None)
client.loop_forever()
