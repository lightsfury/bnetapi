# *-* encoding: utf-8 *-*

import bnetapi.realm
import unittest

class RealmUnitTest(unittest.TestCase):
	def setUp(self):
		self.realmStatus = bnetapi.RealmStatus()
	
	def tearDown(self):
		del self.realmStatus
	
	def test_QueryByName(self):
		name = 'Uther'
		
		status = self.realmStatus.QueryRealm(name, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertEqual(name, status.name)
	
	def test_QueryByNames(self):
		names = ['Uther', 'Velen', 'Aerie Peak', 'Altar of Storms']
		
		status = self.realmStatus.QueryRealms(names, region = bnetapi.REGIONS['UNITED_STATES'])
		
		for realm in status:
			self.assertIn(realm.name, names)
	
	def test_QueryBySlug(self):
		slug = 'uther'
		
		status = self.realmStatus.QueryRealm(slug, region = bnetapi.REGIONS['UNITED_STATES'])
		
		self.assertEqual(status.slug, slug)
	
	def test_QueryBySlugs(self):
		slugs = ['uther', 'velen', 'aerie-peak', 'altar-of-storms']
		
		status = self.realmStatus.QueryRealms(slugs, region = bnetapi.REGIONS['UNITED_STATES'])
		
		for realm in status:
			self.assertIn(realm.slug, slugs)
	
	def test_QueryByUnicodeName(self):
		name = 'Ясеневый лес'
		
		status = self.realmStatus.QueryRealm(name, region = bnetapi.REGIONS['EUROPE'])
		
		self.assertEqual(status.name, name)
	
	def test_QueryByUnicodeNames(self):
		names = ['Черный Шрам', 'Ясеневый лес', 'Ткач Смерти', 'Борейская тундра']
		
		status = self.realmStatus.QueryRealms(names, region = bnetapi.REGIONS['EUROPE'])
		
		for realm in status:
			self.assertIn(realm.name, names)
	
if __name__ == "__main__":
	unittest.main()