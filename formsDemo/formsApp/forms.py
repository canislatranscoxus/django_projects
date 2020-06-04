from django         import forms
from django.core    import validators


class UserRegistrationForm( forms.Form ):

    GENDER = [ ( 'male', 'MALE' ), ( 'female', 'FEMALE' ) ]

    firstName = forms.CharField(
        widget      = forms.Textarea,
        validator   = [ validators.MinLengthValidator( 2), validators.MaxLengthValidator( 45 )  ]
    )


    lastName  = forms.CharField( max_length = 45 )
    salary    = forms.FloatField()
    email     = forms.EmailField ( max_length = 45 )
    pic       = forms.CharField( max_length = 50, required = False )

    gender    = forms.CharField( widget = forms.Select( choices = GENDER ) )
    password  = forms.CharField( widget = forms.PasswordInput )
    ssn       = forms.IntegerField()


    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data[ 'firstName' ]
        if len( inputFirstName ) < 2:
            raise forms.ValidationError( 'The first name is too short' )



    """
    def clean_firstName(self):
        inputFirstName = self.cleaned_data[ 'firstName' ]
        if len( inputFirstName ) < 2:
            raise forms.ValidationError( 'The first name is too short' )
        return inputFirstName

    def clean_email(self):
        inputEmail = self.cleaned_data[ 'email' ]
        if inputEmail.find( '@' ) == -1:
            raise forms.ValidationError( 'The email should contain @' )
        return inputEmail
    """





