from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import PatientData
from .serializers import PatientDataSerializer

class PatientDataCreateView(CreateAPIView):
    """
    Bemor ma'lumotlarini yaratish uchun API ko'rinishi.
    Faqat POST so'rovlarini qabul qiladi va elektron pochta xabarnomasi yuboradi.
    """
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            patient = serializer.save()

            # Email kontentini tayyorlash
            email_content = f"""
            Yangi bemor maʼlumotlari yuborildi:

            Bemor ma'lumotlari:
            - FISH: {patient.fullname}
            - Yosh: {patient.age}

            Xavf omillari:
            - Turar joy, ish sharoiti: {patient.housing_or_working_conditions}
            - Chekish: {patient.smoking}
            - Sovuq qotish: {patient.cold_exposure}
            - Allergenlar bilan kontakt: {patient.contact_with_allergens}
            - Irsiy moyillik: {patient.hereditary_predisposition}

            Kasallik tarixi:
            - Kasallik boshlanishi: {patient.onset_of_disease}
            - Kasallik kechishi: {patient.course_of_disease}
            - Xurujli kechishi: {patient.attack_course}
            - Davo samaradorlik: {patient.treatment_effectiveness}

            Shikoyatlar:
            - Yo'tal: {patient.cough}
            - Yo'tal xuruji: {patient.cough_attack}
            - Balg'am: {patient.phlegm}
            - Qanday balg'am: {patient.what_sputum}
            - Xansirash: {patient.shortness_of_breath}
            - Qanday xansirash: {patient.what_suffocation}
            - Og'riq: {patient.pain}
            - Harorat: {patient.temperature}
            - Qanday harorat: {patient.what_temperature}

            Nafas shovqinlari:
            - Turi: {', '.join(patient.breath_sound_types)}
            - Joylashuvi: {', '.join(patient.breath_sound_location)}
            """

            # Email yuborish
            # send_mail(
            #     subject='Yangi bemor maʼlumotlari qoʻshildi',
            #     message=email_content,
            #     from_email=settings.DEFAULT_FROM_EMAIL,
            #     recipient_list=['ilhamjonpersonal@gmail.com'],
            #     fail_silently=False,
            # )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
