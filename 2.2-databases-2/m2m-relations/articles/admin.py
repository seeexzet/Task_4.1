from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            f = form.cleaned_data
            if f.get('is_main') == True:
                flag += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if flag > 1:
                raise ValidationError('Не должно быть более одного основного раздела')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['tag', 'is_main']


