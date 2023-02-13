#!/bin/bash
echo "Entering Script"
cd ~/zephyrproject
source .venv/bin/activate
cd zephyr/
west build -p always -b qemu_x86 -d build/server samples/net/sockets/tensor_echo_server
west build -d build/server -t run
ls
echo "Exiting Script"
