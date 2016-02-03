from django.contrib.gis.db import models
from django_extensions.db.models import TimeStampedModel


class Authority(TimeStampedModel):
    authority_id = models.CharField(primary_key=True, max_length=100)
    authority_type = models.CharField(blank=True, max_length=10)
    mapit_id = models.CharField(blank=True, max_length=100, db_index=True)
    ons_id = models.CharField(blank=False, max_length=100, unique=True, null=True)
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=100)
    website = models.URLField(blank=True)
    postcode = models.CharField(blank=True, null=True, max_length=100)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.authority_id)

    class Meta:
        verbose_name_plural = "authorities"
        ordering = ('name',)

    def election_urls(self):
        return self.authorityservicedetails_set.filter(LGSL_id=362)

    @property
    def child_areas(self):
        return self.mapitarea_set.all().order_by('name')


class AuthorityGeo(TimeStampedModel):
    authority = models.OneToOneField('Authority', null=True)
    location = models.PointField(null=True, blank=True)
    area = models.MultiPolygonField(
        null=True, blank=True, geography=True, srid=4326)

    def __str__(self):
        return "{0} ({1})".format(
            self.authority.name, self.authority.authority_id)


class AuthorityServiceCategory(models.Model):
    """
    The Taxonomy of local services from local.direct.gov

    Data from
    https://raw.githubusercontent.com/alphagov/publisher/master/data/local_services.csv
    """
    LGSL = models.IntegerField(primary_key=True)
    description = models.CharField(blank=True, max_length=800)
    providing_tier = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return "{0} ({1})".format(self.LGSL, self.description)


class AuthorityServiceDetails(models.Model):
    SNAC = models.ForeignKey(Authority, to_field='ons_id')
    LAid = models.IntegerField(blank=True, null=True)
    LGSL = models.ForeignKey(AuthorityServiceCategory)
    LGIL = models.IntegerField(blank=True, null=True)
    URL = models.URLField(blank=True, max_length=800)
    last_updated = models.DateTimeField(blank=True)

    def __str__(self):
        return "{0} – {1}".format(
            self.SNAC.name,
            self.LGSL.description
        )


class MapitArea(models.Model):
    gss = models.CharField(max_length=100, primary_key=True)
    parent_authority = models.ForeignKey(Authority, null=True)
    name = models.CharField(blank=True, max_length=100)
    area_type = models.CharField(blank=True, max_length=100)
    unit_id = models.CharField(blank=True, max_length=100)
    type_name = models.CharField(blank=True, max_length=255)
    country_name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name
