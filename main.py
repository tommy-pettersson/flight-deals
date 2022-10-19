from data_manager import DataManager
from pprint import pprint

def main():

    sheet_data = DataManager.get_sheet_data()
    pprint(sheet_data)


if __name__ == "__main__":
    main()