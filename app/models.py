from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

'''
Programs or Department Titles e.g. Carpentry
'''
class Program(models.Model):
    title = models.CharField(max_length=200, help_text='Enter the title of your program (e.g. Carpentry)')
    description = models.TextField(max_length=5000, null=True)
    
    def __str__(self):
        return self.title

'''
Extends User to create Teacher Profile
Each User Profile relates to a Program
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, null=True)
    bio = models.TextField(max_length=500, blank=True)
    program = models.ForeignKey('Program', on_delete=models.SET_NULL, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def __str__(self):
        return self.user

'''
Each Program has a framework.
Strand 2 is the program-specific technical objective
Strands 1, 4, 5, 6 are global for 'All' programs.
'''
# Display objectives (many to many) as checkboxes in the Admin
from django.forms import CheckboxSelectMultiple
from django.contrib import admin
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Taxonomy(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
# Strand 1: Safety and Health Knowledge and Skills
class SafetyObjective(models.Model):
    strand = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    
    classification = models.ForeignKey('Taxonomy', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['strand']
   
    def __str__(self):
        return f'{self.strand} {self.description}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this."""
        return reverse('safety-objective-detail', args=[str(self.id)])
        
# Strand 2   
class TechnicalObjective(models.Model):
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    strand = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    
    classification = models.ForeignKey('Taxonomy', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['strand']
   
    def __str__(self):
        return f'{self.strand} {self.description}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this."""
        return reverse('technical-objective-detail', args=[str(self.id)])
        
# Strand 4: Employability and Career Readiness
class EmployabilityObjective(models.Model):
    strand = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    
    classification = models.ForeignKey('Taxonomy', on_delete=models.SET_NULL, null=True)

    
    class Meta:
        ordering = ['strand']
   
    def __str__(self):
        return f'{self.strand} {self.description}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this."""
        return reverse('employability-objective-detail', args=[str(self.id)])

# Strand 5: Management and Entrepreneurship Knowledge and Skills
class ManagementObjective(models.Model):
    strand = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    
    classification = models.ForeignKey('Taxonomy', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['strand']
   
    def __str__(self):
        return f'{self.strand} {self.description}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this."""
        return reverse('management-objective-detail', args=[str(self.id)])

# Strand 6: Technology Literacy Knowledge and Skills
class TechnologyObjective(models.Model):
    strand = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    
    classification = models.ForeignKey('Taxonomy', on_delete=models.SET_NULL, null=True)

    
    class Meta:
        ordering = ['strand']
   
    def __str__(self):
        return f'{self.strand} {self.description}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this."""
        return reverse('technology-objective-detail', args=[str(self.id)])
        

'''
Lesson Plans are linked to courses
'''
class LessonPlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    content_objectives = models.TextField(max_length=5000, null=True, blank=True)
    language_objectives = models.TextField(max_length=5000, null=True, blank=True)
    sequence = models.CharField(max_length=200, null=True, blank=True, help_text="When viewing a course, Lesson Plans will be sorted by this value")
    
    # framework objectives
    safety_objectives = models.ManyToManyField(SafetyObjective, blank=True)
    technical_objectives = models.ManyToManyField(TechnicalObjective, blank=True)
    employability_objectives = models.ManyToManyField(EmployabilityObjective, blank=True)
    management_objectives = models.ManyToManyField(ManagementObjective, blank=True)
    technology_objectives = models.ManyToManyField(TechnologyObjective, blank=True)
    
    # Integrate Summerforms so this field may render with WYSIWYG
    lesson_outline = models.TextField(max_length=5000, null=True, blank=True)
    
    # Resource Links: Going to use Summernote toolbar with link only setting.
    # resource_links = models.ManyToManyField(ResourceLink, blank=True)
    resources = models.TextField(max_length=5000, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} ({self.course.title})'
        
    def get_absolute_url(self):
        """Returns the url to access a detail record for this."""
        return reverse('lesson-plan-detail', args=[str(self.id)])

'''
Courses are specific classes taught
within a program. e.g. Intro to Woodworking, or Freshmen Shop
'''
class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey('Program', on_delete=models.SET_NULL, null=True)
    
    title = models.CharField(max_length=200, help_text='Enter the name of your course (e.g. Intro to Woodworking)')
    prerequisite = models.CharField(max_length=200, null=True, blank=True, help_text='List any prerequisite courses required.')
    version = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=5000, help_text='Enter a your course description', null=True, blank=True)
    
    objectives = models.TextField(max_length=5000, null=True, blank=True)
    resources = models.TextField(max_length=5000, null=True, blank=True)
    grading_policy = models.TextField(max_length=5000, null=True, blank=True)
    assessment_practices = models.TextField(max_length=5000, null=True, blank=True)
    projects = models.TextField(max_length=5000, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} ({self.program.title})'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this."""
        return reverse('course-detail', args=[str(self.id)])