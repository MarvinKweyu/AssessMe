from django.forms import inlineformset_factory
from django.test import TestCase
from classroom import forms
from classroom import models
from django.core.exceptions import ValidationError

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
    
class BaseAnswerInlineFormSetTest(TestCase):

    def test_if_there_is_at_least_one_correct_answer(self):

        user = models.User.objects.create(
            is_teacher=True, 
            username='Teacher Vitas'
        )

        subject = models.Subject.objects.create(
            name = 'Vitas Career'
        )

        quiz = models.Quiz.objects.create(
            owner = user,
            name = "Quiz about Vitas",
            subject = subject,
        )

        post_request_dict = {}

        question_text = 'What is the home country of vitas?'
        post_request_dict['text'] = question_text

        question = models.Question.objects.create(
            quiz = quiz,
            text = question_text 
        )

        post_request_dict['answers-0-question']=question.id
        post_request_dict['answers-0-text'] = 'Russia'
        post_request_dict['answers-0-is_correct'] = False

        post_request_dict['answers-0-question']=question.id
        post_request_dict['answers-0-text'] = 'Lithuania'
        post_request_dict['answers-0-is_correct'] = False

        post_request_dict['answers-0-question']=question.id
        post_request_dict['answers-0-text'] = 'Latvia'
        post_request_dict['answers-0-is_correct'] = False
        
        post_request_dict['answers-TOTAL_FORMS'] = 5
        post_request_dict['answers-INITIAL_FORMS'] = 0
        post_request_dict['answers-MIN_NUM_FORMS'] = 2
        post_request_dict['answers-MAX_NUM_FORMS'] = 10
        
        AnswerFormSet = inlineformset_factory(
            models.Question,
            models.Answer,
            formset = forms.BaseAnswerInlineFormSet,
            fields=('text', 'is_correct'),
        )

        formset = AnswerFormSet(
            post_request_dict,
            instance = question,
        )

        with self.assertRaises(ValidationError):
            formset.clean()