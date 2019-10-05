from django.test import TestCase
from classroom import forms
from classroom import models


def get_valid_data():
    form_data = {
        'username': 'vitas',
        'password1': '123456789',
        'password2': '123456789'
    }

    return form_data

class TeacherSignUpFormTest(TestCase):

    def test_if_user_is_a_teacher(self):
        """
        Testing if the user created by the teacher 
        registration form is being set up as a teacher
        """

        form_data = get_valid_data()
        form = forms.TeacherSignUpForm(data=form_data)
        user = form.save()
        self.assertTrue(user.is_teacher)
    

class StudentSignUpFormTest(TestCase):

    def test_if_user_is_a_student(self):
        """
        Testing if the user created by the student 
        registration form is being set up as a student
        """

        form_data = get_valid_data()
        subject_id = models.Subject.objects.first().id
        form_data['interests'] = [subject_id]
        
        form = forms.StudentSignUpForm(data=form_data)

        user = form.save()
        self.assertTrue(user.is_student)


    def test_if_user_subjects_are_being_saved(self):
        """
        Testing if the subject passed in the form is 
        being saved in the student's interests
        """
        
        subject = models.Subject.objects.create(
            name='Physics',
        )

        form_data = get_valid_data()
        form_data['interests'] = [subject.id]

        form = forms.StudentSignUpForm(data=form_data)
        user = form.save()

        student = models.Student.objects.get(user=user)
        self.assertEqual(len(student.interests.all()), 1)
        
        self.assertEqual(
            student.interests.first(), 
            subject
        )