import time
import rtmidi2
device_name = "LPK25"

midi_in = rtmidi2.MidiIn()
print(midi_in.ports)

try:
    index = midi_in.ports_matching(device_name+"*")[0]
    input_port = midi_in.open_port(index)
except IndexError:
    raise(IOError("Input port not found."))

print("Opened Port " + device_name + " - Ready to receive messages")

#midi_in.open_port(0)


NOTEON = int(144)
NOTEOFF = int(128)

while True:
    message = midi_in.get_message()  # will block until a message is available
    if message:
        messagetype = message[0] & 0xF0
        channel = message[0] & 0x0F
        if messagetype == NOTEON:
            print("Note On  / Channel " + str(channel + 1) + " Note " + str(message[1]) + " Velocity " + str(message[2]))
        elif messagetype == NOTEOFF:
            print("Note Off / Channel " + str(channel + 1) + " Note " + str(message[1]) + " Velocity " + str(message[2]))
        else:
            print("Something else" + str(message))
        #print("Message Type " + str(messagetype))
        #print("Channel      " + str(channel))
        #print("Note " + str(message[1]))
        #print(len(message))
