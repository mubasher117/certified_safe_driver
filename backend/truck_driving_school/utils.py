import csv
from django.conf import settings
from .models import *


def create_first_day_training_record(test):
    items = [
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Introduction to Truck Driving School -STRETCHING',
            'day': 1,
            'location': 'classroom',
            'planned': 0.25,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Federal Regualtions',
            'day': 1,
            'location': 'classroom',
            'planned': 0.25,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Hours of Service',
            'day': 1,
            'location': 'classroom',
            'planned': 0.25,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Emergency Equipment',
            'day': 1,
            'location': 'classroom',
            'planned': 0.32,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Mirrors',
            'day': 1,
            'location': 'classroom',
            'planned': 0.17,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Accident procedures',
            'day': 1,
            'location': 'classroom',
            'planned': 0.25,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'DVIR Review',
            'day': 1,
            'location': 'classroom',
            'planned': 0.17,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Stopping Distance',
            'day': 1,
            'location': 'classroom',
            'planned': 0.25,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Skid Control',
            'day': 1,
            'location': 'classroom',
            'planned': 0.50,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Distracted driving Quiz',
            'day': 1,
            'location': 'classroom',
            'planned': 0.17,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Defensive Driving Quiz',
            'day': 1,
            'location': 'classroom',
            'planned': 0.17,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Defensive driving presentation',
            'day': 1,
            'location': 'classroom',
            'planned': 1.75,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'In Cab Inspection',
            'day': 1,
            'location': 'classroom',
            'planned': 0.50,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Group Pre-trip training',
            'day': 1,
            'location': 'yard',
            'planned': 2.00,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Group Yard Skills training',
            'day': 1,
            'location': 'yard',
            'planned': 2.00,
            'actual': 0.00,
            'initials': 0.00,
        }),
    ]

    records = DriverTrainigRecord.objects.bulk_create(items)
    return records


def create_next_day_training_record(test, day):
    next_day_items = [
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Stretching',
            'day': day,
            'location': 'classroom',
            'planned': 0.32,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Pre - trip training',
            'day': day,
            'location': 'yard',
            'planned': 1.75,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Yard Skills training',
            'day': day,
            'location': 'yard',
            'planned': 2.00,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Behind the Wheel training',
            'day': day,
            'location': 'btw',
            'planned': 4.25,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Post-trip training',
            'day': day,
            'location': 'yard',
            'planned': 0.17,
            'actual': 0.00,
            'initials': 0.00,
        }),
        DriverTrainigRecord(**{
            'test_id': test,
            'title': 'Review',
            'day': day,
            'location': 'classroom',
            'planned': 0.51,
            'actual': 0.00,
            'initials': 0.00,
        })
    ]
    new_items = DriverTrainigRecord.objects.bulk_create(next_day_items)
    return new_items


def create_days_from_csv_template(company_id, test_id):
    csv_template = TrainingRecordCSVTemplate.objects.get(company_id=company_id)
    read_file = csv_template.csv_file.read().decode('utf-8').splitlines(True)
    fieldnames = ['title', 'day', 'location', 'planned', 'actual', 'initials', 'position']
    csv_reader = csv.DictReader(read_file, fieldnames=fieldnames)
    line_count = 0
    items = []

    for row in csv_reader:
        # print(row)
        line_count += 1
        if line_count != 1:
            title = row['title']
            day = row['day']
            location = row['location']
            planned = row['planned']
            actual = row['actual']
            initials = row['initials']
            position = 0
            if 'position' in row:
                position = row['position']
            # print(day)
            if day != "":
                item = DriverTrainigRecord(**{
                    'test_id': test_id,
                    'title': title,
                    'day': int(day),
                    'location': location,
                    'planned': planned,
                    'actual': actual,
                    'initials': initials,
                    'position': position,
                })
                items.append(item)

    if len(items) > 0:
        # print(items)
        records = DriverTrainigRecord.objects.bulk_create(items)
        return records

    print(f'Processed {line_count} lines.')
    return None
