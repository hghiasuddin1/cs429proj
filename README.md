# cs429proj

# Abstract
This report presents the development of a web document retrieval system aimed at efficiently crawling, indexing, and processing web documents. The objectives of the project include implementing a scalable web crawler, constructing an inverted index for search indexing, and developing a query processor to handle free text queries. The system is designed to be modular and extensible, allowing for easy integration of additional features and improvements.

# Overview
The repository consists of three main components: a Scrapy-based web crawler for downloading web documents, a Scikit-Learn-based indexer for constructing an inverted index, and a Flask-based query processor for handling free text queries. Relevant literature in information retrieval and natural language processing guided the design of the system, leveraging techniques such as TF-IDF weighting and cosine similarity for efficient search indexing and retrieval. The proposed system aims to provide users with fast and accurate search results from a large corpus of web documents.

# Design
The system's capabilities include crawling web documents from specified seed URLs, constructing an inverted index using TF-IDF weighting, and processing free text queries to retrieve top-ranked results. Interactions between components involve passing data such as crawled documents and queries, with integration facilitated by standard interfaces and data formats. 

# Architecture
The software architecture consists of three main components: the Scrapy-based web crawler, the Scikit-Learn-based indexer, and the Flask-based query processor. These components communicate through well-defined interfaces, with data passed in JSON format. Implementation details include the use of Python 3.10+, Scrapy 2.11+, Scikit-Learn 1.2+, and Flask 2.2+ libraries to build the system.

# Operation
To use the system, users can run the provided Python scripts for each component. For the web crawler, specify the seed URL/domain, maximum pages, and maximum depth. For the indexer, provide a list of documents to build the inverted index. For the query processor, send free text queries in JSON format to the specified endpoint. 

# Conclusion
The development of the web document retrieval system was successful in achieving the stated objectives. The system demonstrates efficient crawling, indexing, and query processing capabilities. However, further testing and optimization are required to ensure scalability and performance under heavy loads. Caveats include potential challenges in handling dynamic web content and optimizing query processing for real-time responses.

# Data Sources
The system does not rely on external data sources but is designed to crawl and index web documents from any publicly accessible website.
For the crawler test cases, I use a wikipedia page, a quotes website, and Professor Lee's website, moss.cs.iit.edu.

# Test Cases
Test cases for the system can be developed using a framework such as pytest, covering scenarios such as crawling various types of web content, indexing large document collections, and processing diverse query types.

**Crawler:**

1. **Test Case 1:**
   - **Purpose:** 
     - Evaluate the crawler's behavior when crawling Wikipedia pages, starting from the seed URL of "https://en.wikipedia.org/wiki/Mike_Tyson".
     - Test the crawler's ability to limit the crawl to a maximum of 100 pages and a depth of 3 levels.
   - **Framework:**
     - Scrapy provides the testing framework for defining and executing spider-based tests. It offers tools for creating test cases and running spiders within a controlled environment.
   - **Harness:**
     - Scrapy's test harness automates the execution of the crawler based on the provided test case. It sets up the environment, initiates the spider with the specified parameters, and collects the results.
   - **Coverage:**
     - The test case aims to achieve coverage of the crawler's functionality when crawling Wikipedia pages. Coverage analysis will measure the percentage of code paths exercised by the spider during the crawl, ensuring comprehensive testing.

2. **Test Case 2:**
   - **Purpose:**
     - Assess the crawler's performance when scraping quotes from the "http://quotes.toscrape.com" website.
     - Test the crawler's behavior with a higher maximum depth of 40 levels while still limiting the crawl to 100 pages.
   - **Framework:**
     - Utilizes Scrapy's testing framework to define and execute the spider-based test case for scraping quotes.
   - **Harness:**
     - Leverages Scrapy's test harness to automate the execution of the crawler, ensuring consistent and repeatable test runs.
   - **Coverage:**
     - Coverage analysis will gauge the extent to which the crawler exercises the codebase when scraping quotes from the specified website. It helps identify areas of the code that may require additional testing or refinement.

3. **Test Case 3:**
   - **Purpose:**
     - Evaluate the crawler's performance on a different domain, specifically the "https://moss.cs.iit.edu/" website.
     - Test the crawler's behavior with a moderate limit of 60 pages and a deep maximum depth of 60 levels.
   - **Framework:**
     - Relies on Scrapy's testing framework to define and execute the spider-based test case targeting the Moss website.
   - **Harness:**
     - Utilizes Scrapy's test harness to automate the execution of the crawler, facilitating efficient and controlled testing on the specified domain.
   - **Coverage:**
     - Coverage analysis will measure the effectiveness of the crawler in traversing and scraping content from the Moss website. It helps ensure that the crawler adequately exercises the codebase, identifying any potential gaps in test coverage.


