from django.contrib import admin

# Register your models here.
from labreports.models import Lab_report,Lab_test
admin.site.register(Lab_report)
admin.site.register(Lab_test)
