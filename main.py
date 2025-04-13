from src.csv_excel_file_reader import read_csv_file
from config import PATH_TO_CSV
from pprint import pprint


if __name__=="__main__":
    pprint(read_csv_file(PATH_TO_CSV))
