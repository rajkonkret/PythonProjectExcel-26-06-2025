# konwersja plików przy pomocy pyexcel
# pip instrall pyexcel-csv
import pyexcel as pe

pe.save_book_as(file_name='wyniki.xlsx',
                dest_file_name="wyniki.csv")
