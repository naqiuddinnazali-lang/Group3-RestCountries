import sys
from g3_scrape import get_asian_countries
from g3_excel import save_to_excel
#from g3_condition import
#from g3_db import

def run_pipeline():
    countries = get_asian_countries()
    for c in countries:
        print(c)
        file_path = save_to_excel(c)
        print("Excel file saved to:", file_path)

    

if __name__ == "__main__":
    run_pipeline()