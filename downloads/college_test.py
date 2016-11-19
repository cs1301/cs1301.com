"""
Georgia Institute of Technology - CS1301
Basic unittest for student usage in HW9.
"""
import unittest
from college_answer_key import *

__author__  = "Daniel Barrundia"
__version__ = "1.0"
__email__   = "dbarrundia3@gatech.edu"
__date__    = "Fall 2016"

class CollegeTest(unittest.TestCase):
    def setUp(self):
        ##########
        # Majors #
        ##########
        self.my_major_1 = Major("Computer Science", 40)
        self.my_major_2 = Major("Industrial Engineer", 42)
        self.my_major_3 = Major("Business Administration", 39)

       ##############
       # CS Courses #
       ##############
        self.my_course_1 = Course(
                        "CS1301",   self.my_major_1, 3, "Melinda McDaniel")
        self.my_course_2 = Course(
                        "CS1331",   self.my_major_1, 3, "Chris Simpkins")
        self.my_course_3 = Course(
                        "CS4400",   self.my_major_1, 3, "Monica Sweat")
        self.my_course_4 = Course(
                        "CS2110",   self.my_major_1, 4, "Bill Leahy")
        self.my_course_5 = Course(
                        "CS2340",   self.my_major_1, 3, "Bob Waters")
        self.my_course_6 = Course(
                        "CS2200",   self.my_major_1, 4, "Tom Conte")
       ################
       # ISYE Courses #
       ################
        self.my_course_7 = Course(
                        "ISyE2028", self.my_major_2, 4, "Alisha Waller")
        self.my_course_8 = Course(
                        "ISyE2027", self.my_major_2, 3, "Sigrun Andradottir")
       #####################
       # Duplicate Courses #
       #####################
        self.my_course_X = Course(
                        "CS1301",   self.my_major_1, 3, "Mary Hudachek-Buswell")
        self.my_course_Y = Course(
                        "CS1301",   self.my_major_1, 3, "Jay Summet")

        #################
        # Some Students #
        #################
        self.my_student_1 = Student("Daniel", "903054641", self.my_major_1)
        self.my_student_2 = Student("Sara",   "903001239", self.my_major_2)
        self.my_student_3 = Student("Maria",  "903096344", self.my_major_1, [self.my_course_1,self.my_course_2])


        # TODO add more test cases yourself

    #####################
    # TESTS for Student #
    #####################
    def test_init_student_name(self):
        """A Student should be initialized with a name """
        self.assertEqual(self.my_student_1.name, "Daniel",  msg = "A student should be initialized with a name.")

    def test_init_student_id(self):
        """A Student should be initialized with a gtID """
        self.assertEqual(self.my_student_1.gtid, "903054641",  msg = "A student should be initialized with an id.")

    def test_init_empty_courses(self):
        """A Student should be initialized with no courses """
        self.assertEqual(self.my_student_2.courses, [], msg = "A student should have courses initialized as an empty dictionary.")

    def test_init_nonempty_courses(self):
        """A Student can be initialized with some courses """
        self.assertEqual(self.my_student_3.courses, [self.my_course_1,self.my_course_2])

    def test_get_total_credits_1(self):
        """A student with no course should have 0 credits """
        self.assertEquals(self.my_student_1.get_total_credits(), 0)

    def test_get_total_credits_2(self):
        """ A student with: 2x3credits = 6 total credits"""
        self.my_student_1.courses = [self.my_course_1,self.my_course_2]
        self.assertEqual(self.my_student_1.get_total_credits(), 6, msg= "A student 6 credits.")

    def test_get_total_credits_3(self):
        """ A student with: 4x3credits + 2x4credits = 20 total credits"""
        self.my_student_1.courses = [self.my_course_1,self.my_course_2,self.my_course_3,self.my_course_4,self.my_course_5, self.my_course_6]
        self.assertEquals(self.my_student_1.get_total_credits(),20)

    def test_get_total_credits_4(self):
        """ A student with 2 courses of 3 credits each, has 8 total credits"""
        self.my_student_1.courses = [self.my_course_4,self.my_course_6]
        self.assertEqual(self.my_student_1.get_total_credits(), 8)

    def test_get_missing_credits(self):
        """ A CS major with 0 credits, needs 40 more to graduate"""
        self.assertEqual(self.my_student_1.get_missing_credits(), 40)

    def test_get_missing_credits_2(self):
        """ A CS major with 20 credits, needs 20 more to graduate"""
        self.my_student_1.courses = [self.my_course_1,self.my_course_2,self.my_course_3,self.my_course_4,self.my_course_5, self.my_course_6]
        self.assertEqual(self.my_student_1.get_missing_credits(), 20)

    def test_class_standing_1(self):
        """ Student with 20 credits is a Junior """
        self.my_student_1.courses = [self.my_course_1,self.my_course_2,self.my_course_3,self.my_course_4,self.my_course_5, self.my_course_6]
        self.assertEqual(self.my_student_1.get_class_standing(), "Junior")

    def test_class_standing_2(self):
        """ Student with no courses is a Freshman """
        self.my_student_1.courses = []
        self.assertEqual(self.my_student_1.get_class_standing(), "Freshman", msg = "The get_missing_credits method isnt implemented correctly")

    def test_register_1(self):
        """ Register a single course """
        self.my_student_1.courses = []
        self.my_student_1.register(self.my_course_1)
        self.assertEqual(self.my_student_1.courses, [self.my_course_1])

    def test_register_2(self):
        """ Register more than one course """
        self.my_student_1.courses = []
        self.my_student_1.register(self.my_course_1)
        self.my_student_1.register(self.my_course_2)
        self.my_student_1.register(self.my_course_3)
        self.my_student_1.register(self.my_course_4)
        self.assertEqual(self.my_student_1.courses, [self.my_course_1,self.my_course_2,self.my_course_3,self.my_course_4])

    def test_register_3(self):
        """ No duplicates courses allowed in registration """
        self.my_student_1.courses = []
        self.my_student_1.register(self.my_course_1)
        self.my_student_1.register(self.my_course_X)
        self.assertEqual(self.my_student_1.courses, [self.my_course_1])

    def test_register_4(self):
        """ No courses of different major allowed in registration """
        self.my_student_1.courses = []
        self.my_student_1.register(self.my_course_1)
        self.my_student_1.register(self.my_course_7)
        self.my_student_1.register(self.my_course_8)
        self.assertEqual(self.my_student_1.courses, [self.my_course_1])

    def test_register_many(self):
        """ A Student can register many courses at once """
        self.my_student_1.courses = []
        self.my_student_1.register_many([self.my_course_1,self.my_course_2,self.my_course_3,self.my_course_4])
        self.assertEqual(self.my_student_1.courses, [self.my_course_1,self.my_course_2,self.my_course_3,self.my_course_4])

    def test_is_taking(self):
        """ is_taking method works """
        self.my_student_1.courses = [self.my_course_1]
        self.assertTrue(self.my_student_1.is_taking(self.my_course_1))

    def test_drop_1(self):
        """ drop a course successfully """
        self.my_student_1.courses = [self.my_course_1]
        self.my_student_1.drop(self.my_course_1)
        self.assertEquals(self.my_student_1.courses, [])

    def test_drop_2(self):
        """ DropNotEnrolledCourseException whn dropping a course not registered """
        self.my_student_1.courses = [self.my_course_1]
        self.assertRaises(DropNotEnrolledCourseException, lambda: self.my_student_1.drop(self.my_course_2))

    def test_drop_3(self):
        """ Check the message when catching a DropNotEnrolledCourseException. """
        self.my_student_1.courses = [self.my_course_1]
        try:
            self.my_student_1.drop(self.my_course_2)
        except DropNotEnrolledCourseException as e:
            self.assertEqual(str(e), "Not enrolled in: {0}".format(str(self.my_course_2)))
    #####################
    # TESTS for Course #
    #####################
    def test_init_course_code(self):
        """A Course should be initialized with a code """
        self.assertEqual(self.my_course_1.code, "CS1301")

    def test_init_course_credits(self):
        """A Course should be initialized with credits """
        self.assertEqual(self.my_course_1.credits, 3)

    def test_init_course_instructor(self):
        """A Course should be initialized with an instructor """
        self.assertEqual(self.my_course_1.instructor, "Melinda McDaniel")

    def test_course_eq(self):
        """A Course should be equal to another Course if they share the same code """
        self.assertEqual(self.my_course_1, self.my_course_X, msg="The __eq__ method in Course is not correctly implemented")

    def test_course_eq_2(self):
        """A Course should override the __eq__ method """
        self.assertTrue(self.my_course_1 in [self.my_course_X],msg="The __eq__ method in Course is not correctly implemented")

    ###################
    # TESTS for Major #
    ###################
    def test_init_major_name(self):
        """A Course should be initialized with a code """
        self.assertEqual(self.my_course_1.code, "CS1301")

    def test_init_course_credits(self):
        """A Course should be initialized with credits """
        self.assertEqual(self.my_course_1.credits, 3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CollegeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)