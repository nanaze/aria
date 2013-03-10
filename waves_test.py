#!/usr/bin/env python

import waves
import unittest


class WavesTestCase(unittest.TestCase):

  def testSine(self):
    self.assertAlmostEquals(0, waves.sine(0))
    self.assertAlmostEquals(1, waves.sine(.25))
    self.assertAlmostEquals(0, waves.sine(.5))
    self.assertAlmostEquals(-1, waves.sine(.75))
    self.assertAlmostEquals(0, waves.sine(1))
    self.assertAlmostEquals(0, waves.sine(1.5))
    self.assertAlmostEquals(-1, waves.sine(-0.25))
    self.assertAlmostEquals(0, waves.sine(-0.5))

  def testSquare(self):
    self.assertAlmostEquals(1, waves.square(0))
    self.assertAlmostEquals(1, waves.square(0.25))
    self.assertAlmostEquals(1, waves.square(0.49))
    self.assertAlmostEquals(-1, waves.square(0.5))
    self.assertAlmostEquals(-1, waves.square(0.6))
    self.assertAlmostEquals(-1, waves.square(0.75))
    self.assertAlmostEquals(-1, waves.square(0.9))
    self.assertAlmostEquals(1, waves.square(1))
    self.assertAlmostEquals(1, waves.square(1.25))

if __name__ == '__main__':
    unittest.main()
