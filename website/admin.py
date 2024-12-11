from django.contrib import admin

# Register your models here.
from .models import Service
admin.site.register(Service)


from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email', 'date_registered')
    search_fields = ('first_name', 'last_name', 'email')



from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total')
    search_fields = ('customer',)

admin.site.register(Order, OrderAdmin)



from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date')
    search_fields = ('patient',)
    list_filter = ('date',)

admin.site.register(Appointment, AppointmentAdmin)



from .models import SurveyAnswer

class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ('survey_id', 'question', 'answer')
    search_fields = ('question', 'answer')
    list_filter = ('survey_id',)

admin.site.register(SurveyAnswer, SurveyAnswerAdmin)


