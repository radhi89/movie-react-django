from django.db import models
from django_extensions.db import models as dem
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
from rest_framework.compat import MinValueValidator, MaxValueValidator


class Movie(dem.TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    banner_image = models.ImageField(help_text='Banner image for Movie', upload_to='image/')
    genre = models.CharField(max_length=20, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    director = models.CharField(max_length=200,null=True, blank=True)
    stars = models.TextField(null=True, blank=True)


    class Meta:
        ordering = ('-release_date',)

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Enquiry(dem.TimeStampedModel):
    name = models.CharField('Name', max_length=150, null=False, blank=False)
    phone = PhoneNumberField('Phone Number', blank=False, null=False)
    email = models.EmailField('Email', null=True, blank=True)
    content = models.CharField('Content', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'ContactForm'
        verbose_name_plural = 'ContactForms'
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name} : {self.content}'

    def __repr__(self):
        return f'ContactForm({self.name}:{self.content})'


class Review(dem.TimeStampedModel):
    movie = models.ForeignKey('Movie', verbose_name='movie', related_name="review", null=True, blank=True,
                              on_delete=models.SET_NULL)
    review = models.FloatField(help_text='review under 5',validators=[MinValueValidator(0.01), MaxValueValidator(5.00)],
                               null=True, blank=True)

    def __str__(self):
        return 'Movie : {0} Review: {1}'.format(self.movie.title, self.review)
