"""
2437. Number of Valid Clock Times

You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm".
 The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.

Example 1:

Input: time = "?5:00"
Output: 2
Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it
with a 2, since the time "25:00" is invalid. In total, we have two choices.
"""


def count_time(time):
    possible_hours = 1
    possible_minutes = 1

    if time[0] == '?' and time[1] != '?':
        if time[1] <= "3":
            possible_hours = possible_hours * 3
        else:
            possible_hours = possible_hours * 2
    elif time[0] != '?' and time[1] == '?':
        if time[0] <= 1:
            possible_hours = possible_hours * 10
        else:
            possible_hours = possible_hours * 4
    elif time[0] == '?' and time[1] == '?':
        possible_hours = possible_hours * 24

    if time[3] == '?':
        possible_minutes = possible_minutes * 6

    if time[4] == '?':
        possible_minutes = possible_minutes * 10

    answer = possible_minutes * possible_hours
    return answer


"""
ALGORİTMA 

1)
time = time.split(':')
hour = time[0]
minute = time[1]

2) burada bizim bakmamız gereken yer hour. Çünkü minute'ın [0]'ı daima 6 farklı (0,1,2,3,4,5); minute'ın [1]'i ise 
   10 farklı değer alabilir (0,1,2,3,4,5,6,7,8,9)
   
3) eğer hour[0]'ı bilinmiyorsa hour[1]'in değerine bakılır. Bu değer 4 ve 4'ten büyükse hour[0] 0,1 değerlerini alabilir,
   4'ten küçükse 0,1,2 değerlerini alabilir

4) eğer hour[1] bilinmiyorsa hour[0] değerine bakılır. Bu değer 0 veya 1 ise hour[1] 0,1,2,3,4,5,6,7,8,9 alabilir
   eğer hour[0] 2 ise, hour[1] 0,1,2,3 değerlerini alabilir.

5) eğer hour[0]'da hour[1]'de bilinmiyorsa hour toplamda 24 farklı değer alabilir.

NOT: Bu soruda önemli olan 24 değerinin gerçekte var olmadığını unutmamak. Çünkü saat 24 olmaz 00 olur.   

"""




