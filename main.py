Coder: Zain Huda
Student ID:001929695
purpose: To go through the file the user inputs and then find the highest profit movie in that list.

import os
import csv

def get_filename():
    # Keep asking for a valid file name
    filename = input("Enter the input file name: ")
    while not os.path.isfile(filename):
        print("File not found. Please try again.")
        filename = input("Enter the input file name: ")
    return filename

def read_movie_data(filename):
    # Read the data from the CSV file into a list
    file = open(filename, 'r')
    reader = csv.reader(file)
    data = list(reader)
    file.close()
    return data

def write_movie_data_with_profit(data, output_filename):
    file = open(output_filename, 'w', newline='')
    writer = csv.writer(file)
    header = data[0] + ["Profit"]
    writer.writerow(header)
    for row in data[1:]:
        budget = int(row[2])
        worldwide_gross = int(row[4])
        profit = worldwide_gross - budget
        writer.writerow(row + [profit])
    file.close()

def find_highest_profit_movie(data):
    highest_profit = -float('inf')
    highest_profit_movie = None
    for row in data[1:]:
        budget = int(row[2])
        worldwide_gross = int(row[4])
        profit = worldwide_gross - budget
        if profit > highest_profit:
            highest_profit = profit
            highest_profit_movie = row
    return highest_profit_movie

def main():
    input_filename = get_filename()
    movie_data = read_movie_data(input_filename)
    output_filename = input("Enter the output file name: ")
    write_movie_data_with_profit(movie_data, output_filename)
    highest_profit_movie = find_highest_profit_movie(movie_data)
    print("Movie with the highest profit:")
    print(highest_profit_movie)

if __name__ == "__main__":
    main()
