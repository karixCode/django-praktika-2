from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import User, Category, Request

class RequestAdminForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['status', 'comment', 'final_image']

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        comment = cleaned_data.get("comment")
        final_image = cleaned_data.get("final_image")

        if status == 'in_progress' and not comment:
            raise ValidationError("При переводе заявки в статус 'Принято в работу' необходимо добавить комментарий.")
        if status == 'completed' and not final_image:
            raise ValidationError("При переводе заявки в статус 'Выполнено' необходимо прикрепить изображение.")

        return cleaned_data

class RequestAdmin(admin.ModelAdmin):
    form = RequestAdminForm
    list_display = ['title', 'status', 'timestamp', 'user']
    readonly_fields = ['title', 'description', 'category', 'timestamp', 'user', 'design_image']

    def get_readonly_fields(self, request, obj=None):
        readonly = super().get_readonly_fields(request, obj)
        if obj:
            if obj.status == 'new':
                return readonly
            if obj.status == 'in_progress':
                return readonly + ['comment']
            if obj.status == 'completed':
                return readonly + ['comment', 'final_image', 'status']
            print(obj)
        return readonly

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Request, RequestAdmin)
