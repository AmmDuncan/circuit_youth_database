from django.db import models


# Create your models here.
from django.urls import reverse


class PositionChoices(models.Choices):
    LEADER = 1
    SECRETARY = 2
    ORGANIZING_SECRETARY = 3
    FINANCIAL_SECRETARY = 4
    PRAYER = 5
    EVANGELISM = 6
    MEMBER = 7


class Local(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)


class Executive(models.Model):
    name = models.CharField(max_length=100, unique=True)
    position = models.IntegerField(choices=PositionChoices.choices,
                                   default=PositionChoices.MEMBER)
    address = models.CharField(max_length=100, blank=True)
    local = models.ForeignKey(Local,
                              related_name="executives",
                              on_delete=models.CASCADE)
    phone1 = models.CharField(max_length=15, blank=True)
    phone2 = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ("position", )

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100, blank=True)
    phone1 = models.CharField(max_length=15, blank=True)
    phone2 = models.CharField(max_length=15, blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    local = models.ForeignKey(Local,
                              related_name="members",
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_edit_url(self):
        return reverse("locals:members-edit", kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse("locals:members-detail", kwargs={'pk': self.pk})

    class Meta:
        ordering = ("name",)

