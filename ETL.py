import csv
from baza_v1.models import Airport
from baza_v1.models import Owner
from baza_v1.models import Manager
from baza_v1.models import Type
from baza_v1.models import RegionCode
from baza_v1.models import Location


with open("Airports.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        owner = Owner.objects.filter(
            owner_name=row["Owner_Name"],
            owner_addr=row["Owner_Addr"],
            owner_city=row["Owner_City"],
            owner_phon=row["Owner_Phon"],
        ).first()
        if owner is None:
            owner = Owner.objects.create(
                owner_name=row["Owner_Name"],
                owner_addr=row["Owner_Addr"],
                owner_city=row["Owner_City"],
                owner_phon=row["Owner_Phon"],
            )

        manager = Manager.objects.filter(
            manager_name=row["Manager_Na"],
            manager_addr=row["Manager_Ad"],
            manager_city=row["Manager_Ci"],
            manager_phon=row["Manager_Ph"],
        ).first()
        if manager is None:
            manager = Manager.objects.create(
                manager_name=row["Manager_Na"],
                manager_addr=row["Manager_Ad"],
                manager_city=row["Manager_Ci"],
                manager_phon=row["Manager_Ph"],
            )

        type = Type.objects.filter(
            type=row["Fac_Type"],
        ).first()
        if type is None:
            type = Type.objects.create(
                type=row["Fac_Type"],
            )

        region_code = RegionCode.objects.filter(
            region_code=row["Region_Cod"],
        ).first()
        if region_code is None:
            region_code = RegionCode.objects.create(region_code=row["Region_Cod"])

        location = Location.objects.filter(
            state_post=row["State_Post"],
            state_name=row["State_Name"],
            country=row["County"],
            country_pos=row["County_Pos"],
            city=row["City"],
        ).first()
        if location is None:
            location = Location.objects.create(
                state_post=row["State_Post"],
                state_name=row["State_Name"],
                country=row["County"],
                country_pos=row["County_Pos"],
                city=row["City"],
            )

        airport = Airport.objects.filter(
            owner=owner,
            manager=manager,
            type=type,
            region_code=region_code,
            location=location,
        ).first()
        if airport is None:
            Airport.objects.create(
                owner=owner,
                manager=manager,
                type=type,
                region_code=region_code,
                location=location,
                count=0,
            )
        else:
            airport.count += 1
            airport.save()
