import urllib.request, urllib.parse, urllib.error
import re, json, unicodedata

RACES = {	3 : {'id': 3, 'mask': 4, 'name': 'Dwarf', 'side': 'alliance'},
			6 : {'id': 6, 'mask': 32, 'name': 'Tauren', 'side': 'horde'},
			5 : {'id': 5, 'mask': 16, 'name': 'Undead', 'side': 'horde'},
			2 : {'id': 2, 'mask': 2, 'name': 'Orc', 'side': 'horde'},
			7 : {'id': 7, 'mask': 64, 'name': 'Gnome', 'side': 'alliance'},
			8 : {'id': 8, 'mask': 128, 'name': 'Troll', 'side': 'horde'},
			9 : {'id': 9, 'mask': 256, 'name': 'Goblin', 'side': 'horde'},
			11: {'id': 11, 'mask': 1024, 'name': 'Draenei', 'side': 'alliance'},
			22: {'id': 22, 'mask': 2097152, 'name': 'Worgen', 'side': 'alliance'},
			10: {'id': 10, 'mask': 512, 'name': 'Blood Elf', 'side': 'horde'},
			1 : {'id': 1, 'mask': 1, 'name': 'Human', 'side': 'alliance'},
			4 : {'id': 4, 'mask': 8, 'name': 'Night Elf', 'side': 'alliance'}}

CLASSES = {	3 : {'id': 3, 'mask': 4, 'name': 'Hunter', 'powerType': 'focus'},
			1 : {'id': 1, 'mask': 1, 'name': 'Warrior', 'powerType': 'rage'},
			5 : {'id': 5, 'mask': 16, 'name': 'Priest', 'powerType': 'mana'},
			9 : {'id': 9, 'mask': 256, 'name': 'Warlock', 'powerType': 'mana'},
			7 : {'id': 7, 'mask': 64, 'name': 'Shaman', 'powerType': 'mana'},
			2 : {'id': 2, 'mask': 2, 'name': 'Paladin', 'powerType': 'mana'},
			4 : {'id': 4, 'mask': 8, 'name': 'Rogue', 'powerType': 'energy'},
			6 : {'id': 6, 'mask': 32, 'name': 'Death Knight', 'powerType': 'runic-power'},
			11: {'id': 11, 'mask': 1024, 'name': 'Druid', 'powerType': 'mana'},
			8 : {'id': 8, 'mask': 128, 'name': 'Mage', 'powerType': 'mana'}}

REGIONS = {	'UNITED_STATES'	: 'us',
			'KOREA'			: 'kr',
			'TAIWAN'		: 'tw',
			'EUROPE'		: 'eu',}

class APIBase(object):
	_ToSlug_Sub1 = re.compile(r'[^\w\s-]', re.UNICODE)
	_ToSlug_Sub2 = re.compile(r'[-\s]+', re.UNICODE)
	
	defaults = {
		'public_key': None,
		'private_key': None,
		'region': 'us',
	}
	
	def __init__(self, **kargs): # No positional args. Flexible keyword args.
		self.Update(**kargs)
	
	def Update(self, **kargs):
		for k, v in self.defaults.items():
			if k in kargs:
				setattr(self, k, kargs[k])
			else:
				setattr(self, k, v)
	
	def StartQuery(self, path = None, params = None, region = None):
		if not region:
			region = self.region
		if not path:
			path = self._path
		if not params:
			params = self._params
		return APIQuery(region = region, path = path, params = params)
	
	@staticmethod
	def _ToSlug(value):
		slug = APIBase._ToSlug_Sub1.sub('', value)
		slug = APIBase._ToSlug_Sub2.sub('-', slug)
		
		return unicodedata.normalize('NFKC', slug)
	
	@staticmethod
	def _Quote(value):
		return urllib.parse.quote(value)

class APIQuery(object):
	url = r'http://%(region)s.battle.net/api/wow%(path)s?%(fields)s'
	
	def __init__(self, region, path, params):
		self.region = region
		self.path = path
		self.params = params
		self.values = dict()
	
	def SetParams(self, **kargs):
		self.values.update(kargs)
	
	def GetData(self, raw = False):
		values = dict()
		for key, value in self.values.items():
			values[key] = APIBase._Quote(value)
		path = self.path % values
		fields = self.params % values
		url = self.url % {'region': self.region, 'path': path, 'fields': fields}
		
		try:
			response = (urllib.request
				.urlopen(url)
				.read()
				.decode('utf8'))
			
			if raw:
				return response
			
			data = json.loads(response)
		
			if data.get('status', False) == 'nok':
				raise APIError(data['reason'])
			
			return data
		except:
			raise

class APIError(Exception):
	pass

class APIResponse(object):
	def __init__(self, data):
		self.__json = repr(data)
		for k, v in data.items():
			setattr(self, k, v)
	def __repr__(self):
		return self.__json
	def JSON(self):
		return self.__json
