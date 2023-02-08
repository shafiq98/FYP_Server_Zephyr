# FYP_Server_Zephyr
Server to update Zephyr files and restart QEMU Process

### Current Program Flow
1. Program kills any QEMU Instance currently running
2. Starts a new Zephyr Instance and let it run in the background
   1. Stores its PID
3. Start web server that listens for incoming updated tflite models
   1. On receipt, stores it in memory
   2. Overwrites model.cpp in zephyr instance 
4. Call method to restart zephyr instance with new model

### TODO:
1. Move away from absolute paths
2. Make necessary modifications for Linux file structure 