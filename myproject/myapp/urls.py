from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pm_master/$', views.pmindex, name='pmindex'),
    url(r'^pm_master/add$', views.pmadd, name='pmadd'),
    url(r'^pm_master/create$', views.pmcreate, name='pmcreate'),
    url(r'^pm_master/edit/(?P<id>\d+)$', views.pmedit, name='pmedit'),
    url(r'^pm_master/edit/update/(?P<id>\d+)$', views.pmupdate, name='pmupdate'),
    url(r'^pm_master/delete/(?P<id>\d+)$', views.pmdelete, name='pmdelete'),

    url(r'^jobsheet_trace/$', views.sheetindex, name='sheetindex'),
    url(r'^jobsheet_trace/add/$', views.sheetadd, name='sheetadd'),
    url(r'^jobsheet_trace/add/create$', views.sheetcreate, name='sheetcreate'),
    url(r'^jobsheet_trace/edit/(?P<id>\d+)$', views.sheetedit, name='sheetedit'),
    url(r'^jobsheet_trace/edit/update/(?P<id>\d+)$', views.sheetupdate, name='sheetupdate'),
    url(r'^jobsheet_trace/delete/(?P<id>\d+)$', views.sheetdelete, name='sheetdelete'),

    url(r'^jobsheet/$', views.jobindex, name='jobindex'),
    url(r'^jobsheet/add/$', views.jobadd, name='jobadd'),
    url(r'^jobsheet/add/create$', views.jobcreate, name='jobcreate'),
    url(r'^jobsheet/edit/(?P<id>\d+)$', views.jobedit, name='jobedit'),
    url(r'^jobsheet/edit/update/(?P<id>\d+)$', views.jobupdate, name='jobupdate'),
    url(r'^jobsheet/delete/(?P<id>\d+)$', views.jobdelete, name='jobdelete'),


    url(r'^omr/$', views.omrindex, name='omrindex'),
    url(r'^omr/add$', views.omradd, name='omradd'),
    url(r'^omr/create$', views.omrcreate, name='omrcreate'),
    url(r'^omr/edit/(?P<id>\d+)$', views.omredit, name='omredit'),
    url(r'^omr/edit/update/(?P<id>\d+)$', views.omrupdate, name='omrupdate'),
    url(r'^omr/delete/(?P<id>\d+)$', views.omrdelete, name='omrdelete'),


    url(r'^Part_Tracker/$', views.partindex, name='partindex'),
    url(r'^Part_Tracker/add/$', views.partadd, name='partadd'),
    url(r'^Part_Tracker/add/create$', views.partcreate, name='partcreate'),
    url(r'^Part_Tracker/edit/(?P<id>\d+)$', views.partedit, name='partedit'),
    url(r'^Part_Tracker/edit/update/(?P<id>\d+)$', views.partupdate, name='partupdate'),
    url(r'^Part_Tracker/delete/(?P<id>\d+)$', views.partdelete, name='partdelete'),

    url(r'^pm_chart/$', views.chartindex, name='chartindex'),
    url(r'^pm_chart/add/$', views.chartadd, name='chartadd'),
    url(r'^pm_chart/add/create$', views.chartcreate, name='chartcreate'),
    url(r'^pm_chart/edit/(?P<id>\d+)$', views.chartedit, name='chartedit'),
    url(r'^pm_chart/edit/update/(?P<id>\d+)$', views.chartupdate, name='chartupdate'),
    url(r'^pm_chart/delete/(?P<id>\d+)$', views.chartdelete, name='chartdelete'),

    url(r'^dashboard/$', views.dashindex, name='dashindex'),
    url(r'^dashboard/add/$', views.dashadd, name='dashadd'),
    url(r'^dashboard/add/create$', views.dashcreate, name='dashcreate'),
    url(r'^dashboard/edit/(?P<id>\d+)$', views.dashedit, name='dashedit'),
    url(r'^dashboard/edit/update/(?P<id>\d+)$', views.dashupdate, name='dashupdate'),
    url(r'^dashboard/delete/(?P<id>\d+)$', views.dashdelete, name='dashdelete'),

    url(r'^consume/$', views.conindex, name='conindex'),
    url(r'^consume/add/$', views.conadd, name='conadd'),
    url(r'^consume/add/create$', views.concreate, name='concreate'),
    url(r'^consume/edit/(?P<id>\d+)$', views.conedit, name='conedit'),
    url(r'^consume/edit/update/(?P<id>\d+)$', views.conupdate, name='conupdate'),
    url(r'^consume/delete/(?P<id>\d+)$', views.condelete, name='condelete'),
]