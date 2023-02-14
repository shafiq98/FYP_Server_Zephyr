from unittest import TestCase

import psutil

import src.Service.ZephyrService as zs


class Test(TestCase):
    def test_start_zephyr_instance(self):
        self.fail()

    def test_base1(self):
        # print(os.getcwd())
        zs.start_zephyr_instance()

    def test_proc_kill(self):
        # use this test method to kill stray QEMU instances and consoles when server unexpectedly quits
        zs.complete_kill()
        process = psutil.Process(18399)
