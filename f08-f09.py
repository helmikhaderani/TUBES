def peminjaman_gadgets():
    
    gadgets = []

    with open(gadget.csv , mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            gadgets.append(row)
