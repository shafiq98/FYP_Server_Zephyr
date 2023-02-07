:: ../../../../.venv/activate.bat
:: west build -p always -b qemu_x86 -d build/client ../fyp_hello_world
::cd ../../../../../
::call .venv/Scripts/activate.bat
::pip3 show west
::cd zephyr/
::cmake -version
::call west build -p always -b qemu_x86 -d build/client1 samples/modules/tflite-micro/fyp_hello_world -t run
::call west build -d build/client1 -t run
::timeout /t 5
::SendKeys "^{A}"
::SendKeys "x"
::dir
::%SendKeys% "^A"
::%SendKeys% "x"
::deactivate
echo "Hello World"
