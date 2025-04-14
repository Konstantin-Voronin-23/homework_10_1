from src.csv_excel_file_reader import read_csv_file
from src.csv_excel_file_reader import read_excel_file
from config import PATH_TO_CSV
from config import PATH_TO_EXCEL
from pprint import pprint


if __name__=="__main__":
    pprint(read_excel_file(PATH_TO_EXCEL))
