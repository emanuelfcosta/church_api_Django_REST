from django.contrib import admin

from church.models import Member, Church, Financial, Occasion, Prayer, Study


class Members(admin.ModelAdmin):
    list_display = (
        'id', 'status', 'role', 'baptismdate', 'addmission',
        'name', 'gender', 'birthdate', 'address', 'state', 'occupation',
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'address', 'occupation')
    list_filter = ('status', 'role', 'state')
    ordering = ('name',)
    list_per_page = 20



class Churches(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'responsible', 'city', 'state',
        'cnpj', 'phone', 'foundationdate'
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'city', 'cnpj')
    list_filter = ('state', 'type')
    ordering = ('name',)
    list_per_page = 20



class Financials(admin.ModelAdmin):
    list_display = (
        'id', 'type', 'description', 'amount',
        'theDate', 'paymentMethod'
    )
    list_display_links = ('id', 'description')
    search_fields = ('description', 'type')
    list_filter = ('type', 'paymentMethod', 'theDate')
    ordering = ('-theDate',)
    list_per_page = 20



class Occasions(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'start', 'end'
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('start', 'end')
    ordering = ('start',)
    list_per_page = 20



class Prayers(admin.ModelAdmin):
    list_display = (
        'id', 'reason', 'priority', 'status'
    )
    list_display_links = ('id', 'reason')
    search_fields = ('reason', 'description')
    list_filter = ('priority', 'status')
    ordering = ('priority',)
    list_per_page = 20



class Studies(admin.ModelAdmin):
    list_display = (
        'id', 'subject', 'theDate'
    )
    list_display_links = ('id', 'subject')
    search_fields = ('subject', 'description')
    list_filter = ('theDate',)
    ordering = ('-theDate',)
    list_per_page = 20



admin.site.register(Member, Members)
admin.site.register(Church, Churches)
admin.site.register(Financial, Financials)
admin.site.register(Occasion, Occasions)
admin.site.register(Prayer, Prayers)
admin.site.register(Study, Studies)