
from django.contrib import admin
from .models import user,student_details,cards

                                          
class useredit(admin.ModelAdmin):               
    search_fields = ['first_name']
    list_display = ['first_name','last_name','phone','course','address']
    list_filter=('course',) 

admin.site.register(user, useredit)
admin.site.register(student_details)
admin.site.register(cards)