**Processor:**

1. **Test Case 1: Test Adding Documents**
   - **Purpose:** 
     - Validate the functionality of adding documents to the Flask application.
   - **Framework:**
     - Utilizes the unittest framework for defining and executing test cases.
   - **Harness:**
     - Leverages Flask's test client to simulate HTTP requests and interact with the application endpoints.
   - **Coverage:**
     - Ensures that the endpoint '/add_documents' properly handles JSON requests containing documents and returns a successful response upon adding documents successfully.

2. **Test Case 2: Test Processing Queries**
   - **Purpose:**
     - Evaluate the capability of the Flask application to process queries based on the added documents.
   - **Framework:**
     - Utilizes the unittest framework for defining and executing test cases.
   - **Harness:**
     - Leverages Flask's test client to simulate HTTP requests and interact with the application endpoints.
   - **Coverage:**
     - Verifies that the '/query' endpoint correctly handles queries, calculates cosine similarity scores, and returns the top-k results as expected.

3. **Test Case 3: Test Empty Query**
   - **Purpose:**
     - Validate the behavior of the Flask application when an empty query is provided.
   - **Framework:**
     - Utilizes the unittest framework for defining and executing test cases.
   - **Harness:**
     - Leverages Flask's test client to simulate HTTP requests and interact with the application endpoints.
   - **Coverage:**
     - Ensures that the application returns an appropriate error response with status code 400 when an empty query is provided.

4. **Test Case 4: Test Missing Query Key**
   - **Purpose:**
     - Validate the behavior of the Flask application when the 'query' key is missing from the JSON data.
   - **Framework:**
     - Utilizes the unittest framework for defining and executing test cases.
   - **Harness:**
     - Leverages Flask's test client to simulate HTTP requests and interact with the application endpoints.
   - **Coverage:**
     - Verifies that the application returns an appropriate error response with status code 400 and an error message when the 'query' key is missing from the JSON data.


**Indexer**


1. **Test Case 1: Adding Documents**
   - **Purpose:** 
     - To verify the functionality of adding documents to the indexer.
   - **Framework:** 
     - Utilizes Python's unittest framework for defining and executing test cases.
   - **Harness:** 
     - Uses a test environment where the `Indexer` class is instantiated and documents are added using the `add_document` method.
   - **Coverage:** 
     - Ensures that documents can be successfully added to the indexer and that the indexer maintains the correct association between terms and documents.

2. **Test Case 2: Building Index**
   - **Purpose:** 
     - To ensure that the index is built correctly from the added documents.
   - **Framework:** 
     - Utilizes Python's unittest framework for defining and executing test cases.
   - **Harness:** 
     - Uses a test environment where the `Indexer` class is instantiated, documents are added, and the index is built using the `build_index` method.
   - **Coverage:** 
     - Verifies that the TF-IDF matrix is constructed accurately and reflects the document-term associations in the indexed documents.

3. **Test Case 3: Performing Searches**
   - **Purpose:** 
     - To validate the capability of the indexer to perform search queries based on the built index.
   - **Framework:** 
     - Utilizes Python's unittest framework for defining and executing test cases.
   - **Harness:** 
     - Uses a test environment where the `Indexer` class is instantiated, documents are added, the index is built, and search queries are executed using the `search` method.
   - **Coverage:** 
     - Ensures that search queries return relevant documents with accurate cosine similarity scores and TF-IDF scores.

4. **Test Case 4: Printing TF-IDF Matrix**
   - **Purpose:** 
     - To verify that the TF-IDF matrix representation of the indexed documents is accurate.
   - **Framework:** 
     - Utilizes Python's unittest framework for defining and executing test cases.
   - **Harness:** 
     - Uses a test environment where the `Indexer` class is instantiated, documents are added, and the index is built. The TF-IDF matrix is then printed using the `print` statement.
   - **Coverage:** 
     - Confirms that the TF-IDF matrix reflects the numerical representation of the indexed documents accurately.


# Source Code
The source code for this project was generated using OpenAI's ChatGPT model. The code is written in Python and utilizes various libraries and frameworks, including:

- `scikit-learn` for TF-IDF vectorization and cosine similarity calculations.
- `pickle` for serializing and deserializing Python objects.
- `unittest` for defining and executing test cases.
- `Flask` for creating the web service

# Bibliography
Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to Information Retrieval. Cambridge University Press.
Jurafsky, D., & Martin, J. H. (2020). Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition. Pearson.
