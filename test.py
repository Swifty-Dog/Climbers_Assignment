import csv
with open("test.csv", "w", newline='') as file:
    headers = ["id", "name", "country", "rank", "height", "prominence", "range"]
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerow()