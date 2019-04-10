from django.contrib import admin

'''
Register Profile, Program, and ResourceLink
in the Admin Site
'''
from .models import Course, Profile, Program, Taxonomy

admin.site.register(Profile)
admin.site.register(Program)
admin.site.register(Taxonomy)

'''
Register all objective models 
in the Admin Site using django import-export
'''
# This enables django-import-export in the admin app
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# SafetyObjective
from .models import SafetyObjective
class SafetyObjectiveResource(resources.ModelResource):
    class Meta:
        model = SafetyObjective

@admin.register(SafetyObjective)
class SafetyObjectiveAdmin(ImportExportModelAdmin):
    pass

# TechnicalObjective
from .models import TechnicalObjective
class TechnicalObjectiveResource(resources.ModelResource):
    class Meta:
        model = TechnicalObjective

@admin.register(TechnicalObjective)
class TechnicalObjectiveAdmin(ImportExportModelAdmin):
    pass

# EmployabilityObjective
from .models import EmployabilityObjective
class EmployabilityObjectiveResource(resources.ModelResource):
    class Meta:
        model = EmployabilityObjective

@admin.register(EmployabilityObjective)
class EmployabilityObjectiveAdmin(ImportExportModelAdmin):
    pass

# ManagementObjective
from .models import ManagementObjective
class ManagementObjectiveResource(resources.ModelResource):
    class Meta:
        model = ManagementObjective

@admin.register(ManagementObjective)
class ManagementObjectiveAdmin(ImportExportModelAdmin):
    pass

# TechnologyObjective
from .models import TechnologyObjective
class TechnologyObjectiveResource(resources.ModelResource):
    class Meta:
        model = TechnologyObjective

@admin.register(TechnologyObjective)
class TechnologyObjectiveAdmin(ImportExportModelAdmin):
    pass


'''
Register LessonPlan and Course in Admin site 
using Summernote for the text fields
'''
# Summernote WYSIWYG in admin
from django_summernote.admin import SummernoteModelAdmin

# LessonPlan
from .models import LessonPlan
# class LessonPlanAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     pass

admin.site.register(LessonPlan)#, LessonPlanAdmin)

# Course
from .models import Course
class CourseAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    pass

admin.site.register(Course, CourseAdmin)
