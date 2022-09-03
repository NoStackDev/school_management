from django import forms 
from django.forms import Form
from accounts.models import ClassLevel, Session, Fee


def get_class_level_choices():
    #For Displaying Classes
    try:
        class_levels = ClassLevel.objects.all()
        class_level_list = []
        for class_level in class_levels:
            single_course = (class_level.id, class_level.class_level_name)
            class_level_list.append(single_course)

    except:
        class_level_list = []

    finally:
        return class_level_list


#def get_session_choices():
    #For Displaying Session
#    try:
#        sessions = Session.objects.all()
#        session_list = []
#        for session in sessions:
#            single_session = (session.id, str(session.session_start)+" to "+str(session.session_end))
#            session_list.append(single_session)
#            
#    except:
#        session_list = []
#    
#    finally:
#        return session_list



class DateInput(forms.DateInput):
    input_type = "date"

    


class AddStudentForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    other_names = forms.CharField(label="Other Names", required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, required=False, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Phone Number", required=False, max_length=13, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    gender_list = (
        (1,'Female'),
        (2,'Male'),
    )
    
    class_level_id = forms.ChoiceField(label="Class", choices=get_class_level_choices, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    dob=forms.DateField(label="Date of Birth", widget=forms.DateInput(format=('%Y-%m-%d'), attrs={"class":"form-control","type":"date"}), required=False)
    profile_pic = forms.ImageField(label="Profile Pic", required=False)



class EditStudentForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    other_names = forms.CharField(label="Other Names", required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, required=False, widget=forms.EmailInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Phone Number", required=False, max_length=13, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    gender_list = (
        (2,'Male'),
        (1,'Female')
    )
    
    class_level_id = forms.ChoiceField(label="Class", choices=get_class_level_choices, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    dob=forms.DateField(label="Date of Birth", widget=forms.DateInput(format=('%Y-%m-%d'), attrs={"class":"form-control","type":"date"}), required=False)
    profile_pic = forms.ImageField(label="Profile Pic", required=False)

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ('fee_name','fee_amount','course_id','term','custom_id')
        labels = {
            'fee_name':'Fee Name',
            'fee_amount':'Fee Amount',
            'course_id':'Select All Classes The Fee Description Applies To',
            'term': 'Select The Term(s) The Fee Description Applies To',
            'custom_id':'Custom ID'
        }
        widgets = {
            'fee_name':forms.TextInput(attrs={"class":"form-control", "placeholder":"Fee Name"}),
            'fee_amount':forms.NumberInput(attrs={"class":"form-control", "placeholder":"Fee Amount"}),
            'course_id':forms.CheckboxSelectMultiple(attrs={"placeholder":"Class(es)"}),
            'custom_id':forms.TextInput(attrs={"class":"form-control", "placeholder":"#xxxx"}),
        }