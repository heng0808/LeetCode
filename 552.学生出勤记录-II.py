class Solution:
    def checkRecord(self, n: int) -> int:
        records = []

        def attendance(previous_attendance: str, a_count: int, serial_l_count: int):
            # if a_count > 1 or (len(previous_attendance) > 2 and previous_attendance[-3:] == 'LLL'):
            if a_count > 1 or serial_l_count > 2:
                return
            elif len(previous_attendance) == n:
                records.append(previous_attendance)
            else:
                attendance(previous_attendance + "A", a_count + 1, 0)
                attendance(previous_attendance + "L", a_count, serial_l_count + 1)
                attendance(previous_attendance + "P", a_count, 0)

        attendance("", a_count=0, serial_l_count=0)
        return len(records) % (10 ** 9 + 7)


# ['AAA', 'AAL', 'AAP', 'ALA', 'ALL', 'ALP', 'APA', 'APL', 'APP', 'LAA', 'LAL', 'LAP', 'LLA', 'LLL', 'LLP', 'LPA', 'LPL', 'LPP', 'PAA', 'PAL', 'PAP', 'PLA', 'PLL', 'PLP', 'PPA', 'PPL', 'PPP']
# ['ALL', 'ALP', 'APL', 'APP', 'LAL', 'LAP', 'LLA', 'LLP', 'LPA', 'LPL', 'LPP', 'PAL', 'PAP', 'PLA', 'PLL', 'PLP', 'PPA', 'PPL', 'PPP']
print(Solution().checkRecord(3))
