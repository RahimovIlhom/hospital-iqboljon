from django.db import models


class PatientData(models.Model):
    # Platform
    fullname = models.CharField(max_length=255, verbose_name="Bemor FISH")
    age = models.CharField(max_length=50, verbose_name="Yosh")

    # Risk Factors
    housing_or_working_conditions = models.CharField(max_length=255, verbose_name="Turar joy, ish sharoiti")
    smoking = models.CharField(max_length=255, verbose_name="Chekish")
    cold_exposure = models.CharField(max_length=4, verbose_name="Sovuq qotish")
    contact_with_allergens = models.CharField(max_length=4, verbose_name="Allergenlar bilan kontakt")
    hereditary_predisposition = models.CharField(max_length=4, verbose_name="Irsiy moyillik")

    # Medical History
    onset_of_disease = models.CharField(max_length=50, verbose_name="Kasallik boshlanishi")
    course_of_disease = models.CharField(max_length=50, verbose_name="Kasallik kechishi")
    attack_course = models.CharField(max_length=4, verbose_name="Xurujli kechishi")
    treatment_effectiveness = models.CharField(max_length=50, verbose_name="Davo samaradorlik")

    # Complaints
    cough = models.CharField(max_length=4, verbose_name="Yo'tal")
    cough_attack = models.CharField(max_length=50, null=True, blank=True, verbose_name="Yo'tal xuruji")
    phlegm = models.CharField(max_length=4, verbose_name="Balg'am")
    what_sputum = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qanday balg'am")
    shortness_of_breath = models.CharField(max_length=4, verbose_name="Xansirash")
    what_suffocation = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qanday xansirash")
    pain = models.CharField(max_length=4, verbose_name="Og'riq")
    temperature = models.CharField(max_length=4, verbose_name="Harorat")
    what_temperature = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qanday harorat")

    # Breath Sounds
    breath_sound_types = models.JSONField(verbose_name="Nafas shovqini turi")
    breath_sound_location = models.JSONField(verbose_name="Lokalizatsiya")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Bemor"
        verbose_name_plural = "Bemorlar"
        ordering = ["-created_at"]
