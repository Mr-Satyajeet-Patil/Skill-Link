from django.contrib import admin 
from django.http import HttpResponse
from .utils import render_to_pdf
from .models import *
admin.site.register(company)
admin.site.register(freelancer)
admin.site.register(freelancerexperience)
admin.site.register(project)
admin.site.register(bid)
admin.site.register(paymentcompany)
admin.site.register(paymentfreelancer)
admin.site.register(feedback)
admin.site.register(notification)
admin.site.register(quizresult)
admin.site.register(questionnaire)
admin.site.register(projectcategory)

admin.site.register(allotment)


class enquiryadmin(admin.ModelAdmin):
    list_display=['name','email','mobile','message','date']
    list_filter=['name','date']
    search_fields=['name','email','mobile','message']

   
    
    actions=['download_pdf']
    
    #pdf
    def download_pdf(self, request, queryset):
        ids = queryset.values_list('id', flat=True)
        pdf = render_to_pdf('enquiry_reports.html', {'enquiry': queryset})
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="enquiries.pdf"'
        return response
    
    download_pdf.short_description = "Download PDF of selected enquiries"

admin.site.register(enquiry, enquiryadmin)

# Register your models here.
