#!/bin/bash
echo "Entering Script"
cd ~/zephyrproject
source .venv/bin/activate
cd zephyr/
#west build -p always -b qemu_x86 -d build/server samples/net/sockets/tensor_echo_server
#west build -d build/server -t run

west build -p always -d build/server -b qemu_x86 -t run \
      samples/modules/tflite-micro/tensor_server -- \
      -DOVERLAY_CONFIG=overlay-e1000.conf \
      -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"198.51.100.1\" \
      -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"203.0.113.1\" \
      -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:100::1\" \
      -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:200::1\" \
      -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"203.0.113.1\" \
      -DCONFIG_ETH_QEMU_IFACE_NAME=\"zeth.1\" \
      -DCONFIG_ETH_QEMU_EXTRA_ARGS=\"mac=00:00:5e:00:53:01\"
echo "Exiting Script"
exit 0
