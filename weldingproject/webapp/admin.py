from django.contrib import admin
from .models import Project, Contact, Review


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created_at',
    )



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'created_at',
    )



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'rating',
        'created_at',
    )