class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
        def f(date_str: str) -> int:
            year, month, day = map(int, date_str.split('-'))
            days_count = 0
            
            days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
            for y in range(1900, year):
                days_count += 366 if is_leap_year(y) else 365
                
            for m in range(1, month):
                if m == 2 and is_leap_year(year):
                    days_count += 29
                else:
                    days_count += days_in_months[m]
                    
            days_count += day
            
            return days_count
        return abs(f(date1) - f(date2))
