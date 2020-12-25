from django.forms import ModelForm, TextInput
from datetime import date
from .models import Events

class RecordForm(ModelForm):

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args, **kwargs)
        # by_user = Category.objects.filter(user=user) | Category.objects.filter(pk=39)
        # self.fields['category'].queryset = by_user

    class Meta:
        model = Events
        fields = ['date','start_time','end_time','event']
        widgets = {
            'date': TextInput(attrs={\
                        'id':'datepicker1',\
                        'value':date.today().strftime('%Y-%m-%d')\
                    }),
        }

class UserForm(ModelForm):
    class Meta:
        model = Events
        fields = ['user']

