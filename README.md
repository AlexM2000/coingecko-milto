# How to run code
1. In separate virtualenv run on command line/bash go to project root directory. 
2. Run `pip install -r requirements.txt`
3. Run `python main.py --db_name=coins.db`. Or use any other output database name. 
   Database file will be created in the same directory where command was executed.

### OR

1. In separate virtualenv run `pip install coingecko_milto`.
2. Run `etl --db_name=coins.db`. Or use any other output database name. 
   Database file will be created in the same directory where command was executed.

If SQLite database doesn't exist, it will create new database and write data there.
