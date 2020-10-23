from orlem_connect.settings import STATIC_DIR
from bible.models import Reading
from datetime import date
import pandas as pd
import json


BIBLE_PATH = STATIC_DIR / 'res' / 'nrsv.csv'
BIBLE = pd.read_csv(BIBLE_PATH) # BIBLE INSTANCE


def put_in_list(dataframe, COLLATED_READINGS):
    for row in dataframe.itertuples():
        verse_num = int(row[1])
        verse_text = row[2]
        COLLATED_READINGS.append(verse_num)
        COLLATED_READINGS.append(verse_text)
    return COLLATED_READINGS
    

def query_bible(BOOK_NAME, READINGS):
    COLLATED_READINGS = []
    for chap in READINGS.keys():
        COLLATED_READINGS.append('Chapter %s' %chap)
        curated_read = BIBLE.loc[(BIBLE.book == BOOK_NAME) & (BIBLE.chapter == int(chap))]
        for chap_iter in READINGS[chap]:    
            try:
                if type(chap_iter) == list:
                    range_verse = curated_read.loc[(BIBLE.verse >= chap_iter[0]) & (BIBLE.verse < chap_iter[1]+1)].iloc[:, 3:5]
                    COLLATED_READINGS = put_in_list(range_verse, COLLATED_READINGS)
                elif type(chap_iter) == int:
                    atomic_verse = curated_read.loc[BIBLE.verse == chap_iter].iloc[:, 3:5]
                    COLLATED_READINGS = put_in_list(atomic_verse, COLLATED_READINGS)
                else:
                    print('Error occured, please check verse input')
            except Exception as e:
                print(e)
    return COLLATED_READINGS

           
def runner(BOOK_NAME, READINGS):
    COLLATED_READINGS = query_bible(BOOK_NAME, READINGS)
    response = {
        'book' : BOOK_NAME,
        'chapter' : READINGS,
        'text': [lines for lines in COLLATED_READINGS]
    }
    return response

def today_reading_setter():
    R = Reading.objects.filter(date = date.today())
    TODAY_READINGS = {}
    for r in R:
        print(r.reading)
        TODAY_READINGS[r.reading] = runner(r.book, json.loads(r.content))

    return TODAY_READINGS
    

if __name__ == '__main__':
    book_name = 'Genesis'   # Case sensitive, list always
    '''
        ----------- FOR readings for a given postion (1st, 2nd..etc) --------------
            1. Keys are chapter numbers
            2. Atomic values are isolated values given a particular chapter
            3. The nested list [[]] is a continuous sequence of readings
    '''
    readings_for_book_name = {
        1 : [[2, 6], 9, [10, 13]],
        5 : [1, [8,9], [15,19]]
    }
    
    print(runner(book_name, readings_for_book_name))