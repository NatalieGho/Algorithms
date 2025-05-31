def greedyalgorithm(times_array):
    times_array.sort()
    timeSheet = []
    current_start, current_end = times_array[0]
    for i in range(1, len(times_array)):
        next_start, next_end = times_array[i]
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            timeSheet.append((current_start, current_end))
            current_start, current_end = next_start, next_end
    #making sure to add the last interval
    timeSheet.append((current_start, current_end))
    Solution(timeSheet)
def Solution(time_sheet):
    result = []
    for number in range(len(time_sheet)):
        (value1,value2) = time_sheet[number]
        if number == len(time_sheet)-1:
            result.append(str(value1) + "-" + str(value2))
        else:
            result.append(str(value1) + "-" + str(value2) + ",")
    print(" ".join(result))
test_cases = int(input())
for _ in range(test_cases):
    shifts = int(input().strip())
    times_array = []
    for each in range(shifts):
        s, m = map (int, input().split(" "))
        times_array.append((s,m))
    greedyalgorithm(times_array)
