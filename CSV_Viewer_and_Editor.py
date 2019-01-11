import csv

def main():
    filename = "imdb_top_4.csv"
    header = ("Rank", "Rating", "Title")
    data = [
        (1, 9.2, "The Shawshank Redemption(1994)"),
        (2, 9.2,    "The Godfather(1972)"),
        (3, 9, "The Godfather: Part II(1974)"),
        (4, 8.9, "Pulp Fiction(1994)")
    ]

    writer(header, data, filename, "write")
    updater(filename)

def writer(header, data, filename, option):
        with open (filename, "w", newline = "") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")


def updater(filename):
    with open(filename, newline= "") as file:
        readData = [row for row in csv.DictReader(file)]
        # print(readData)
        readData[0]['Rating'] = '9.4'
        # print(readData)

    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")





if __name__=="__main__":
    main()