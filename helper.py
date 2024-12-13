import pandas as pd
import sqlite3


class MyDB():
    ''' Defines a class that will keep track of a SQLite database cursor and has methods
        to save databases to their respective tables.
    
        Methods:
            __init__
            save_table
            get_table
            query
            
        Attributes:
            db: the database object
            cursor: SQLite cursor for the database
            names: names of the tables for convenience        
    '''
    
    db = None
    cursor = None
    names = ['Library', 'Document', 'Token', 'Vocabulary']
    
    def __init__(self, db_name):
        ''' Initialize the database wrapper.
            Arguments:
                string db_name: name of the database you want this object to create/communicate with
        '''
        if not db_name.endswith('.db'):
            db_name += '.db'
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()
    
    def save_table(self, table_object, table_name,
                   index = True, chunksize = 1000, 
                   if_exists = 'replace', confirm = False):
        ''' Saves all tables of a specific form into the database
            Arguments:
                list table_objects: a list of 4 pd.DataFrame objects representing the 4 tables:
                                    LIBRARY
                                    DOC
                                    TOKEN
                                    VOCAB
                (optional)
                bool index: save the index with the df (default True)
                int chunksize: number of rows to write to the database at once (default 1000)
                string if_exists: what to do if the tables already exist (default 'replace')
                bool confirm: whether or not to execute a uery on the table you just saved to confirm it was written to the database
        '''
        
        if isinstance(table_object, list):
            if table_name == 'all':
                    table_name = ['Library', 'Document', 'Token', 'Vocabulary']
            if len(table_object) != len(table_name):
                    raise ValueError('Mismatching input: table list len', len(table_object), 'and name list len', len(table_name))

            for i in range(len(table_object)):
                

                self.save_table(table_object[i], table_name[i], index = index, chunksize = chunksize,
                          if_exists = if_exists, confirm = confirm)
        
        elif isinstance(table_object, pd.DataFrame):
            table_object.to_sql(table_name, self.db, 
                                index = index, chunksize = chunksize, 
                                if_exists = if_exists)
            if confirm:
                print(f'Saved table {table_name}:')
                display(self.query(f'SELECT * FROM {table_name};'))
        else:
            raise TypeError(f'Cannot save object of type {dtype(table_object)}')
                
    def get_table(self, table):
        ''' For users unfamiliar with SQL, returns a whole table from the database
            Arguments:
                string table: the name of the table to retrieve from the database
        '''
        return self.query(f'SELECT * FROM {table};')
            
    def query(self, q):
        ''' Executes a query and returns a padas dataframe with column lables
            Arguments:
                string q: SQL query string to execute
        '''
        self.cursor.execute(q)
        colnames = [x[0] for x in self.cursor.description]
        df = self.cursor.fetchall()
        return pd.DataFrame(df, columns = colnames)
    
def display_tables(df, form, table = None, sample = 3):
    ''' Helper function to show all of the tables in a specific form at once'''
    if isinstance(df, list):
        if table == 'all':
            table = ['Library', 'Document', 'Token', 'Vocabulary']
        if len(df) != len(table):
            raise ValueError('Mismatching input: df list len', len(df), 'and name list len', len(table))
        for i in range(len(df)):
            display_tables(df[i], form, table = table[i], sample = sample)
    else:
        if table is None:
            table = ''
        else:
            table += ' '
        columns = df.columns
        if len(columns) > 10:
            columns = columns[:10]
            
        print(f'F{form} {table}table sample:')
        display(df.sample(sample)[columns])