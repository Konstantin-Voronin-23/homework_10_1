from src.csv_excel_file_reader import read_excel_file, read_csv_file
from config import PATH_TO_CSV, PATH_TO_EXCEL

if __name__ == "__main__":
    print(read_csv_file(PATH_TO_CSV))
