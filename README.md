# News Extraction Automation

This project automates the process of extracting news data from a website using Python and Selenium. It searches for news articles related to a specified search phrase and category, retrieves relevant information such as title, date, description, and image, and stores it in an Excel file. Additionally, it checks for the presence of specific keywords (such as money-related terms) in the news articles.

## Project Structure

The project structure is organized as follows:

- **src/**: Contains the source code files.
  - **main.py**: The main script to initiate the news extraction process.
  - **news_extractor.py**: Contains the class implementing the news extraction logic.
  - **__init__.py**: An empty file to make the `src` directory a Python package.

- **utils/**: Holds utility files.
  - **chromedriver.exe**: WebDriver executable for Chrome (or appropriate driver for your browser).

- **output/**: Contains output files generated during the news extraction process.
  - **news_data.xlsx**: Excel file to store extracted news data.

- **README.md**: Documentation and instructions for the project.

- **requirements.txt**: Lists all Python dependencies required by the project.

## Dependencies

The project requires the following Python libraries:
- `selenium`: For browser automation.
- `openpyxl`: For working with Excel files.

Install the dependencies using pip:

