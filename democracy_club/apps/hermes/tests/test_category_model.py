from . import HermesTestCase
from hermes import models


class CategoryTestCase(HermesTestCase):
    def test_is_root(self):
        """A Category should know if it is the root category"""
        expected = True
        self.assertEqual(expected, self.root_category.is_root)

        expected = False
        self.assertEqual(expected, self.second_category.is_root)

        expected = False
        self.assertEqual(expected, self.third_category.is_root)

    def test_hierarchy(self):
        """A Category should know it's hierarchy"""
        expected = [
            self.root_category,
        ]
        self.assertEqual(expected, self.root_category.hierarchy())

        expected = [
            self.root_category,
            self.second_category,
        ]
        self.assertEqual(expected, self.second_category.hierarchy())

        expected = [
            self.root_category,
            self.second_category,
            self.third_category,
        ]
        self.assertEqual(expected, self.third_category.hierarchy())

    def test_parents(self):
        """A Category should know its parents"""
        expected = []
        self.assertEqual(expected, self.root_category.parents())

        expected = [
            self.root_category,
        ]
        self.assertEqual(expected, self.second_category.parents())

        expected = [
            self.root_category,
            self.second_category,
        ]
        self.assertEqual(expected, self.third_category.parents())

    def test_root_parent(self):
        """A Category should know its top-most parent"""
        expected = self.root_category
        self.assertEqual(expected, self.root_category.root_parent())
        self.assertEqual(expected, self.second_category.root_parent())
        self.assertEqual(expected, self.third_category.root_parent())

        expected = self.another_category
        self.assertEqual(expected, self.another_category.root_parent())

    def test_generate_slug(self):
        """A Category should know how to generate its slug"""
        expected = "programming"
        self.assertEqual(expected, self.root_category._generate_slug())

        expected = "programming/python"
        self.assertEqual(expected, self.second_category._generate_slug())

        expected = "programming/python/django"
        self.assertEqual(expected, self.third_category._generate_slug())

    def test_unicode(self):
        """A Category should have a unicode representation"""
        expected = "Programming"
        self.assertEqual(expected, self.root_category.__unicode__())

        expected = "Programming > Python"
        self.assertEqual(expected, self.second_category.__unicode__())

        expected = "Programming > Python > Django"
        self.assertEqual(expected, self.third_category.__unicode__())

    def test_save(self):
        """A Category should update its slug on save"""
        self.third_category.slug = "Banana Slug"
        self.third_category.save()

        expected = "programming/python/django"
        self.assertEqual(expected, self.third_category.slug)


class CategoryManagerTestCase(HermesTestCase):
    def test_children_of(self):
        """The Category Manager should know the children of a Category"""
        expected = [
            self.second_category,
            self.third_category,
        ]
        self.assertEqual(
            expected, models.Category.objects.children_of(self.root_category)
        )

        expected = [
            self.third_category,
        ]
        self.assertEqual(
            expected, models.Category.objects.children_of(self.second_category)
        )

    def test_children_of_leaf(self):
        """The Category Manager should know that a leaf Category has no children"""
        expected = []
        self.assertEqual(
            expected, models.Category.objects.children_of(self.third_category)
        )
