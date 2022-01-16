import paho.mqtt.client as paho
import time
from multiprocessing import Process

mqtthost = "localhost"
mqttuser = "admin"
mqttpass = "admin"


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))
    client.subscribe('beta')
    client.publish('beta', 'Excellent!', 0, False)

"""
in each publish
"""
def on_publish(client, userdata, mid):
    print("mid: " + str(mid))

"""
in each publish for each user 
"""
def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    pass


topic = 'a/b'


def publish(client, msg):
    msg_count = 1
    while True:
        time.sleep(1)
        result = client.publish(topic, msg)
        result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}{msg_count}")

        msg_count += 1


"""
create client -- introduce function -- set user pass
"""
client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.username_pw_set(mqttuser, mqttpass)

print(str(client.connect(mqtthost, 1883, 300)))

process_list = []
"""
append process to list 
"""
for i in range(20):
    process_list.append(Process(target=publish, args=(client, f'{i}',)))

"""
start and join process
"""
for process in process_list:
    process.start()

for process in process_list:
    process.join()
client.loop_forever()
