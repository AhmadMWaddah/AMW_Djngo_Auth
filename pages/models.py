import pathlib

from django.db import models
from django.urls import reverse


def default_image():
    return 'default/default.png'


def upload_branch_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'branches/{self.slug}{ext}'


def upload_store_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'store/{self.slug}{ext}'


def upload_country_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'flags/{self.name}{ext}'


def upload_distributor_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'distributors/{self.name}{ext}'


def upload_project_main_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'project/{self.name} - {self.area}{ext}'


def upload_project_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'project/{self.project.name} - {self.project.area}{ext}'


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return f'{self.question}'


class Term(models.Model):
    name = models.CharField(max_length=255)
    condition = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return f'{self.name}'


class SalesOffice(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    email = models.EmailField(unique=True)
    website = models.URLField()
    mobile = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_branch_image, default=default_image)

    class Meta:
        ordering = ['region', 'country', 'state', 'city']

    def get_absolute_url(self):
        return reverse('sales_office', args={'slug': self.slug})

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to=upload_country_image, default=default_image)

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class LocalStore(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_store_image, default=default_image)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('our_stores', args={'slug': self.slug})

    def __str__(self):
        return f'{self.name}'


class Distributor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_distributor_image, default=default_image)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    main_image = models.ImageField(default=default_image, upload_to=upload_project_main_image)

    def images(self):
        images = Image.objects.filter(project=self)
        return images

    class Meta:
        ordering = ['area', '-year', 'name']

    def get_absolute_url(self):
        return reverse('project_details', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.name} - {self.area}'


class Image(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    image = models.ImageField(default=default_image, upload_to=upload_project_image)

    def __str__(self):
        return f'{self.project}'
