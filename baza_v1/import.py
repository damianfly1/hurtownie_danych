import csv
from datetime import datetime
from baza_v1.models import Airport
from baza_v1.models import Owner
from baza_v1.models import ReferencePoint
from baza_v1.models import Manager

with open("Airports.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a = Airport.objects.create(
            site_number=row["Site_Num"],
            type=row["Fac_Type"],
            location_id=row["Loc_Id"],
            date=datetime.strptime(row["Eff_Date"], "%m/%d/%Y"),
            region_code = row["Region_Cod"],
            jet_count = row["Based_Jet_"] if row["Based_Jet_"] is not '' else 0,
            helicopter_count = row["Based_Heli"] if row["Based_Heli"] is not '' else 0,
            military_aircraft_count = row["Based_Mili"] if row["Based_Mili"] is not '' else 0,
            commercial_aircraft_count = row["Commercial"] if row["Commercial"] is not '' else 0,
            flight_count = row["Ga_Local_O"] if row["Ga_Local_O"] is not '' else 0,
        )
        Owner.objects.create(
            airport=a,
            owner_name=row["Owner_Name"],
            owner_addr=row["Owner_Addr"],
            owner_city=row["Owner_City"],
            owner_phon=row["Owner_Phon"],
        )
        ReferencePoint.objects.create(
            airport = a,
            ref_point_1 = row["Ref_Poin_1"],
            ref_point_2 = row["Ref_Poin_2"],
            ref_point_3 = row["Ref_Poin_3"],
            ref_point_4 = row["Ref_Poin_4"],
        )
        Manager.objects.create(
            airport=a,
             manager_name=row["Manager_Na"],
             manager_addr=row["Manager_Ad"],
             manager_city=row["Manager_Ci"],
             manager_phon=row["Manager_Ph"],
        )