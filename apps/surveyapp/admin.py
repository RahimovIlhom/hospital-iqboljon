from django.contrib import admin
from .models import PatientData


@admin.register(PatientData)
class PatientDataAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Bemor haqida ma\'lumot', {
            'fields': ('fullname', 'age')
        }),
        ('Xavf omillari', {
            'fields': (
                'housing_or_working_conditions',
                'smoking',
                'cold_exposure',
                'contact_with_allergens',
                'hereditary_predisposition'
            )
        }),
        ('Anamnez', {
            'fields': (
                'onset_of_disease',
                'course_of_disease',
                'attack_course',
                'treatment_effectiveness'
            )
        }),
        ('Shikoyat', {
            'fields': (
                'cough',
                'cough_attack',
                'phlegm',
                'what_sputum',
                'shortness_of_breath',
                'what_suffocation',
                'pain',
                'temperature',
                'what_temperature'
            )
        }),
        ('Nafas shovqinlari', {
            'fields': ('breath_sound_types', 'breath_sound_location')
        })
    )

    list_display = ('fullname', 'age', 'created_at')
    list_filter = ('created_at', 'age')
    search_fields = ('fullname',)
    readonly_fields = ('created_at',)
