from django.contrib import admin
from classroom import models

admin.site.register(models.Answer)
admin.site.register(models.Question)
admin.site.register(models.Quiz)
admin.site.register(models.Student)
admin.site.register(models.StudentAnswer)
admin.site.register(models.Subject)
admin.site.register(models.TakenQuiz)
admin.site.register(models.User)