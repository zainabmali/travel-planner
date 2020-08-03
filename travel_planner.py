import requests


class TravelPlanner():
	def __init__(self):
		self.country = None

	def get_country_info(self, country_name):
		request = requests.get('https://restcountries.eu/rest/v2/name/' + country_name)
		self.country = request.json()[0]
		return self.country

	def get_specific_info(self, param):
		return self.country[param]

def main():
	travel_planner = TravelPlanner()
	travel_planner.get_country_info('Norway')
	print(travel_planner.get_specific_info('currencies'))

if __name__ == '__main__':
	main()