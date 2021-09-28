from django.contrib import admin
from. models import Frequently_Asked_Questions, Notice, Social_Media, Terms_and_Conditions, Website_Details

admin.site.register(Website_Details)
admin.site.register(Social_Media)
admin.site.register(Notice)
admin.site.register(Terms_and_Conditions)
admin.site.register(Frequently_Asked_Questions)

