# *-* encoding: utf-8 *-*

import bnetapi.guild
import unittest

class ArenaUnitTest(unittest.TestCase):
	def setUp(self):
		self.arenaProfile = bnetapi.ArenaProfile()
	
	def tearDown(self):
		del self.arenaProfile
	
	def test_QueryArena(self):
		realm = 'Bloodhoof'
		name = 'plzspankus'
		size = '2V2'
		fields = []
		
		profile = self.arenaProfile.QueryTeam(realm = realm, name = name, size = size, region = bnetapi.REGIONS['UNITED_STATES'], fields = fields)
		
		self.assertEqual(profile.name, name)
		self.assertEqual(profile.realm['name'], realm)
		self.assertEqual(profile.teamsize, 2)

if __name__ == "__main__":
	unittest.main()