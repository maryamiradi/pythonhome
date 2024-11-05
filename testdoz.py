import unittest
from unittest.mock import MagicMock, patch
import random
from tkinter import Tk, simpledialog, messagebox
from doz import User , Table , Game , Computer
class UserTest(unittest.TestCase):
    newuser=User('maryam','o')
    self.assertEqual(user.name,'maryam')