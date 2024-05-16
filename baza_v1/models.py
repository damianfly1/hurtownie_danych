from django.db import models


# Właściciel
class Owner(models.Model):
    owner_name = models.CharField(max_length=255)  # imie właściciela
    owner_addr = models.TextField()  # adres właściciela
    owner_city = models.CharField(max_length=255)  # miasto właściciela
    owner_phon = models.CharField(max_length=255)  # telefon właściciela

    class Meta:
        db_table = "Owner"


# Zarządca
class Manager(models.Model):
    manager_name = models.CharField(max_length=255)  # imie menedzera
    manager_addr = models.TextField()  # adres menedzera
    manager_city = models.CharField(max_length=255)  # miasto menedzera
    manager_phon = models.CharField(max_length=255)  # telefon menedzera

    class Meta:
        db_table = "Manager"


# Typ lotniska
class Type(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        db_table = "Type"


# Kod regionu
class RegionCode(models.Model):
    region_code = models.CharField(max_length=255)

    class Meta:
        db_table = "RegionCode"


# Lokalizacja
class Location(models.Model):
    state_post = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    country_pos = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        db_table = "Location"


# Lotnisko
class Airport(models.Model):
    # tabele faktów
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    region_code = models.ForeignKey(RegionCode, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        db_table = "Airport"
