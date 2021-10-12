from django.test import TestCase
from .models import Category


# Create your tests here.
class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """Test Category model data insertion/types/fields attributes"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry_name(self):
        """Test catey model defoult name"""
        data = self.data1
        self.assertEqual(str(data), 'django')
