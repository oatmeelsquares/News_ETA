# Project Manifest
Becky Desrosiers | rn7ena@virginia.edu | DS5001 F24 | 13 December, 2024

Link to this project on GitHub: https://github.com/oatmeelsquares/News_ETA

## Project description
In partial fulfillment of the requirements of DS5001: Exploratory Text Analytics at the University of Virginia School of Data Science. This project extracts unstructured text data into forms 2-5 and investigates them using a variety of visualizations.

## Source data
File: newzy.zip

Obtained from: Professor Rafael Alvarado

Location: https://virginia.app.box.com/s/bj8f1khrkfd6thm9umq35m6xp2an4zej/file/624341579635

Description: A collection of 1,026,347 snippets from American news articles dating November 05, 2013 to February 27, 2020. Articles are gathered from a range of 16 different sources, from CNN to Fox. Due to time and computation constraints, 10,000 documents were randomly sampled with seed = 5001 to be used for analysis.

Format: (zipped) CSV with columns

- doc_id
- doc_source
- doc_title
- doc_content
- doc_date
- doc_url

## Project report
File: [rn7ena_news_report.pdf](https://github.com/oatmeelsquares/News_ETA/blob/main/rn7ena_news_report.pdf)

Purpose: Provide a high-level summary of results and what I learned from this project.

## Text processing
File: [rn7ena_news_processing.ipynb](https://github.com/oatmeelsquares/News_ETA/blob/main/rn7ena_news_processing.ipynb)

Purpose: Produce data in all tables F2 through F5, save as SQLite databases.

## Exploratory Analysis
File: [rn7ena_news_eta.ipynb](https://github.com/oatmeelsquares/News_ETA/blob/main/rn7ena_news_eta.ipynb)

Purpose: Explore the tables using statistical and visual analysis.

## Helper module
File: [helper.py](https://github.com/oatmeelsquares/News_ETA/blob/main/helper.py)

Purpose: Defines a wrapper class `MyDB` for easy manipulation of SQLite databases, and a helper function to pretty print all relevant dataframes of a given form.

## Sentiment Lexicon
File: [sales_nrc.csv](https://github.com/oatmeelsquares/News_ETA/blob/main/salex_nrc.csv)

Purpose: Used to apply sentiments to terms for F5. From the NRC Word-Emotion Association Lexicon (aka EmoLex).

Obtained from: Professor Rafael Alvarado

## Word2Vec model
File: word2vec.model

Purpose: Saves vectorized vocabulary along with convenience methods for semantic algebra and other analysis.

## F2 through F5 data tables
Directory: tables (tables.zip)

Format: SQLite and CSV

Files:
- F2.db includes:
    - Library table with columns:
        - doc_id (index)
        - doc_source
        - doc_title
        - doc_date
        - doc_url
    - Document table with columns:
        - doc_id (index)
        - doc_content
    - Token table with columns:
        - doc_id (OHCO index 0)
        - sent_num (OHCO index 1)
        - token_id (OHCO index 2)
        - token
    - Vocabulary table with columns:
        - term_id (index)
        - term
        - count
- F3.db includes:
    - Library table (same as F2)
    - Document table (same as F2)
    - Token table with additional columns:
        - pos
        - term
        - term_id
    - Vocabulary table with additional columns:
        - punctuation (boolean)
        - numeric (boolean)
        - stopword (boolean)
        - stem
        - pos_max
- F4.db includes:
    - Library table (same as F2 & F3)
    - Document table (same as F2 & F3)
    - Token table (same as F3)
    - Vocabulary table with additional column:
        - tfidf_sum
- TFIDF.csv (part of F4 & F5, but too many columns for SQLite)
- F5.db includes:
    - Library table (same as F2-4)
    - Document table (same as F2-4)
    - Token table (same as F3 & F4)
    - Vocabulary table with additional column:
        - max_topic_id
    - Additional tables:
        - Topics with columns:
            - topic_id (index)
            - label
            - doc_weight_sum
        - Theta (doc-topic table) columns:
            - doc_id (index)
            - 0-14 (topic_id)
        - Principal_Components columns:
            - principle_component (index)
            - explained_variance
            - eigenvalue
        - Loadings (Principle Components) with columns:
            - term_id (index)
            - PCX_loading for X = 0-9
        - Phi (topic-word table) with columns:
            - term_id (index)
            - 0-14 (topic_id)
        - Vectors (Word2Vec embeddings) with columns:
            - term_id (index)
            - word_vector\[X\] for X = 0-49
        - Sentiments with index term_id and columns:
            - anger
            - anticipation
            - disgust
            - fear
            - joy
            - positive
            - negative
            - sadness
            - surprise
            - trust
            - polarity
