from django.contrib import admin

from import_export.admin import ImportExportMixin
from fsm_admin.mixins import FSMTransitionMixin

from .models import ContractType, Contract, Jabatan


# Register your models here.

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Contract)
class ContractAdmin(FSMTransitionMixin, ImportExportMixin, admin.ModelAdmin):
    autocomplete_fields = ('employee', 'jabatan')
    search_fields = ('number_contract', 'employee__person__name')
    list_filter = ('project__name', 'contract_type__contract_name')
    list_display = [
        'number_contract', 'employee', 'contract_type'
        , 'start_date', 'end_date','contract_distance', 'project'
    ]
    fieldsets = (
        ('', {
            'fields': (
                ('number_contract', 'contract_type'),
                'doc_date',
                ('project', 'jabatan'),
                ('start_date', 'end_date'),
                'contract_distance',
                'besar_upah',
                'status'
            ),
        }),
        ('Company Information', {
            'fields': (
                'corporate_name',
                'corporate_address',
                ('jenis_usaha', 'cara_pembayaran'),
                ('tempat_aggrement', 'pejabat_acc')

            ),
            'classes': ('collapse', 'extrapretty')
        })
    )
    fsm_field = ['status',]
    readonly_fields = ['status', ]
    list_per_page = 20


@admin.register(Jabatan)
class JabatanAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ('nama',)
