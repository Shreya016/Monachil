import requests

class NetworkRequest:
	def get(self, url):
		response = requests.get(url)
		return response.json()