from django.db.models import Model, CharField, IntegerField, TextChoices


class Contact(Model):
    class Course(TextChoices):
        HTML = 'Html', 'html'
        CSS = 'Css', 'css'
        JAVASCRIPT = 'Javascript', 'javascript'
        PYTHON = 'Python', 'python'
        CISCO = 'Cisco', 'cisco'
    name = CharField(max_length=255, null=True, blank=True)
    email = CharField(max_length=255, null=True, blank=True)
    number = IntegerField()
    course = CharField(max_length=25, choices=Course.choices, default=Course.HTML)
    gender = CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return self.name



