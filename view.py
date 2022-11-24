from funcs1 import read_csv_file, write_csv_file
from funcs2 import read_txt_file, write_txt_file

def read_data(tape):
    if tape == 'csv':
        data = read_csv_file()
    elif tape == 'txt':
        data = read_txt_file()
    return data        
    
def print_data(data):
    for i in range(len(data)):
        print(
            f'\nПродукт: {data[i][0]}, Белки: {data[i][1]}, Жиры: {data[i][2]}, Углеводы: {data[i][3]}, Каллорийность: {data[i][4]}\n')

def write_data():
    pass
            
def run():
    data = read_data(type = 'csv')
    data.sort()
    print_data(data)
    write_data(data)


 
