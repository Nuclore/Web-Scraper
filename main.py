from web_scraper import WebScraper # Class containing web scraping functionality.

if __name__ == '__main__':
	url = 'https://thehackernews.com/search/label/Cyber%20Attack' # Website URL
	web_scraper = WebScraper(url) # Creates a WebScraper object and passes it the URL.
	web_scraper.get_website_content() # Obtains the HTML content of the webpage.
	web_scraper.create_soup() # Creates the BeautifulSoup object with the URL.
	web_scraper.process_webpage() # Processes the webpage to extract the information.
	# If you want to display the results on the screen.
	# web_scraper.display_results()
	web_scraper.save('results.txt') # Save the results to a text file.