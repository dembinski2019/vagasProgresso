from django.test import TestCase

class WebSiteIndexTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_get_index(self):
        """GET / must return status code 200 """
        self.assertEqual(self.resp.status_code, 200)

    def test_template_index(self):
        """Must use template website/index.html"""
        self.assertTemplateUsed(self.resp, "website/index.html")

class WebSiteCandidateTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/candidato')

    def test_get_candidate(self):
        """GET /candidato must return status code 200 """
        self.assertEqual(self.resp.status_code, 200)

    def test_template_candidate(self):
        """Must use template website/candidate_home.html"""
        self.assertTemplateUsed(self.resp, "website/candidate_home.html")

class WebSiteCompanyTest(TestCase):
    
    def setUp(self):
        self.resp = self.client.get('/empresas')

    def test_get_company(self):
        """GET /empresas must return status code 200 """
        self.assertEqual(self.resp.status_code, 200)

    def test_template_company(self):
        """Must use template website/company_home.html"""
        self.assertTemplateUsed(self.resp, "website/company_home.html")