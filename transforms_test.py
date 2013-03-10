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

if __name__ == '__main__':
    unittest.main()
