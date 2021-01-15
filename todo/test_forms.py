from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        """
        make sure that the name field
        is required in order to create an item.
        """

        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """
        Ensure done field is not required
        """

        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        only fields that are displayed in
        the form are the name and done fields.
        """

        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
