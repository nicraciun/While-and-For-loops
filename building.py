building = { "Entrance 1": {
                "floor 1": ["ap. 1", "ap. 2", "ap. 3"],
                "floor 2": ["ap. 4", "ap. 5", "ap. 6"],
                "floor 3": ["ap. 7", "ap. 8", "ap. 9"],
                },
             "Entrance 2": {
                "floor 1": ["ap. 10", "ap. 11", "ap. 12"],
                "floor 2": ["ap. 13", "ap. 14", "ap. 15"],
                "floor 3": ["ap. 16", "ap. 17", "ap. 18"],
                },    
             "Entrance 3": {
                "floor 1": ["ap. 19", "ap. 20", "ap. 21"],
                "floor 2": ["ap. 22", "ap. 23", "ap. 24"],
                "floor 3": ["ap. 25", "ap. 26", "ap. 27"],
                }    
            }

for e in building:
    print (f"{e}:")
    for f in building[e]:
        print (f"       {f}:")
        for a in building[e][f]:
            print (f"           {a}")