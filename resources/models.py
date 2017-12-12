from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

# link languages
LANGUAGE_CHOICES = (("pt", 'Português'),("en", 'English'), ("es", 'Español'))

# limit the instances of a certain model
def validate_number_of_instances(obj, INSTANCE_NUMBER):
    model = obj.__class__
    if(model.objects.count() > INSTANCE_NUMBER):
        raise ValidationError("Can only have up to {} {} instances".format(INSTANCE_NUMBER, model.__name__)) 

# link tags
class Tag(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True, error_messages={'unique':"Esta tag já existe."}) 

    def __str__(self):
        return self.title

    def clean(self):
        validate_number_of_instances(self, 5)

# link instances
class Link(models.Model):
    title = models.CharField(max_length=100, blank=False)
    url = models.URLField(blank=False)
    language = models.CharField(max_length=10, blank=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("link_detail", kwargs={'pk': self.pk})


  
