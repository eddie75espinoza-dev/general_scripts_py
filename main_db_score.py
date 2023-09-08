"""
usage: 
    main_db_score.py save <data>
    main_db_score.py consult-all
    main_db_score.py consult-last
    main_db_score.py consult-date <date>

options:
save          Save record in database
consult-all   Consult all records
consult-last  Consult last record
consult-date  Consult record by date (yyyy-mm-dd)
"""
from docopt import docopt
from conn_database import Base, engine
from queries_score import (
    insert_data,
    get_all_data,
    get_data_date,
    get_last_data
)


if __name__ == '__main__':
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    arguments = docopt(__doc__, help=True, version=None, options_first=False)

    if arguments['save']:
        insert_data()
    elif arguments['consult-all']:
        get_all_data()
    elif arguments['consult-last']:
        get_last_data()
    elif arguments['consult-date']:
        get_data_date(arguments['<date>'])
