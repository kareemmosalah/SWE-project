import csv
from datetime import date
from itertools import islice
import pathlib
from django.conf import settings
from django.core.management.base import BaseCommand
from myapp.models import Datacsv 


class Command(BaseCommand):
    help = 'Load data from data.csv file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'data.csv'

        with open(datafile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dt = date(
                    year=int(row['year']),
                    month=int(row['month']),
                    day=1
                )
                Datacsv.objects.get_or_create(date=dt, average=row['average'])