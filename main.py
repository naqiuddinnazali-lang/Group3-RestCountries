import sys
import json
from g3_scrape import get_asian_countries
from g3_excel import save_to_excel
from g3_condition import get_top_10_countries
from g3_db import int_db, save_db
from g3_telegram import send_telegram_notification

def run_pipeline():
    countries = get_asian_countries()
    for c in countries:
        print(c)
        file_path = save_to_excel(c)
        print("Excel file saved to:", file_path)

    int_db()
    data = get_top_10_countries()
    record = save_db(data)
    print(json.dumps(record, indent=2))

    send_telegram_notification(record)


if __name__ == "__main__":
    run_pipeline()