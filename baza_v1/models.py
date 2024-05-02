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


# Punkty odniesienia
class ReferencePoint(models.Model):
    ref_point_1 = models.CharField(max_length=255, default="")  # punkt1
    ref_point_2 = models.CharField(max_length=255, default="")  # punkt2
    ref_point_3 = models.CharField(max_length=255, default="")  # punkt2
    ref_point_4 = models.CharField(max_length=255, default="")  # punkt3

    class Meta:
        db_table = "ReferencePoint"

class SiteNumber(models.Model):
    site_number = models.CharField(max_length=255, unique=True)  # kod lotniska

    class Meta:
        db_table = "SiteNumber"

class Type(models.Model):
    type = models.CharField(max_length=255)  # typ lotniska

    class Meta:
        db_table = "Type"

class RegionCode(models.Model):
    region_code = models.CharField(max_length=255)  # kod regionu

    class Meta:
        db_table = "RegionCode"

class Location(models.Model):
    location = models.CharField(max_length=255)  # id lokalizacji

    class Meta:
        db_table = "Location"

# Lotnisko
class Airport(models.Model):
    
    date = models.DateField()  # data dodania danych, mapuje się do eff_date

    # tabele faktów
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    reference_point = models.ForeignKey(ReferencePoint, on_delete=models.CASCADE)
    site_number = models.ForeignKey(SiteNumber, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    region_code = models.ForeignKey(RegionCode, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # agregaty
    jet_count = models.IntegerField()  # liczba myśliwców
    helicopter_count = models.IntegerField()  # liczba helikopterów
    military_aircraft_count = models.IntegerField()  # liczba militarnych
    commercial_aircraft_count = models.IntegerField()  # liczba cywlinych
    flight_count = models.IntegerField()  # ilość lotów (Ga_Local_O)

    class Meta:
        db_table = "Airport"
