from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from sla_report.models import Sla_Report

class sla_report(TemplateView):
    template_name = 'sla_report/summary.html'
    title = 'Summary'

    def data(self):
        filter = 'hotspot%'
        hotspot = Sla_Report.objects.raw('SELECT * FROM sla_report WHERE "group" LIKE %s ORDER BY name', [filter])
        filter1 = 'billing%' 
        billing = Sla_Report.objects.raw('SELECT * FROM sla_report WHERE "group" LIKE %s ORDER BY name', [filter1])       
        filter2 = 'subscription%'
        subscription = Sla_Report.objects.raw('SELECT * FROM sla_report WHERE "group" LIKE %s ORDER BY name', [filter2])

        products = Sla_Report.objects.raw('SELECT * FROM sla_report WHERE "group" LIKE %s ORDER BY name', [filter12])
 
        context = {
            'hotspot': hotspot,
            'billing': billing,
            'subscription': subscription,
        }

        return context

