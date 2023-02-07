echo "Hello World"
cd C:\Users\pcadmin\Documents\CodingProjects\ZephyrOS\zephyrproject
call .venv/Scripts/activate.bat
cd zephyr/
call west build -p always -b qemu_x86 -d build/client1 samples/modules/tflite-micro/fyp_hello_world -t run
::timeout /t 5
