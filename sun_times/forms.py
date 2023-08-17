from django import forms


class CoordinatesForm(forms.Form):
    lat = forms.FloatField(label="latitude", min_value=-90, max_value=90)
    lng = forms.FloatField(label="longitude", min_value=-90, max_value=90)
