from .apibase import APIError, APIBase, APIResponse

FIELDS = { # Temporary arena team fields map
	'ROSTER'	: 'members',
	'MEMBERS'	: 'members',}

SIZE = {
	'2V2'	: '2v2',
	'3V3'	: '3v3',
	'5V5'	: '5v5',}

'''
Arena Team
URL: /api/wow/arena/{realm}/{size}/{name} (size being 2v2, 3v3 or 5v5)
Basic information: name, ranking, rating, weekly/season statistics
Optional fields: members (roster)
'''

class ArenaProfile(APIBase):
	_path = '/arena/%(realm)s/%(size)s/%(name)s'
	_params = 'fields=%(fields)s'
	
	@staticmethod
	def _ResolveField(field):
		if field in FIELDS:
			return FIELDS[field]
		elif field in ('all', 'ALL'):
			return ','.join(set(FIELDS.values())) # Only take unique field tags
		else:
			return field
	
	@staticmethod
	def _ResolveSize(size):
		if size in SIZE:
			return SIZE[size]
		else:
			return size
	
	def QueryTeam(self, realm, name, size, fields = None, raw = False, region = None):
		if fields:
			if not isinstance(fields, str):
				fields = ','.join(list(map(ArenaProfile._ResolveField, fields)))
		else:
			fields = ''
		if not region:
			region = self.region
		
		query = self.StartQuery(region = region)
		query.SetParams(realm = self._ToSlug(realm), name = self._Quote(name), size = self._ResolveSize(size), fields = fields)
		
		data = query.GetData(raw)
		
		if raw:
			return data
		
		return ArenaResponse(data)

class ArenaResponse(APIResponse):
	pass
