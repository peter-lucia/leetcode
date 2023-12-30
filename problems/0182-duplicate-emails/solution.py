import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person = person[person["email"].duplicated(keep=False)]
    person = person.rename(columns={"email": "Email"})
    person.drop_duplicates(subset=["Email"], inplace=True)
    return person["Email"].to_frame()

    
