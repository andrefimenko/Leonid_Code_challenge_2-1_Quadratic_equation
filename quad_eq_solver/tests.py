# from django.test import TestCase, Client
# from django.urls import reverse
# from . models import Equation
# import json
#
#
# class ResultTestCase(TestCase):
#     """Testing our views.result works properly."""
#     def setUp(self):
#         self.client = Client()
#         self.equation1 = Equation.objects.create(
#             a=1, b=4, c=3, root1=-1, root2=-3)
#         self.equation2 = Equation.objects.create(
#             a=1, b=2, c=1, root1=-1, root2=None)
#         self.equation3 = Equation.objects.create(
#             a=1, b=1, c=1, root1=None, root2=None)
#
#     def test_two_roots_case(self):
#         response = self.client.get(reverse("result"),
#                                     {'a': '1', 'b': '4', 'c': '3'})
#         self.assertEqual(response.status_code, 200)
#         json_response = json.loads(response.content)
#         self.assertTrue(json_response['success'])
#         self.assertEqual(json_response['message'], "Two roots.")
#         self.assertAlmostEqual(json_response['data']['root1'], -1.0)
#         self.assertAlmostEqual(json_response['data']['root2'], -3.0)
#
#     def test_one_root_case(self):
#         response = self.client.get(reverse('result'),
#                                    {'a': '1', 'b': '2', 'c': '1'})
#         self.assertEqual(response.status_code, 200)
#         json_response = json.loads(response.content)
#         self.assertTrue(json_response['success'])
#         self.assertEqual(json_response['message'], "One root.")
#         self.assertAlmostEqual(json_response['data']['root'], -1.0)
#
#     def test_no_roots(self):
#         response = self.client.get(reverse('result'),
#                                    {'a': '1', 'b': '2', 'c': '1'})
#         self.assertEqual(response.status_code, 200)
#         json_response = json.loads(response.content)
#         self.assertFalse(json_response['success'])
#         self.assertEqual(json_response['message'], 'No roots.')
#         self.assertIsNone(json_response['data'])
#
#     def test_invalid_http_method(self):
#         response = self.client.get(reverse('result'),
#                                    {'a': '1', 'b': '2', 'c': '1'})
#         self.assertEqual(response.status_code, 200)
#         json_response = json.loads(response.content)
#         self.assertFalse(json_response['success'])
#         self.assertEqual(json_response['message'], "Invalid HTTP method")
#         self.assertIsNone(json_response['data'])
#
#     def tearDown(self):
#         Equation.objects.all().delete()
#
#
#
#
# import math
# from django.test import TestCase, Client
# from django.http import JsonResponse
# from . models import Equation
# from . views import result
#
#
# class TestResultView(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#
#     def test_no_roots(self):
#         response = self.client.get('/result?a=2&b=3&c=4')
#         equation = Equation.objects.filter(a=2, b=3, c=4).first()
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content, b'"No roots for quadratic equation 2.0 * x^2 + 3.0 * x + 4.0 = 0"')
#         self.assertEqual(equation.root1, None)
#         self.assertEqual(equation.root2, None)
#
#     def test_one_root(self):
#         response = self.client.get('/result?a=1&b=-2&c=1')
#         equation = Equation.objects.filter(a=1, b=-2, c=1).first()
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content, b'"One root: 1.0 for quadratic equation 1.0 * x^2 + -2.0 * x + 1.0 = 0"')
#         self.assertEqual(equation.root1, 1.0)
#         self.assertEqual(equation.root2, None)
#
#     def test_two_roots(self):
#         response = self.client.get('/result?a=1&b=0&c=-4')
#         equation = Equation.objects.filter(a=1, b=0, c=-4).first()
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content, b'"Two roots: 2.0, -2.0 for quadratic equation 1.0 * x^2 + 0.0 * x + -4.0 = 0"')
#         self.assertEqual(equation.root1, 2.0)
#         self.assertEqual(equation.root2, -2.0)

    # def test_invalid_method(self):
    #     response = self.client.post('/result')
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.content, b'"Invalid method!"')

    # def test_missing_parameter(self):
    #     response = self.client.get('/result?a=1&b=2')
    #     equation = Equation.objects.filter(a=1, b=2).first()
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.content, b'"No roots for quadratic equation 1.0 * x^2 + 2.0 * x + None = 0"')
    #     self.assertEqual(equation.root1, None)
    #     self.assertEqual(equation.root2, None)

    # def test_value_error(self):
    #     response = self.client.get('/result?a=1&b=2&c=x')
    #     equation = Equation.objects.filter(a=1, b=2, c=0).first()
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.content, b'"No roots for quadratic equation 1.0 * x^2 + 2.0 * x + x = 0"')
    #     self.assertEqual(equation.root1, None)
    #     self.assertEqual(equation.root2, None)

from django.test import TestCase


class TestQuad_eq_solver(TestCase):

    def test_result(self):
        self.client.get()