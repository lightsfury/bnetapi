# *-* encoding: utf-8 *-*

import bnetapi.guild
import unittest

class GuildUnitTest(unittest.TestCase):
	def setUp(self):
		self.guildProfile = bnetapi.GuildProfile()
	
	def tearDown(self):
		del self.guildProfile
		
	def test_QueryGuild(self):
		name = 'Forgotten Valor'
		realm = 'Uther'
		
		profile = self.guildProfile.QueryGuild(realm, name, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertEqual(profile.name, name)
		self.assertEqual(profile.realm, realm)
	
	def test_QueryGuildRoster(self):
		name = 'Forgotten Valor'
		realm = 'Uther'
		fields = ['ROSTER']
		
		profile = self.guildProfile.QueryGuild(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertGreater(len(profile.members), 0)
	
	def test_QueryGuildMembers(self):
		name = 'Forgotten Valor'
		realm = 'Uther'
		fields = ['MEMBERS']
		
		profile = self.guildProfile.QueryGuild(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertGreater(len(profile.members), 0)
	
	def test_QueryGuildAchievements(self):
		name = 'Forgotten Valor'
		realm = 'Uther'
		fields = ['ACHIEVEMENTS']
		
		profile = self.guildProfile.QueryGuild(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		self.assertGreater(len(profile.achievements), 0)
	
	def test_QueryGuildAll(self):
		name = 'Forgotten Valor'
		realm = 'Uther'
		fields = ['ALL']
		
		profile = self.guildProfile.QueryGuild(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertGreater(len(profile.members), 0)
		self.assertGreater(len(profile.achievements), 0)

if __name__ == "__main__":
	unittest.main()