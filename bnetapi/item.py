from .apibase import APIError, APIBase, APIResponse

class ItemData(APIBase):
	_path = '/item/%(id)s'
	_params = ''
	
	def QueryItem(self, id, raw = False, region = None):
		query = self.StartQuery(region = region)
		query.SetParams(id = int(id))
		
		data = query.GetData(raw) # Returns a decoded JSON object. `raw` denotes raw JSON output
		
		if raw:
			return data
		
		return ItemResponse(data)

class ItemResponse(APIResponse):
	pass
