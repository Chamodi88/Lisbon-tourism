from django import forms
from .models import Attraction

# Obtaining number of places to visit and location from user
class QueryForm(forms.Form):

    keynumbers = forms.IntegerField(
        required=False,
        label='',
        widget=forms.NumberInput(        
            attrs={
                'class':'form-control',
                'placeholder':' '
            }))

    lat = forms.FloatField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_lat',
            }))

    lon = forms.FloatField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_lon',
            })) 

# Obtaining details of new attractions from user
class AttractionForm(forms.ModelForm):

    Name = forms.CharField(
        required=True, 
        label = "",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_Name',
                'placeholder': "Name",
                'label':''
            }))

    Address = forms.CharField(
        label='',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'id':'id_Address', 
                'rows':2,
                'placeholder':'Address',
                'label':''
            }))

    
    Opening_hours = forms.CharField(
        label = "", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_Opening_hours',
                'placeholder':'Opening hours',
                'label':''             
            }))
    
    Website = forms.CharField(
        label='',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'id':'id_Website', 
                'rows':2,
                'placeholder':'Website',
                'label':''
            }))
    
    Tickets = forms.CharField(
        label='',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'id':'id_Tickets', 
                'rows':2,
                'placeholder':'Tickets',
                'label':''
            }))

    Latitude = forms.CharField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_Latitude',
                'placeholder': "Latitude",
                'type':'text', 
            }))

    Longitude = forms.CharField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_Longitude',
                'placeholder': "Longitude",
                'type':'text', 
            })) 

    class Meta:
        model = Attraction
        fields = [
            'Name',
            'Address',
            'Opening_hours',
            'Website',
            'Tickets',
            'Latitude',
            'Longitude',
        ]