from .apibase import APIError, APIBase, APIResponse

FIELDS = {
	'ROSTER'		: 'members',
	'MEMBERS'		: 'members',
	'ACHIEVEMENTS'	: 'achievements',}

class GuildProfile(APIBase):
	_path = '/guild/%(realm)s/%(name)s'
	_params = 'fields=%(fields)s'
	
	@staticmethod
	def _ResolveField(field):
		if field in FIELDS:
			return FIELDS[field]
		elif field in ('all', 'ALL'):
			return ','.join(set(FIELDS.values())) # Only take unique field tags
		else:
			return field
	
	def QueryGuild(self, realm, name, fields = None, raw = False, region = None):
		if fields:
			if not isinstance(fields, str):
				fields = ','.join(list(map(GuildProfile._ResolveField, fields)))
		else:
			fields = ''
		if not region:
			region = self.region
		
		query = self.StartQuery(region = region)
		query.SetParams(realm = self._ToSlug(realm), name = name, fields = fields)
		
		data = query.GetData(raw)
		
		if raw:
			return data
		
		return GuildResponse(data)

class GuildResponse(APIResponse):
	pass


