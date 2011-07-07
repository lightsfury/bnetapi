from .apibase import APIError, APIBase, APIResponse

FIELDS = {
	'GUILD'			: 'guild',
	'STATS'			: 'stats',
	'TALENTS'		: 'talents',
	'GEAR'			: 'items',
	'ITEMS'			: 'items',
	'REPUTATION'	: 'reputation',
	'TITLES'		: 'title',
	'TRADESKILLS'	: 'professions',
	'PROFESSIONS'	: 'professions',
	'APPEARANCE'	: 'appearance',
	'NONCOMBAT_PETS': 'companions',
	'COMPANIONS'	: 'companions',
	'MOUNTS'		: 'mounts',
	'COMBAT_PETS'	: 'pets',
	'PETS'			: 'pets',
	'ACHIEVEMENTS'	: 'achievements',
	'PROGRESSION'	: 'progression',}

class CharacterProfile(APIBase):
	_path = '/character/%(realm)s/%(name)s'
	_params = 'fields=%(fields)s'
	
	@staticmethod
	def _ResolveField(field):
		if field in FIELDS:
			return FIELDS[field]
		elif field in ('all', 'ALL'):
			return ','.join(set(FIELDS.values())) # Only take unique field tags
		else:
			return field
	
	def QueryCharacter(self, realm, name, fields = None, raw = False, region = None):
		if fields:
			if not isinstance(fields, str):
				fields = ','.join(list(map(CharacterProfile._ResolveField, fields)))
		else:
			fields = ''
		if not region:
			region = self.region
		
		query = self.StartQuery(region = region)
		query.SetParams(realm = self._ToSlug(realm), name = self._ToSlug(name), fields = fields)
		
		data = query.GetData(raw)
		
		if raw:
			return data
		
		return CharacterResponse(data)

class CharacterResponse(APIResponse):
	pass
