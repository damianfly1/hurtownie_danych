from django.db import models

# Lotnisko
class Airport(models.Model):
    site_num = models.CharField(max_length=255, unique=True)
    fac_type = models.CharField(max_length=255)
    loc_id = models.CharField(max_length=255)
    eff_date = models.DateField()
    
    class Meta:
        db_table = "Airport"

# Właściciel
class Owner(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=255)
    owner_addr = models.TextField()
    owner_city = models.CharField(max_length=255)
    owner_phon = models.CharField(max_length=255)

    class Meta:
        db_table = "Owner"

# Zarządca
class Manager(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=255)
    manager_addr = models.TextField()
    manager_city = models.CharField(max_length=255)
    manager_phon = models.CharField(max_length=255)

    class Meta:
        db_table = "Manager"

# Punkty odniesienia
class ReferencePoint(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    ref_point_1 = models.CharField(max_length=255, default='')
    ref_point_2 = models.CharField(max_length=255, default='')
    ref_point_3 = models.CharField(max_length=255, default='')
    ref_point_4 = models.CharField(max_length=255, default='')

    class Meta:
        db_table = "ReferencePoint"

# Statki powietrzne
class BasedAircraft(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.CharField(max_length=255)

    class Meta:
        db_table = "BasedAircraft"