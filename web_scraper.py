from bs4 import BeautifulSoup # For extracting information from a web page.
import requests # For obtaining HTML content from a webpage.

class WebScraper:
	'''Class containing functionality for extracting information from a website.'''
	def __init__(self, url=None):
		'''Initializes the object with the URL and a list to store the results.'''
		self.url = url # Stores the website URL.
		self.results = [] # Stores the results in a list.

	def create_soup(self):
		try:
			if self.content != None: # Checks if there are any HTML content.
				# Creates a BeautifulSoup object with the HTML content and 'lxml' parser.
				self.soup = BeautifulSoup(self.content, 'lxml')
		except AttributeError:
			# Displays an error if no HTML content was found.
			print('No HTML content was found for the specified URL.')

	def get_website_content(self):
		'''Obtains the HTML content from a webpage.'''
		try:
			response = requests.get(self.url) # Obtains a response object from the URL.
			# Checks if the status code of the response was ok.
			# A response code of 200 means a successful response.
			if response.status_code == requests.codes.ok: 
				# Obtains the HTML content from the response object text attribute,
				# and stores it as an attribute.
				self.content = response.text 
			else:
				# Displays an error if the response was unsuccessful.
				print(f'The content for {self.url} cannot be obtained.\n')  
		except requests.exceptions.ConnectionError:
			# Displays an error if the URL is invalid.
			print(f'{self.url} is not a valid URL.')
		except requests.exceptions.RequestException:
			# Displays an error if the request could not be processed.
			print(f'The request for {self.url} could not be processed.\n')

	def process_webpage(self):
		'''Processes the webpage and stores the results in a list.'''
		try:
			# Finds all the stories by specifiying the 'a' tag and class_='story-link'.
			stories = self.soup.find_all('a', class_='story-link')

			for story in stories: # Loop through each story.
				# Finds the  story title by specifying the 'h2' tag and class_='home-title',
				# extracts the text and strip any whitespace.
				story_title = story.find('h2', class_='home-title').text.strip()

				# Finds the story description by specifying the 'div' tag and class_='home-desc',
				# extracts the text and strip any whitespace.
				story_desc = story.find('div', class_='home-desc').text.strip()

				# Finds the story link by using the get method with 'href'.
				story_link = story.get('href')

				result = {} # Creates an empty dictionary to store the results.
				result['Story Title'] = story_title # Stores the story title in the results.
				result['Story Description'] = story_desc # Stores the story description in the results.
				result['Story Link'] = story_link # Stores the story link in the results.

				self.results.append(result) # Appends the result to the results list.
		except AttributeError:
			# Displays an error if a BeautifulSoup object was not created.
			print('BeautifulSoup object was not created because no HTML content was found.')

	def display_results(self):
		'''Displays the results to the screen.'''
		for result in self.results: # Loops through dictionary in the results list.
			for name, value in result.items(): # Loops through each key-value pair in the dictionary.
				print(f'{name}: {value}') # Prints each line of the result.
			print() # Prints a blank line for readability.

	def save(self, filename):
		'''Save the results to a text file.'''
		with open(filename, 'w') as f: # Creates an empty text file.
			for result in self.results: # Loops through each dictionary in the results list.
				for name, value in result.items(): # Loops through each key-value pair in the dictionary.
					f.write(f'{name}: {value}\n') # Writes each line of the result to the file.
				f.write('\n') # Writes a blank line for readability.

	


