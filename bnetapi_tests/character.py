# *-* encoding: utf-8 *-*

import bnetapi.character
import unittest

class CharacterUnitTest(unittest.TestCase):
	def setUp(self):
		self.characterProfile = bnetapi.CharacterProfile()
	
	def tearDown(self):
		del self.characterProfile
	
	def test_QueryCharacter(self):
		realm = 'Uther'
		name = 'Naidi'
		
		profile = self.characterProfile.QueryCharacter(realm, name, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertEqual(profile.name, name)
		self.assertEqual(profile.realm, realm)
	
	def test_QueryCharacterTalents(self):
		realm = 'Uther'
		name = 'Naidi'
		fields = ['TALENTS']
		
		profile = self.characterProfile.QueryCharacter(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertGreater(len(profile.talents), 0)
	
	def test_QueryCharacterGear_Standard(self):
		realm = 'Uther'
		name = 'Naidi'
		fields = ['ITEMS']
		
		profile = self.characterProfile.QueryCharacter(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertGreater(len(profile.items), 0)
	
	def test_QueryCharacterGear_NonStandard(self):
		realm = 'Uther'
		name = 'Naidi'
		fields = ['GEAR']
		
		profile = self.characterProfile.QueryCharacter(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertGreater(len(profile.items), 0)
	
	def test_QueryCharacterAll(self):
		realm = 'Uther'
		name = 'Goatsé'
		fields = ['ALL']
		
		profile = self.characterProfile.QueryCharacter(realm, name, fields = fields, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertEqual(profile.realm, realm)
		self.assertEqual(profile.name, name)
		
		# Cannot use exhaustive lookup for ALL information as invalid or unkown information will NOT be included.
		# IE: An unguilded character will never have a "guild" section even if guild information is requested.
		#for field in bnetapi.character.FIELDS.values():
		#	self.assertTrue(hasattr(profile, field), 'profile has `%s` = `%s`' % (field, hasattr(profile, field)))
	
	def test_QueryUnicodeCharacter(self):
		realm = 'Ревущий фьорд'
		name = 'Джусичь'
		
		profile = self.characterProfile.QueryCharacter(realm, name, region = bnetapi.REGIONS['EUROPE'])
		
		self.assertEqual(profile.realm, realm)
		self.assertEqual(profile.name, name)
	
if __name__ == "__main__":
	unittest.main()