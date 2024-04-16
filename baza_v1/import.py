import csv
from datetime import datetime
from baza_v1.models import Airport
from baza_v1.models import Owner

with open("Airports.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a = Airport.objects.create(
            site_num=row["Site_Num"],
            fac_type=row["Fac_Type"],
            loc_id=row["Loc_Id"],
            eff_date=datetime.strptime(row["Eff_Date"], "%m/%d/%Y"),
        )
        Owner.objects.create(
            airport = a,
            owner_name=row["Owner_Name"],
            owner_addr=row["Owner_Addr"],
            owner_city=row["Owner_City"],
            owner_phon=row["Owner_Phon"],
        )
        Owner.objects.create(
            airport = a,
            ref_point_1 = row["Ref_Poin_1"],
            ref_point_2 = row["Ref_Poin_2"],
            ref_point_3 = row["Ref_Poin_3"],
            ref_point_4 = row["Ref_Poin_4"],
        )