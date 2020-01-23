from django.contrib import admin
from .forms import CustomUserCreationForm
from django.utils.html import format_html
from hospital.models import Hospital
from vehicle.models import Vehicle,VehicleCategory
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.apps import apps
class HospitalAdmin(admin.ModelAdmin):
    list_display_links = None
    change_form_template = 'admin/hospital/change_form.html'
    change_list_template = 'admin/hospital/change_list.html'
    form = CustomUserCreationForm
    model = Hospital
    list_display = ('full_name','email', 'phone','address','status','Action')
    list_filter = ('status',)
    list_per_page = 5   #For Pagination

    fieldsets = (
        (None, {'fields': ('full_name','email','phone','address','status','password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email','phone','status','password', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('-id',)
    
    def Action(self, obj):
        if(obj.status == 3):
            delete = ''
            edit   = ''
            add    = ''
        else: 
            delete = '<a class="button delete_hospital_user trash-icon" title="Delete" data-id="%s" href="delete/%s"><i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;' % (
                obj.id, obj.id)
            add = '<a class="button" title="Add Vehicle" href="add_vehicle/%s"><i class="fa fa-plus" aria-hidden="true"></i></a>&nbsp;' % (
            obj.id)
            edit   = '<a class="button edit-icon" title="Edit" data-id="%s" href="/admin/hospital/hospital/%s/change/"><i class="fa fa-edit" aria-hidden="true"></i></a>&nbsp;' % (obj.id,obj.id)

        view = '<a class="button" title="View" href="view/%s"><i class="fa fa-eye" aria-hidden="true"></i></a>&nbsp;' % (
            obj.id)
        
        return format_html(view + delete + edit + add)
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url('^view/(?P<hospital_id>\d+)/$', self.hospital_view),
            url('^add_vehicle/(?P<hospital_id>\d+)/$', self.vehicle_add),
        ]
        return my_urls + urls
    
    def extra_context(self, request):
        context = admin_site.each_context(request)
        context['opts'] = Hospital._meta
        context['site_title'] = ugettext_lazy('Hospital')
        return context


    @method_decorator(login_required())
    def vehicle_add(self, request,hospital_id):
        context = self.extra_context(request)
        context['title'] = 'Add Vehicle'
        context['data'] = Hospital.objects.get(id=hospital_id)
        context['category'] = VehicleCategory.objects.all()
        return TemplateResponse(request, 'admin/hospital/add_vehicle.html', context=context)

    @method_decorator(login_required())
    def hospital_view(self, request,hospital_id):
        context = self.extra_context(request)
        context['title']      = 'Hospital User Details'
        context['userDetail'] = Hospital.objects.get(id=hospital_id)
        context['Vehicle']    = Vehicle.objects.filter(user_id = hospital_id).filter(user_type = 1)
        context['site_title'] = ugettext_lazy('Hospital')
        return TemplateResponse(request, 'admin/hospital_view.html', context=context)

admin_site.register(Hospital,HospitalAdmin)
