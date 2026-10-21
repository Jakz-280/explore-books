import csv
# comma seperated value

with open("YA_Books.csv", mode="r", encoding="utf-8") as bookfile:
    # mode "r" means read
    # as bookfile means alias/nickname

    books = csv.reader(bookfile)
    # skip the header row
    header = next(books)
    # Author col is at index 1

    MINyear = 0
    CurMIN_rating = 5
    CurHI_rating = 0
    for row in books:
        # print out only authors that start with "m"
        if row[1].startswith("M"):
            print(row[1])

        # print out last names (slice)
        authorname = row[1]
        lastindex = authorname.rfind(" ")
        lastname = authorname[lastindex + 1:]
        if lastname.startswith("J"):
            print(authorname)

        # find most recent book (highest number)
        year = int(row[2])
        if MINyear < year:
            MINyear = year
            MostREC_book = row

        # get the book with WORST (absolute BUNS) rating:
        rating = float(row[6])
        if CurMIN_rating > rating:
            CurMIN_rating = rating
            LOWrating = row

        rating = float(row[6])
        if CurHI_rating < rating:
            CurHI_rating = rating
            HI_rating = row

    print(f"the WORST, absolute BUNS and TRASH book: \n{LOWrating}")
    print(f"most recent book: \n{MostREC_book}")
    print(f"the book with the highest rating is: \n'{HI_rating[0]}' by {HI_rating[1]} with a rating of {HI_rating[6]}")
    print(year) 


    # what is the highest rating in the data set and who wrote it