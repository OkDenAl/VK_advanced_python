import unittest
from descriptors import Programmer


class TestDescriptor(unittest.TestCase):
    def test_correct_fields(self):
        Programmer("C++", 1.0, 100000)
        Programmer("Python", 2.0, 200000)

    def test_incorrect_prog_language(self):
        with self.assertRaises(TypeError) as err:
            Programmer(100, 1.0, 100000)
        self.assertEqual("Язык программирования должен быть строкой", str(err.exception))
        with self.assertRaises(ValueError) as err:
            Programmer("string", 1.0, 100000)
        self.assertEqual("Язык программирования должен быть в ('C++',"
                         " 'Python', 'Golang', 'Rust', 'Java', 'Javascript')", str(err.exception))

    def test_incorrect_salary(self):
        with self.assertRaises(TypeError) as err:
            Programmer("C++", 1.0, 100000.4)
        self.assertEqual("Зарплата должна быть целым числом в рублях", str(err.exception))
        with self.assertRaises(ValueError) as err:
            Programmer("C++", 1.0, -100000)
        self.assertEqual("Зарплата должна быть положительным числом", str(err.exception))

    def test_incorrect_work_experience(self):
        with self.assertRaises(TypeError) as err:
            Programmer("C++", 1, 100000)
        self.assertEqual("Опыт работы должен быть числом с плавающей точкой в годах", str(err.exception))
        with self.assertRaises(ValueError) as err:
            Programmer("C++", -1.0, 100000)
        self.assertEqual("Опыт работы должен быть положительным числом", str(err.exception))

    def test_str(self):
        programmer = Programmer("Python", 2.0, 200000)
        self.assertEqual(str(programmer), "Программист, пишущий на Python,"
                                          " с опытом работы 2.0 год(а) и зарплатой в 200000 рублей")

    def test_get_with_correct_field(self):
        programmer = Programmer("Python", 2.0, 200000)

        self.assertEqual(programmer.salary, 200000)
        self.assertEqual(programmer.work_experience, 2.0)
        self.assertEqual(programmer.program_language, "Python")

    def test_change_prog_language_field(self):
        programmer = Programmer("Python", 2.0, 200000)
        self.assertEqual(programmer.program_language, "Python")

        programmer.program_language = "Golang"
        self.assertEqual(programmer.program_language, "Golang")

        with self.assertRaises(TypeError) as err:
            programmer.program_language = 100
        self.assertEqual("Язык программирования должен быть строкой", str(err.exception))
        with self.assertRaises(ValueError) as err:
            programmer.program_language = "lang"
        self.assertEqual("Язык программирования должен быть в ('C++',"
                         " 'Python', 'Golang', 'Rust', 'Java', 'Javascript')", str(err.exception))

    def test_change_salary_field(self):
        programmer = Programmer("Python", 2.0, 200000)
        self.assertEqual(programmer.salary, 200000)

        programmer.salary = 300000
        self.assertEqual(programmer.salary, 300000)

        with self.assertRaises(TypeError) as err:
            programmer.salary = 111111.1
        self.assertEqual("Зарплата должна быть целым числом в рублях", str(err.exception))
        with self.assertRaises(ValueError) as err:
            programmer.salary = -300000
        self.assertEqual("Зарплата должна быть положительным числом", str(err.exception))

    def test_change_work_experience_field(self):
        programmer = Programmer("Python", 2.0, 200000)
        self.assertEqual(programmer.work_experience, 2.0)

        programmer.work_experience = 2.5
        self.assertEqual(programmer.work_experience, 2.5)

        with self.assertRaises(TypeError) as err:
            programmer.work_experience = 1
        self.assertEqual("Опыт работы должен быть числом с плавающей точкой в годах", str(err.exception))
        with self.assertRaises(ValueError) as err:
            programmer.work_experience = -1.0
        self.assertEqual("Опыт работы должен быть положительным числом", str(err.exception))