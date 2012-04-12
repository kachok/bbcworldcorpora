"""
Unit tests for the BBC News corpora builder
"""

import os
import unittest

import bbcworldcorpora


class FeedDiscovery(unittest.TestCase):

	def setUp(self):
		self.langs=['russian','urdu','tamil']

	def test_discovery(self):
		for lang in self.langs:
			self.assertTrue("feed" in bbcworldcorpora.get_feed(lang))
			self.assertTrue("title" in bbcworldcorpora.get_feed(lang)["feed"])

if __name__ == '__main__':
    unittest.main()