from django.test import TestCase
from .models import Employtment
from accounts.models import User

class EmploytmentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="company2", password="Dembinski123")

    def test_new_employtment_ok(self):
        for i in range(3):
                self.new_employtment = Employtment.objects.create(
                    employtment_name=f"Motorista{i}",
                    requirements="Cnh C, precisa conhecer bem a cidade",
                    description="Fazer entregas na cidade, horario 07:00 as 18:00",
                    salary='1280',
                    jobs_vacancy="3",
                    company=self.user,
                    )
        self.count = Employtment.objects.count()
        self.assertEqual(self.count, 3)

    def tearDown(self):
        Employtment.objects.all().delete()

        