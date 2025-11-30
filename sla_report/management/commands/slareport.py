import csv
import json
import logging
import requests

from datetime import timedelta
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from sla_report.models import Sla_Report

logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = 'manage data for sla_report application'

    def add_arguments(self, parser):
        parser.add_argument('--truncate', action='store_true', help='truncate data')

        parser.add_argument('--update', action='store_true', help='update data')

        parser.add_argument('--target', action='store', dest='target',
                            help='Set minion target data', default='*')

    def handle(self, *args, **kwargs):
        """
        Command to create list of system information/stats
        """

        if kwargs['truncate']:
            Sla_Report.objects.all().delete()
            return

        timestamp = timezone.now()

        #if settings.PURGE_OLD_RECORDS:
        #    ts = timestamp - timedelta(settings.PURGE_OLDER_THAN)
        #    obj = Sla_Report.objects.filter(last_update__lt=ts).delete()

        #self._get_info(kwargs['target'], timestamp)
        self._get_data(timestamp)

    def _get_data(self, timestamp):
        with open("/app/sla_report/sla_report.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            header1 = next(csvreader)
            for row in csvreader:
                (product, uptimeT, uptime30, uptime90, uptime90d, uptime365, group)=row
                #print("%s :: %0.3f :: %0.3f :: %0.3f ::  %0.3f ::  %0.3f :: %s" % (product, uptimeT, uptime30, uptime90, uptime90d, uptime365, group))
                results = {'uptimeT': float(uptimeT),
                        'uptime30': float(uptime30),
                        'uptime90': float(uptime90),
                        'uptime90d': float(uptime90d), 
                        'uptime365': float(uptime365),
                        'last_update': timestamp,
                        'group': group
                    }
                #for key in results:
                #    print(results[key])

                obj, created = Sla_Report.objects.update_or_create(name=product, defaults = (results))
                if created:
                    self.stdout.write(self.style.SUCCESS('Added new product "{}" to sla_report table'.format(product)))

                obj.save()

        self.stdout.write(self.style.SUCCESS('Finished updating sla_report table'))
