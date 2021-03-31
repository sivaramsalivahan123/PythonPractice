from datetime import date
from datetime import time
from datetime import datetime
def main():
    Date=date.today()
    print(Date)
    print(Date.year)
    print(Date.month)
    print(Date.day)
    Time = datetime.now()
    print(Time.time().strftime(" %I"))
    
if __name__ == "__main__":
    main()