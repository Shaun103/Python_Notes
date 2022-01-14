import csv 

# with open('googleData.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     # for line in csv_reader:   # 
#     #     print(line['Date'])
#     #     print(line['High'])

#     with open('new_googleData.csv', 'w') as new_file:
#         fieldnames = ['Date', 'Open', 'Low', 'Adj Close', 'Close', 'Volume', 'High']

#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

#         csv_writer.writeheader()

#         for line in csv_reader:
#             csv_writer.writerow(line)


#_____________________________________________________________________________


# Deleting specific column from

with open('googleData.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line['Date'])
    #     print(line['Low'])
    #     print(line['High'])

    with open('new_googleData.csv', 'w',  newline='') as new_file:
        fieldnames = ['Date','Low', 'High']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['Adj Close']       # deleting the lines we do not want
            del line['Volume']
            del line['Close']
            del line['Open']
            csv_writer.writerow(line)