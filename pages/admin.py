from django.contrib import admin
from pages.models import Faq, Term, SalesOffice, Country, LocalStore, Distributor, Project, Image


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    list_display_links = ['question', ]


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ['name', 'condition']
    list_display_links = ['name', ]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_display_links = ['name', ]


@admin.register(SalesOffice)
class SalesOfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'country', 'state', 'city', 'email', 'website']
    list_display_links = ['name', 'email']
    list_filter = ['region', 'country', 'state', 'city']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(LocalStore)
class LocalStoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'city', 'email']
    list_display_links = ['name', 'email']
    list_filter = ['state', 'city']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'phone']
    list_display_links = ['name', ]
    list_filter = ['location', ]


class ImageInline(admin.TabularInline):
    model = Image
    extra = 8


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'year']
    list_display_links = ['name', ]
    list_filter = ['area', 'year']
    prepopulated_fields = {'slug': ('name', 'area', 'year')}
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['project', ]
    list_display_links = ['project', ]
