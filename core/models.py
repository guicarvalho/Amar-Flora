# coding: utf-8

from django.conf import settings

from django.core.validators import MinValueValidator

from django.db import models

from django.utils.translation import ugettext_lazy as _


class Partner(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    phone = models.CharField(_('Phone'), max_length=11, blank=True, null=True)
    email = models.EmailField(_('E-mail'))
    benefit = models.CharField(_('Benefit'), max_length=100)
    site = models.URLField(_('Site'))

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')

    def __str__(self):
        return self.name


class Associate(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    rg = models.CharField(_('RG'), max_length=10)
    cpf = models.CharField(_('CPF'), max_length=11)
    birthday = models.DateField(_('Birthday'))
    phone = models.CharField(_('Phone'), max_length=11, blank=True, null=True)
    cell_phone = models.CharField(_('Cell Phone'), max_length=11, blank=True, null=True)
    street = models.CharField(_('Street'), max_length=100)
    number = models.IntegerField(_('Number'), null=True, blank=True, validators=[MinValueValidator(1)])
    complement = models.CharField(_('Complement'), max_length=35, blank=True, null=True)
    email = models.EmailField(_('E-mail'))
    approved = models.BooleanField(_('Approved'), default=False)
    associated_from = models.DateField(_('Associated from'))

    class Meta:
        verbose_name = _('Associate')
        verbose_name_plural = _('Associates')

    def __str__(self):
        return '{0} - [{1}]'.format(self.name,
                                    _('Approved') if self.approved else _('Waiting for approval'))


class News(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title


class ImageNews(models.Model):
    news_id = models.ForeignKey('core.News', on_delete=models.CASCADE, related_name='image', verbose_name='News')
    image = models.ImageField(upload_to='news', null=True, blank=True)

    class Meta:
        verbose_name = _('Image news')
        verbose_name_plural = _('Images news')


class Request(models.Model):
    OTHERS = 1
    SECURITY = 2
    LIGHTING = 3
    CONSTRUCTION = 4
    CLEANING = 5

    SUBJECT_CHOICES = (
        (OTHERS, _('Others')),
        (SECURITY, _('Security')),
        (LIGHTING, _('Lighting')),
        (CONSTRUCTION, _('Construction')),
        (CLEANING, _('Cleaning')),
    )

    OPEN = 'O'
    WAITING = 'W'
    CLOSED = 'C'

    STATUS_CHOICE = (
        (OPEN, _('Open')),
        (WAITING, _('Waiting')),
        (CLOSED, _('Closed')),
    )

    email = models.EmailField(_('E-mail'))
    name = models.CharField(_('Name'), max_length=50)
    phone = models.CharField(_('Phone'), max_length=11)
    street = models.CharField(_('Street'), max_length=100)
    number = models.IntegerField(_('Number'), null=True, blank=True, validators=[MinValueValidator(1)])
    complement = models.CharField(_('Complement'), max_length=35, blank=True, null=True)
    description = models.TextField(_('Description'))
    status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICE, default=OPEN)
    subject = models.IntegerField(_('Subject'), choices=SUBJECT_CHOICES)

    class Meta:
        verbose_name = _('Request')
        verbose_name_plural = _('Requests')

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(_('Title'), max_length=80)
    description = models.TextField(_('Description'))
    date = models.DateField(_('Date'))
    principal_image = models.ImageField(upload_to="Gallery", null=True, blank=True)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    gallery_id = models.ForeignKey('core.Gallery', on_delete=models.CASCADE, related_name='images', verbose_name='Gallery')
    image = models.ImageField(upload_to="Gallery", null=True, blank=True)

    class Meta:
        verbose_name = _('Image gellery')
        verbose_name_plural = _('Images galleries')

    def __str__(self):
        return str(self.image)


class Classified(models.Model):
    title = models.CharField(_('Title'), max_length=80)
    description = models.TextField(_('Description'))
    site = models.URLField(_('Site'))

    class Meta:
        verbose_name = _('Classified')
        verbose_name_plural = _('Classifieds')

    def __str__(self):
        return self.title


class ImageClassified(models.Model):
    classified_id = models.ForeignKey('core.Classified', on_delete=models.CASCADE, related_name='image', verbose_name='Classified')
    image = models.ImageField(upload_to="Classified", null=True, blank=True)

    class Meta:
        verbose_name = _('Image classified')
        verbose_name_plural = _('Images classified')


class Member(models.Model):
    name = models.CharField(_('Name'), max_length=80)
    charge = models.CharField(_('Charge'), max_length=80)
    email = models.EmailField()
    image = models.ImageField(upload_to='members', null=True, blank=True)

    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Members')

    def __str__(self):
        return self.name


class Association_information(models.Model):
    company_name = models.CharField(_('Company name'), max_length=120)
    name = models.CharField(_('Name'), max_length=80)
    cnpj = models.CharField(_('CNPJ'), max_length=18)
    email = models.EmailField()
    long_description = models.TextField(_('Long Description'))
    home_description = models.TextField(_('Home Description'))

    class Meta:
        verbose_name = _('Association information')
        verbose_name_plural = _('Association information')

    def __str__(self):
        return self.name


class UsefulPhone(models.Model):
    name = models.CharField(_('Name'), max_length=80)
    phone1 = models.CharField(_('Phone'), max_length=15)
    phone2 = models.CharField(_('Phone'), max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = _('Useful_phone')
        verbose_name_plural = _('Useful_phones')

    def __unicode__(self):
        return self.name


class CategoryAssociates(models.Model):
    RESIDENTIAL = 'R'
    GROUND = 'G'
    COMPANY = 'C'
    INDIVIDUAL = 'I'

    CATEGORY_CHOICES = (
        (None, ''),
        (RESIDENTIAL, _('Residential')),
        (GROUND, _('Ground')),
        (COMPANY, _('Company')),
        (INDIVIDUAL, _('Individual')),
    )

    category_type = models.CharField( _('Subject'), max_length=1, choices=CATEGORY_CHOICES)
    price = models.DecimalField(_('Price'), max_digits=11, decimal_places=2)

    class Meta:
        verbose_name = _('Category Associates')
        verbose_name_plural = _('Categories Associates')

    def __str__(self):
        return self.category_type


class Document(models.Model):
    STATUTE = 'S'
    RECORD = 'R'
    CRAFT = 'C'
    DOCUMENTS = 'D'

    DOCUMENT_CHOICES = (
        (None, ''),
        (STATUTE, _('Statute')),
        (RECORD, _('Record')),
        (CRAFT, _('Craft')),
        (DOCUMENTS, _('Documents'))
    )
    name = models.CharField(_('Name'), max_length=80)
    document_type = models.CharField(_('Documents'), max_length=1, choices=DOCUMENT_CHOICES)
    document = models.FileField(upload_to="Documents", null=True, blank=True)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    def __str__(self):
        return self.name
