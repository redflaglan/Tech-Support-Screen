#!/bin/bash
sudo killall fbi
echo | sudo fbi -T 1 -t 10 -noonce -noverbose -autozoom -d /dev/fb0 "$@"
