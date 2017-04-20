# cnn_text_classification
Build a model which automatically classifies an article under Finance, Law, Fashion and Lifestyle, using the data from leading magazines for training the model.

This text classification problem was solved using CNN in tensorflow. 

Details for the folder in the first commit:

raw_data/			Contains files related to train and test
├── collect_url_data.py		Python script that scrapes articles		
├── data			Training data folder
│   ├── fashion_7000.txt	7000 training data for class fashion
│   ├── finance_7000.txt	7000 training data for class finance
│   ├── law_7000.txt		7000 training data for class law
│   └── lifestyle_7000.txt	7000 training data for class lifestyle
├── fashion			From original scraped data and cleaned one
│   ├── fashion_7000.txt	7000 training data for class fashion
│   ├── fashion_original.txt	Original scraped data
│   ├── log			Log output of python
│   ├── test_fashion.txt	test data for python 1001 samples
│   ├── urls.txt		urls which were scraped
│   └── urltext.txt		raw text from urls
├── finance			From original scraped data and cleaned one
│   ├── finance.txt		raw text from urls
│   ├── finance_7000.txt	7000 training data for class finance
│   ├── finance_urls.txt	urls scraped for finance
│   ├── log_finance		log output
│   ├── original_finance.txt	Original scraped file
│   └── test_finance.txt	test sample for finance
├── law				Data folder for law
│   ├── law.txt			scraped data for law
│   ├── law_7000.txt		7000 training samples for law
│   ├── law_urls.txt		urls scraped for law
│   ├── log_law			log output
│   ├── original_law.txt	original scraped data for law
│   └── test_law.txt		test data for law
└── lifestyle			Data folder for lifestyle
    ├── lifestyle.txt		cleaned data for lifestyle
    ├── lifestyle_7000.txt	7000 training samples for lifestyle
    ├── lifestyle_urls.txt	urls collected for scraping
    ├── log_lifestyle		log output of the script
    ├── original_lifestyle.txt	original scraped data
    └── test_lifestyle.txt	test data for lifestyle



