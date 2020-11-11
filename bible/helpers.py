from .models import Reading, ReadingVerse
from django.core import serializers
from .reading_getter import runner
from datetime import date
import json



def cache_todays_reading():
    R = Reading.objects.filter(date = date.today()).order_by('reading')
    TODAY_READINGS = {}
    for r in R:
        print(r.reading)
        RV = ReadingVerse.objects.filter(reading = r).order_by("chapter", "start_verse")
        TODAY_READINGS[r.reading] = runner(r.book, RV)

    return TODAY_READINGS


def add_reading(date, reading, book, content):
    try:
        R = Reading.objects.filter(date = date, reading = reading).first()
        #print(date); print(book); print(content)
        if not R:
            R = Reading(date = date, reading = reading, book = book)
            print("Added Reading")
            R.save()             

        RV = ReadingVerse.objects.filter(reading = R)
        RV.delete() ### delete all currently saved verses for reading;

        for chapter in content:
            for verse_group in content[chapter]:
                if type(verse_group) == int:
                    RV = ReadingVerse(reading = R, chapter = int(chapter), start_verse = verse_group, end_verse = False)
                else:
                    RV = ReadingVerse(reading = R, chapter = int(chapter), start_verse = verse_group[0], end_verse = verse_group[1])
                RV.save()
        return True
    except Exception as e:
        #print(e)
        return False


def get_reading(date):
    print(date)
    readings = {}

    R = Reading.objects.filter(date = date)
    for r in R:
        #RV = ReadingVerse.objects.filter(reading = r.id)
        RV = ReadingVerse.objects.filter(reading = r).order_by("chapter", "start_verse")
        readings[r.reading] = runner(r.book, RV)
        #readings[r.reading] = serializers.serialize("json", )

    return readings


def delete_reading(date, reading):
    R = Reading.objects.filter(date = date)
    if reading != "*":
        R = R.filter(reading = reading)
    
    try:
        R.delete()
        return True

    except Exception as e:
        print(e)
        return False;