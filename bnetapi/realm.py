from .apibase import APIError, APIBase, APIResponse

class RealmStatus(APIBase):
	_path = '/realm/status'
	_params = 'realms=%(realms)s'
	
	def QueryRealm(self, name, raw = False, region = None):
		query = self.StartQuery(region = region)
		query.SetParams(realms = self._ToSlug(name))
		
		data = query.GetData(raw) # Returns a decoded JSON object. `raw` denotes raw JSON output
		
		if raw:
			return data
		
		return StatusResponse(data['realms'][0])
	
	def QueryRealms(self, names, raw = False, region = None):
		query = self.StartQuery(region = region)
		query.SetParams(realms = ','.join(list(map(self._ToSlug, names))))
		
		try:
			data = query.GetData(raw) # Returns a decoded JSON object. `raw` denotes raw JSON output
			
			if raw:
				return data
				
			return list(map(StatusResponse, data['realms']))
			
		except Exception as e:
			raise APIError(str(e))
	
	def QueryAllRealms(self, raw = None, region = None):
		query = self.StartQuery(params = '', region = region)
		#query.SetParams(realms = self._ToSlug(name)) # Don't need to set params for all realms
		
		try:
			data = query.GetData(raw) # Returns a decoded JSON object. `raw` denotes raw JSON output
			
			if raw:
				return data
				
			return list(map(StatusResponse, data['realms']))
			
		except Exception as e:
			raise APIError(str(e))

class StatusResponse(APIResponse):
	pass
