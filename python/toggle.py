
#!/usr/bin/python2
import OSC
import sys
msg = OSC.OSCMessage()
msg.setAddress('/1/toggle3')
msg.append(int(sys.argv[1]))
client = OSC.OSCClient()
client.sendto(msg,('senderechner',8000))

