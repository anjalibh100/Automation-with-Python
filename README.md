# Automation-with-Python : 

The Python API's will get data through REST API's.

In this example: Python API will get data from the News API. News API is a simple HTTP REST API for searching and retrieving live articles from all over the web. (https://newsapi.org/docs).

Once you have get the api-key, you can also access the link using api-key and retrieve the data.
https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=<api-key>


Situation:
----------
The project involved automating the process of retrieving data from a website using a Python script and an API key. The data would be written to a text file, although this approach might not be suitable for large datasets.

Task:
------
The task was to create a Python automation script that retrieves live data from an authorized website using the provided API key, and then writes the retrieved data to a text file.

Action:
--------
Requested the API key to gain authorized access to the website's live data.
Wrote a Python script that used the API key to send requests to the website and retrieve the data.
The data retrieved was then written to a text file.
The script was designed using the requests library for handling API calls, referring to the REST API and Python documentation for proper implementation.
For larger datasets, a suggestion was made to use Python's pandas library to perform data exploration and analysis more effectively.

Result:
-------
The automation successfully retrieved live data from the website and stored it in a text file. The solution works for smaller datasets, but larger datasets can be handled more efficiently using pandas for analysis.

Project Code Link => https://github.com/anjalibh100/Automation-with-Python/blob/main/python-automation-example.ipynb
