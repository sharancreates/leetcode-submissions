class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        latest_arrive = max(arriveAlice, arriveBob)
        earliest_leave = min(leaveAlice, leaveBob)

        if latest_arrive > earliest_leave:
            return 0

        start_month, start_day = int(latest_arrive[:2]), int(latest_arrive[3:])
        end_month, end_day = int(earliest_leave[:2]), int(earliest_leave[3:])
        
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if start_month == end_month:
            return end_day - start_day + 1
            
        else:
            total_days = days_in_months[start_month - 1] - start_day + 1
            
            total_days += end_day
            for m in range(start_month + 1, end_month):
                total_days += days_in_months[m - 1]
                
            return total_days
