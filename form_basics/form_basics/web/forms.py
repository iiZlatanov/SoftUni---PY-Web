from django import forms

from form_basics.web.models import Employee


class DemoForm(forms.Form):
    firstname = forms.CharField(
        max_length=35,
        required=False,
        label='First Name:',
        initial="Doncho",
        help_text='Enter your first name.',
        #disabled=True,
    )

    lname = forms.CharField(
        max_length=35,
        required=False,
        label='Last Name:',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name.",
            }
        ),
    )

    email = forms.EmailField(
        required=False,
    )

    age = forms.IntegerField(
        required=False,
        step_size=3
    )

    description = forms.Textarea()

    INTERESTS = (
        (7, 'Gaming'),
        (6, 'Reading'),
        (3, 'Watching'),
        (11, 'Sport')
    )

    interests = forms.ChoiceField(
        choices=INTERESTS,
        required=False,
    )

    interests2 = forms.IntegerField(
        widget=forms.Select(choices=INTERESTS),
        required=False,
    )

    interests3 = forms.IntegerField(
        widget=forms.RadioSelect(choices=INTERESTS),
    )

    # interests4 = forms.IntegerField(
    #     widget=forms.CheckboxSelectMultiple(choices=INTERESTS),
    # )

    interests5 = forms.BooleanField()


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=Employee.MAX_FIRST_NAME_LENGTH,
        required=True,
    )

    last_name = forms.CharField(
        max_length=35,
        required=True,
    )
