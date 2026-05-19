from django.contrib import admin

from .models import (
    Scoring,
    ScoringRule
)

admin.site.register(Scoring)
admin.site.register(ScoringRule)