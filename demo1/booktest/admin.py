from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
class HeroInfoInlne(admin.StackedInline):
    model = HeroInfo
    extra = 1
class BookInfoInlne(admin.StackedInline):
    model = BookInfo
    extra = 1
class HeroInfoAdmin(admin.ModelAdmin):
    list_per_page = 1
    list_display = ['name','gender']
    search_fields = ['name']
    list_filter = ['name']

    # inlines = [BookInfoInlne]
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle','pub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 1
    #关联添加
    inlines = [HeroInfoInlne]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)