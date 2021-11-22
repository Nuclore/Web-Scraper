# Web-Scraper

Program to extract a list of stories from https://thehackernews.com/search/label/Cyber%20Attack and store the results in a text file.
Each result would contain the story title, story description and story link.

If you want to extract information from a different URL, you will need to specify the URL in main.py, and modify the process_webpage method in the WebScraper class located in web_scraper.py

To obtain the tag and class values for the webpage, you will need to inspect it on your web browser.

Note: This program uses the following external packages.
      1) beautifulsoup4
      2) requests
      3) lxml
      
      If you do not have these packages installed, you can install it with pip.
      On Windows, execute the following command: pip install <package_name>
      On Linux/macOS, execute the following command: pip3 install <package_name>