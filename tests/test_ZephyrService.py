from unittest import TestCase
import src.Service.ZephyrService as zs
import os
import signal
import psutil


class Test(TestCase):
    def test_start_zephyr_instance(self):
        self.fail()

    def test_base1(self):
        # print(os.getcwd())
        zs.start_zephyr_instance()

    def test_proc_kill(self):
        zs.kill_QEMU()