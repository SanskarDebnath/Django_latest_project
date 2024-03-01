from django import forms
from django.forms import ModelForm

from . models import ProductCategory

class ProductCategoryForm (ModelForm):
    class Meta: #meta class will connect the form to the model ; meta class name can't be change
        model = ProductCategory
        fields = "__all__" #retrieve all the field to build the form
        #other scenerio (selective forms fields)
        #fields = ('p_cat_name', 'p_cat_image')

        widgets = {
            'p_cat_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the catagory name'}),
            'p_cat_desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the catagory description here'}),
            
        }
        labels = {
            'p_cat_name':"Enter the catagory name", 'p_cat_desc':"Enter the catagory description", 'p_cat_image':"upload the image"
        }