from django.contrib import admin

# Register your models here.
from .models import Team
from .models import Player
from .models import Submission

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Submission)