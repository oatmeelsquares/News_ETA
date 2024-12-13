# Project manifest
Becky Desrosiers | rn7ena@virginia.edu | DS5001 F24 | 13 December, 2024

Link to this project on GitHub: https://github.com/oatmeelsquares/News_ETA

## Project description

In partial fulfillment of the requirements of DS5001: Exploratory Text Analytics at the University of Virginia School of Data Science. This project extracts unstructured text data into forms 2-5 and investigates them using a variety of visualizations.

## Source data

File: newzy.zip

Obtained from: Raf Alvarado

Location: https://virginia.app.box.com/s/bj8f1khrkfd6thm9umq35m6xp2an4zej/file/624341579635

Description: A collection of 1,026,347 snippets from American news articles dating November 05, 2013 to February 27, 2020. Articles are gathered from a range of sources, from CNN to Fox. Due to time and computation constraints, 10,000 documents were randomly sampled with seed = 5001 to be used for analysis.

Format: CSV with columns
        - doc_id
        - doc_source
        - doc_title
        - doc_content
        - doc_date
        - doc_url
        
## Text processing

File: rn7ena-ds5001-final-project-code.ipynb

Purpose: Produce data in all tables F2 through F5, save as SQLite databases.

## Exploratory Analysis
File: rn7ena-final-project-eta.ipynb

Purpose: Explore the tables using statistical and visual analysis.

## Helper module

File: helper.py

Purpose: Defines a wrapper class `MyDB` for easy manipulation of SQLite databases, and a helper function to pretty print all relevant dataframes of a given form.

## Sentiment Lexicon

File: sales_nrc.cev

Purpose: Used to apply sentiments to terms for F5. From the NRC Word-Emotion Association Lexicon (aka EmoLex).

Obtained from: Raf Alvarado

## Word2Vec model

File: word2vec.model

Purpose: Saves vectorized vocabulary along with convenience methods for semantic algebra and other analysis.

## F2 through F5 data tables

Directory: tables

Format: SQLite

Files:
- F2.db
- F3.db
- F4.db
- TFIDF.csv
- F5.db