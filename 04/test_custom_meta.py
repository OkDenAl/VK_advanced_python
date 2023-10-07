import unittest
from custom_meta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class TestMetaClassCustom(unittest.TestCase):

    def test_general_fields(self):
        inst = CustomClass()

        self.assertFalse(hasattr(inst, 'line'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'val'))
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)

        inst.custom_val = 12
        self.assertEqual(inst.custom_val, 12)

        self.assertFalse(hasattr(inst, 'custom___str__'))
        self.assertTrue(hasattr(inst, '__str__'))
        self.assertEqual(str(inst), 'Custom_by_metaclass')

    def test_additional_field(self):
        inst = CustomClass(100)
        self.assertEqual(inst.custom_val, 100)
        self.assertEqual(inst.custom_x, 50)
        inst.k = 120  # pylint: disable=W0201
        self.assertFalse(hasattr(inst, 'k'))
        self.assertTrue(hasattr(inst, 'custom_k'))
        self.assertEqual(inst.custom_k, 120)
        CustomClass.test = 'test'
        self.assertFalse(hasattr(CustomClass, 'test'))
        self.assertTrue(hasattr(CustomClass, 'custom_test'))
        self.assertEqual(inst.custom_test, 'test')

    def test_custom_class_fields(self):
        self.assertFalse(hasattr(CustomClass, 'x'))
        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertEqual(CustomClass.custom_x, 50)

        CustomClass.test = 'test'
        self.assertFalse(hasattr(CustomClass, 'test'))
        self.assertTrue(hasattr(CustomClass, 'custom_test'))
        self.assertEqual(CustomClass.custom_test, 'test')
