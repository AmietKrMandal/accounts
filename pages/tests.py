from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_view_users_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")


class SignupPageTests(TestCase):
    username = "Admin"
    email = "amit33mandal@gmail.com"

    def test_signup_page_status_code(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)


    