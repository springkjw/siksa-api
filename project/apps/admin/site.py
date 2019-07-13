from django.contrib import admin


class SiksaAdminSite(admin.AdminSite):
    site_title = '식사 프로젝트'
    site_header = '식사 프로젝트'
    index_title = '통합 관리'