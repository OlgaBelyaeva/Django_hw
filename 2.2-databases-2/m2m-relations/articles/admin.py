from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if [form.cleaned_data['is_main'] for form in self.forms if form.cleaned_data].count(True) == 1:
            return super().clean()  # вызываем базовый код переопределяемого метода
        else:
            raise ValidationError('Внимание! Нужно выбрать только один основной тэг!')

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['title']
    inlines = [ScopeInline, ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']

# @admin.register(Scope)
# class ScopeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'article', 'tag', 'is_main']
#     list_filter = []
