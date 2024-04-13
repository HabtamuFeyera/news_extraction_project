from news_extractor import NewsExtractor

def main():
    # Initialize NewsExtractor
    extractor = NewsExtractor("https://apnews.com/")
    
    # Extract news data
    extractor.extract_news("COVID-19", "Health")
    
    # Close the WebDriver
    extractor.close_driver()

if __name__ == "__main__":
    main()
