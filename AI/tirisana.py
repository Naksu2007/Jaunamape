import pandas as pd

# Nolasa sākotnējo datu kopu.
df = pd.read_csv("Dati/helpdesk_tickets.csv")

sakuma_rindas = len(df)

# Šajā datu kopā daļai ierakstu trūkst error_code, tāpēc aizstājam tukšās vērtības ar "UNKNOWN".
df["error_code"] = df["error_code"].fillna("UNKNOWN")

# Šajā datu kopā daļai ierakstu trūkst reported_severity, tāpēc aizstājam tās ar biežāk sastopamo kategoriju.
df["reported_severity"] = df["reported_severity"].fillna(
    df["reported_severity"].mode()[0]
)

# Šajā datu kopā dažiem pieteikumiem trūkst wait_time_minutes, tāpēc aizstājam tās ar mediānu.
df["wait_time_minutes"] = df["wait_time_minutes"].fillna(
    df["wait_time_minutes"].median()
)

# Dublikāti var radīt nepareizu statistiku un modeļa apmācību, tāpēc identiskas rindas izņemam.
df = df.drop_duplicates()

beigu_rindas = len(df)

# Saglabā iztīrītos datus jaunā failā, nemainot oriģinālo CSV.
df.to_csv("tirs.csv", index=False)

print(f"Rindu skaits sākumā: {sakuma_rindas}")
print(f"Rindu skaits beigās: {beigu_rindas}")