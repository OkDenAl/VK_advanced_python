class ProgrammingLanguageDescriptor:
    languages = ("C++", "Python", "Golang", "Rust", "Java", "Javascript")

    def __set_name__(self, owner, name):
        self.name = f"prog_lang_descr_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if obj is None:
            return None
        if not isinstance(val, str):
            raise TypeError('Язык программирования должен быть строкой')
        if val not in self.languages:
            raise ValueError(f'Язык программирования должен быть в '
                             f'{self.languages}')
        return setattr(obj, self.name, val)


class WorkExperienceDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"work_exp_descr_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        print(obj,val)
        if obj is None:
            print("here")
            return None
        if not isinstance(val, float):
            raise TypeError('Опыт работы должен быть'
                            ' числом с плавающей точкой в годах')
        if val < 0.0:
            raise ValueError('Опыт работы должен быть положительным числом')
        return setattr(obj, self.name, val)


class SalaryDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"salary_descr_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if obj is None:
            return None
        if not isinstance(val, int):
            raise TypeError('Зарплата должна быть целым числом в рублях')
        if val < 0.0:
            raise ValueError('Зарплата должна быть положительным числом')
        return setattr(obj, self.name, val)


class Programmer:
    program_language = ProgrammingLanguageDescriptor()
    work_experience = WorkExperienceDescriptor()
    salary = SalaryDescriptor()

    def __init__(self, prog_language, work_experience, salary):
        self.program_language = prog_language
        self.work_experience = work_experience
        self.salary = salary

    def __str__(self):
        return f"Программист, пишущий на {self.program_language}," \
               f" с опытом работы {self.work_experience} год(а)" \
               f" и зарплатой в {self.salary} рублей"
