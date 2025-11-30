from django.urls import re_path

from sla_report.views import sla_report

urlpatterns = [
    re_path(r'', sla_report.as_view()),
]
