# -*-coding: utf-8 -*-
''' Test suit for maridian.py

@version: 0.0.1
@author: sheng
@contact: sinotradition@gmail.com
@copyright: License according to the project lincese.
'''
import unittest
import meridian

class TestMeridianFunctions(unittest.TestCase):

    def setUp(self):
        self.ap = meridian.acupoint('name','type','channel')
        self.ac = meridian.acuchannel('name',('ap1','ap2'))
    def test_acupoint(self):
        self.assertEqual(self.ap.name, 'name', 'msg ap name')
        self.assertEqual(self.ap.type, 'type', 'msg ap type')
        self.assertEqual(self.ap.channel, 'channel', 'msg ap channel')
    def test_acuchannel(self):
        self.assertEqual(self.ac.name, 'name', 'msg ac name')
        self.assertEqual(self.ac.member, ('ap1','ap2'), 'msg ac member')


if __name__ == "__main__":
    unittest.main()

