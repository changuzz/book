import books as books
from django import forms
from book.models import Books
# class BookForm(forms.Form):
#     book_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     copies = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data.get("price")
#         copies=cleaned_data.get("copies")
#         if int(price)<0:
#             msg="invalid price"
#             self.add_error("price",msg)
#         if int(copies) < 0:
#             msg = "invalid copies"
#             self.add_error("copies", msg)

#          model form

class BookForm(forms.ModelForm):
     class Meta:
         model=Books
         fields="__all__"
         widgets={
             "book_name": forms.TextInput(attrs={"class":"form_control"}),
             "author": forms.TextInput(attrs={"class":"form_control"}),
             "amount":forms.NumberInput(attrs={"class":"form_control"}),
             "copies":forms.NumberInput(attrs={"class":"form_control"}),
             "image":forms.FileInput(attrs={"class":"form_control"}),

         }