#!/usr/bin/env python

import unittest
import transforms

class TransformsCase(unittest.TestCase):

  def testScaleAmplitude(self):
    wave_func = lambda t: t
    self.assertEqual(1, wave_func(1))

    scaled_func = transforms.scale_amplitude(wave_func, 2)
    self.assertEqual(2, scaled_func(1))

  def testMapAmplitude(self):
    wave_func = lambda t: t
    negate_func = lambda amp: -amp

    mapped_func = transforms.map_amplitude(wave_func, negate_func)
    self.assertEqual(-1, mapped_func(1))

  def testMapRate(self):
    wave_func = lambda t: t
    mult_func = lambda t: t * 100 # speed up 100 time
    mapped_func = transforms.map_rate(wave_func, mult_func)
    self.assertEqual(100, mapped_func(1))

  def testScaleRate(self):
    wave_func = lambda t: t
    mapped_func = transforms.scale_rate(wave_func, 50)
    self.assertEqual(50, mapped_func(1))
    

if __name__ == '__main__':
    unittest.main()
