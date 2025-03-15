def main():
    date = get_date("Date: ")
    print (f"{date[0]}-{date[1]}-{date[2]}")

def get_date(prompt):
    cal = {"January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"}
    
    while True:
        try:
            endian = input(prompt)
            if "A" <= endian[0] <= "Z":
                mon , day , ye = endian.split()
                if mon in cal:
                    mon = cal[mon]
                else:
                    raise KeyError
                day = day.rstrip(",")
                if int(day) <= 9:
                    day = "0" + day
                else:
                    pass
                
            elif int(endian[0]) <= 9:
                mon , day , ye = endian.split("/")
                if int(mon) <= 9:
                    mon = "0" + mon
                else:
                    pass
                if int(day) <= 9:
                    day = "0" + day
                else:
                    pass

            else:
                raise KeyError
            return [ye, mon, day]
            
        except (ValueError, KeyError):
            pass
    
main()