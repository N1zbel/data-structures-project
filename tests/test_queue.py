"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class QueueTestCase(unittest.TestCase):

    def test_enqueue(self):
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")
