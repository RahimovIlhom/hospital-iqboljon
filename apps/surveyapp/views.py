from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import threading

from core.settings import env
from .models import PatientData
from .serializers import PatientDataSerializer

class EmailThread(threading.Thread):
    """
    Email yuborishni backgroundda bajaradigan thread.
    """
    def __init__(self, subject, message, from_email, recipient_list):
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.recipient_list = recipient_list
        super().__init__()

    def run(self):
        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=self.from_email,
            recipient_list=self.recipient_list,
            fail_silently=False,
        )

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
            - Bemor (FISh): {patient.fullname}
            - Yoshi: {patient.age}

            Xavf omillari:
            - Turar joy, ish sharoiti: {patient.housing_or_working_conditions}
            - Chekish: {patient.smoking}
            - Sovuq qotish: {patient.cold_exposure}
            - Allergenlar bilan kontakt: {patient.contact_with_allergens}
            - Irsiy moyillik: {patient.hereditary_predisposition}

            Anamnez:
            - Kasallik boshlanishi: {patient.onset_of_disease}
            - Kasallik kechishi: {patient.course_of_disease}
            - Xurujli kechishi: {patient.attack_course}
            - Davo samaradorlik: {patient.treatment_effectiveness}

            Shikoyatlar:
            - Yo'tal: {patient.cough}, {patient.cough_attack}
            - Balg'am: {patient.phlegm}, {patient.what_sputum}
            - Xansirash: {patient.shortness_of_breath}, {patient.what_suffocation}
            - Og'riq: {patient.pain}
            - Harorat: {patient.temperature}, {patient.what_temperature}

            Nafas shovqinlari:
            - Turi: {', '.join(patient.breath_sound_types)}
            - Localization: {', '.join(patient.breath_sound_location)}
            """

            # Emailni backgroundda yuborish
            email_thread = EmailThread(
                subject='Yangi bemor maʼlumotlari qoʻshildi',
                message=email_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=env.list('RECIPIENT_LIST', default=[]),
            )
            email_thread.start()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
