from django import forms
from django.contrib import admin

from mainapp.models import Category, VideoItem


class VideoItemForm(forms.ModelForm):
    Description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40})
    )

    class Meta:
        model = VideoItem
        fields = '__all__'

class VideoItemAdmin(admin.ModelAdmin):
    form = VideoItemForm
    list_display = ('Title', 'InActive')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'OrderId', 'InActive')


admin.site.register(Category, CategoryAdmin)
admin.site.register(VideoItem, VideoItemAdmin)
