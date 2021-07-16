import unittest
from sms_pycode import * 

class messageTest(unittest.TestCase):
    def test_markAsRead(self):
        sms = SMSMessage(False, "Hello", "0798653452")
        self.assertTrue(MarkASRead("read",sms))
    def test_MsgCount(self):
        result = SMSMessage(False, "How are you?", "0631873298")
        self.assertGreater(get_count(SMSStore), -1)

if __name__ == '__main__':
    unittest.main()