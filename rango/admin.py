from django.contrib import admin
from rango.models import Category, Page


admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
#admin.site.register(Page, PageAdmin)

	
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)	
	
	
