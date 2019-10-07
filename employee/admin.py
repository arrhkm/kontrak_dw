from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Employee, Person, Leader, Group, GroupEmployee, NotifyEmail, EmailGroup, RegisterEmailGroup
from contract.models import Contract
# Register your models here.


@admin.register(Person)
class PersonAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ('name', 'idcard')
    list_filter = ('marital',)
    list_display = ('idcard', 'name', 'birth_of_date', 'phone', 'marital')
    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('idcard', 'name'),
                ('birth_city', 'birth_of_date'),
                ('gender', 'marital'),
                ('address', 'city'),
                ('phone', 'bank_account'),
                'tax_account'
            )
        }),
    )
    list_per_page = 20


class ContractLine(admin.StackedInline):
    autocomplete_fields = ('jabatan', 'project')
    fieldsets = (
        ('', {
            'fields': (
                ('number_contract', 'contract_type'),
                'doc_date',
                ('project', 'jabatan'),
                ('start_date', 'end_date'),
                'contract_distance',
                'besar_upah'
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

    model = Contract
    max_num = 2
    min_num = 1
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ('person__name',)
    autocomplete_fields = ('person',)
    list_filter = ('is_permanent',)
    list_display = ['reg_number', 'person', 'date_of_hired', 'is_permanent', 'number_bpjstk', 'number_bpjskes', 'email']
    fieldsets = (
        ('Employee Information', {
            'fields': (('reg_number', 'person'), 'date_of_hired', 'is_permanent')
        }),
        ('Other Information', {
            'fields': (('number_bpjstk', 'number_bpjskes'), 'email')
        })
    )

    inlines = [ContractLine]


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'jabatan')
    list_display = ['name', 'email', 'jabatan']


class GroupEmployeeInline(admin.TabularInline):
    autocomplete_fields = ('employee',)
    model = GroupEmployee
    extra = 0
    min_num = 1


class RegisterEmailGroupInline(admin.TabularInline):
    autocomplete_fields = ('email_group',)
    model = RegisterEmailGroup
    extra = 0
    min_num = 1
    classes = ('collapse',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    autocomplete_fields = ('leader',)
    list_display = ['name', 'leader']
    inlines = [GroupEmployeeInline, RegisterEmailGroupInline]


@admin.register(NotifyEmail)
class NotifyEmailAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailGroup)
class EmailGroupAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')
    list_display = ('name', 'email')


@admin.register(GroupEmployee)
class GroupEmployeeAdmin(admin.ModelAdmin):
    list_display = ('group',)
