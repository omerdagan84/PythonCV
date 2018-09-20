import time
import _thread as thread

import paho.mqtt.client as paho
broker="localhost"
def listner_func():
    client= paho.Client("listner") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
    ######Bind function to callback
    client.on_message=on_message
    #####
    print("connecting to broker ",broker)
    client.connect(broker)#connect
    client.loop_start() #start loop to process received messages
    print("subscribing ")
    client.subscribe("house/bulb1")#subscribe
    while True:
        pass

def publisher_func():
    counter = 0
    client= paho.Client("publisher") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
    client.connect(broker)#connect
    while True:
        test_string = "test string no:" + str(counter)
        client.publish("house/bulb1",test_string)#publish
        time.sleep(4)
        counter += 1

#define callback
def on_message(client, userdata, message):
    print("received the test message =",str(message.payload.decode("utf-8")))

thread.start_new_thread(listner_func,())
thread.start_new_thread(publisher_func,())

while True:
     pass
