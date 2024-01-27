from django import forms

class YourForm(forms.Form):
    choose = forms.ChoiceField(choices=[
        ('Respiratory Physiology', 'Respiratory Physiology'),
        ('Embryology', 'Embryology'),
        ('GIT Physiology', 'GIT Physiology'),
        ('Cardiovascular Physiology', 'Cardiovascular Physiology'),
        ('Neurophysiology', 'Neurophysiology'),
        ('Renal Physiology', 'Renal Physiology'),
        ('Introductory Physiology', 'Introductory Physiology'),
        ('Blood Physiology', 'Blood Physiology'),
        ('Endocrinology', 'Endocrinology'),
        ('Reproductive Physiology', 'Reproductive Physiology'),],
        label='', 
        )