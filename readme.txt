Just an example of a python program that uses rtmidi2 to read messages. 

built on an M1 mac using pycharm ce (dont forget to add the rtmidi2 package) and an AKAI LPK25 USB Keyboard (which acts as a MIDI device when plugged into your pc).

I used it with an AKAI LPK25 midi keyboard, a I wanted to find out the MIDI channel number the device was sending on but then it morhped into finding out other info like note number/velocity. 

This would make a great base for a midi input analyser. 

Found these examples helpful 
https://qiita.com/Dr10_TakeHiro/items/e6df6c9b59869a74f899 << useful to learn how to select the correct interface
https://rtmidi2.readthedocs.io/en/latest/reference.html << the reference for RTMIDI2
https://www.cs.cmu.edu/~music/cmsip/readings/davids-midi-spec.htm << quick reference for the MIDI Spec
https://fmslogo.sourceforge.io/manual/midi-table.html << more stuff on the midi spec / quick lookup 
