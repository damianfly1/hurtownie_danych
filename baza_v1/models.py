from django.db import models

# Lotnisko
class Airport(models.Model):
    site_number = models.CharField(max_length=255, unique=True) #kod lotniska
    type = models.CharField(max_length=255) #typ lotniska
    location_id = models.CharField(max_length=255) #id lokalizacji
    date = models.DateField() #data dodania danych, mapuje się do eff_date
    region_code = models.CharField(max_length=255) #kod regionu
    jet_count = models.IntegerField() #liczba myśliwców
    helicopter_count = models.IntegerField() #liczba helikopterów
    military_aircraft_count = models.IntegerField() #liczba militarnych
    commercial_aircraft_count = models.IntegerField() #liczba cywlinych 
    flight_count = models.IntegerField() #ilość lotów (Ga_Local_O)

    class Meta:
        db_table = "Airport"

# Właściciel
class Owner(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE) #lotnisko
    owner_name = models.CharField(max_length=255) #imie właściciela
    owner_addr = models.TextField() #adres właściciela
    owner_city = models.CharField(max_length=255) #miasto właściciela
    owner_phon = models.CharField(max_length=255) #telefon właściciela

    class Meta:
        db_table = "Owner"

# Zarządca
class Manager(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE) #lotnisko
    manager_name = models.CharField(max_length=255) #imie menedzera
    manager_addr = models.TextField() #adres menedzera
    manager_city = models.CharField(max_length=255) #miasto menedzera
    manager_phon = models.CharField(max_length=255) #telefon menedzera

    class Meta:
        db_table = "Manager"

# Punkty odniesienia
class ReferencePoint(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE) #lotnisko
    ref_point_1 = models.CharField(max_length=255, default='') #punkt1
    ref_point_2 = models.CharField(max_length=255, default='') #punkt2
    ref_point_3 = models.CharField(max_length=255, default='') #punkt2
    ref_point_4 = models.CharField(max_length=255, default='') #punkt3

    class Meta:
        db_table = "ReferencePoint"

# Przypisany statek powietrzny
# class BasedAircraft(models.Model):
#     airport = models.ForeignKey(Airport, on_delete=models.CASCADE) #lotnisko
#     aircraft_type = models.CharField(max_length=255) #typ statku powietrznego

#     class Meta:
#         db_table = "BasedAircraft"