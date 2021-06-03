from django.contrib import admin
from .models import CAREER, Gallery, Services, Executive

# Register your models here.

admin.site.register(CAREER)
admin.site.register(Gallery)
admin.site.register(Services)
admin.site.register(Executive)

admin.site.site_header = 'Matrix Security Company'
admin.site.site_title =  'Matrix Security Company'
