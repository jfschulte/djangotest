from django.contrib import admin
from redapp.models import Category, Page, UserProfile, RedditUserName, FavRedditor

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)
admin.site.register(RedditUserName)
#admin.site.register(UserFavorites)
admin.site.register(FavRedditor)