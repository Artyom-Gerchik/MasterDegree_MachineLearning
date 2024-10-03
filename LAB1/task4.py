class Task4Manager:
     
    @staticmethod
    def check_sets_duplicates(subset1, subset2, subset3):
        if len(subset1) != len(set(subset1)) or len(subset2) != len(set(subset2)) or len(subset2) != len(set(subset2)):
            print("Given sets has duplicates")
            return
        else:
            set1, set2, set3 = set(subset1), set(subset2), set(subset3)
            dup_12 = set1 & set2
            dup_13 = set1 & set3
            dup_23 = set2 & set3

            if len(dup_12) + len(dup_13) + len(dup_23) == 0:
                print("Given sets doesn't has duplicates")
                return
            else:
                print("Given sets has duplicates")
                return    
