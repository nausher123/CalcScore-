from django.contrib import admin
from .models import ThresholdData, ThresholdData1, ThresholdData_O, Sat_Curves, ThresholdData_OP


admin.site.register(ThresholdData)
admin.site.register(ThresholdData1)
admin.site.register(ThresholdData_O)
admin.site.register(Sat_Curves)

admin.site.register(ThresholdData_OP)




# Register your models here.
