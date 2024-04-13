from news_extractor import NewsExtractor

def main():
    # Initialize NewsExtractor with the URL of the AP News website
    extractor = NewsExtractor("https://apnews.com/")
    
    # Extract news data with the search phrase "Trump Chick-fil-A Black Voters"
    extractor.extract_news("Trump Chick-fil-A Black Voters")
    
    # Close the WebDriver
    extractor.close_driver()

if __name__ == "__main__":
    main()
