#!/usr/bin/env python
"""
Georgia Institute of Technology - CS1301
Introduction to Object Oriented Programming using Python.
"""
__author__ = "YOUR NAME HERE"
""" YOUR COLLABORATION STATEMENT HERE """

class Student(object):
    """ docstring of a Student object.
    Student have the following properties:
    Attributes:
        name: A string representing the student's name. (i.e. George)
        gtid: A string representing  the student's GT id. (i.e. 1234)
        major: A Major object, representing the student's major. (i.e. <CS>)
        courses: A list representing the courses a student has taken or is currently  enrolled in. A new Student may or may not come with Courses already taken. (default to empty list)
    """

    def __init__(self):
        """Initialize a Student object whose name is *name*, gtid is *gtid*, major is *major*, courses is *courses* (default: empty)"""
        pass
    def get_total_credits(self):
        """ return the student's total amount of credits as an int"""
        pass

    def get_missing_credits(self):
        """ return the student's missing amount of credits to graduate as as an int (hint: Missing Credits = Required by Major - Total Credits) """
        pass

    def get_class_standing(self):
        """ return a string representation of the student's class standing. Freshman: 0-9 credits; Sophomore: 10-19; Junior: 20-29; Senior: 30-39"""
        pass

    def register(self, course):
        """ Add a course to the student's courses. No duplicate courses are allowed. If student is registered for X course with code "ZZ 1234", it should not be allowed to registered for Y course with code "ZZ 1234". In other words, what makes a course unique is its code. (hint: implement this in the Course class; major hint: override the __eq__ method in Course). Also, in our system a student can only register for courses that belong to his/her major."""
        pass

    def register_many(self, courses):
        """ register courses from a list of Course objects """
        pass

    def is_taking(self, course):
        """ Returns true if student is registered for a course """
        pass

    def drop(self, course):
        """ Drop a course if student is registered to it. Raise a DropNotEnrolledCourseException if student is not registered for that course. (TODO: implement this simple exception yourself, helpful toturial [http://www.programiz.com/python-programming/user-defined-exception]). Pass a message of the exception, exactly this: "Not enrolled in: {0}".format(course) """
        pass

    # ################## #
    # DON'T CHANGE THIS: #
    # ################## #
    def __str__(self):
        """ String representation of a Student object """
        return "({0}, {1}, {2})".format(self.name, self.gtid, self.get_class_standing())


class Course(object):
    """ docstring of a Course object.
    Course have the following properties:
    Attributes:
        code: A string representing the course code (i.e CS1301)
        major: A Major object, representing the major a Course belongs to. (i.e <CS>)
        credits: An integer representing the course's amount of credits (i.e 3)
        instructor: A  string representing the instructor of the course (i.e Jay Summet)
    """

    def __init__(self):
        """Initialize a Course object whose code is *code*, credits is *cresits*, and instructor is *instructor*."""
        pass

    def __eq__(self, other):
        pass

    # ################## #
    # DON'T CHANGE THIS: #
    # ################## #
    def __str__(self):
        """ String representation of a Course object """
        return "({0}, {1}, {2})".format(self.code, self.credits, self.instructor)
    def __repr__(self):
        return "<Course object: ({0}, {1}, {2})>".format(self.code, self.credits, self.instructor)

class Major(object):
    """docstring of a Major object.
    Major have the following properties:
        Attributes:
            name: A string representing the major name (i.e CS)
            required_credits: An int representing the amount of credits required to graduate (i.e 40)
    """
    def __init__(self):
        """Initialize an Instructor object whose name is *name* and required_credits are *required_credits*"""
        pass


# #################################################### #
# Implemtent your DropNotEnrolledCourseException below: #
# #################################################### #


if __name__ == '__main__':
    help(Major)