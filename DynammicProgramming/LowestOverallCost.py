def DynamicProgramming(TAtimes, TransferTimes):
    rowsize = len(TAtimes)
    columnsize = len(TAtimes[0])
    DPArray = [[0] * columnsize for _ in range(rows)]
    for i in range(columnsize): #base case for all the values
        DPArray[0][i] = TAtimes[0][i] #at this point, the base cases have been taken care of.
    if rowsize==1:
        return min(DPArray[0])
    #at this point you can do continue since the rowsize is greater than one and can continue
    for currRowNumber in range(1,rowsize):
        for currTeam in range(columnsize):
            TAtime = TAtimes[currRowNumber][currTeam]
            minCost = float('inf')
            for prevTeam in range(columnsize):
                prevCost = DPArray[currRowNumber - 1][prevTeam]
                if currTeam == prevTeam:
                    cost = prevCost + TAtime
                else:
                    cost = prevCost + TAtime + TransferTimes[currRowNumber-1][prevTeam]
                if cost < minCost:
                    minCost = cost
            DPArray[currRowNumber][currTeam] = minCost
    return min(DPArray[-1])
#can instead try finding the min of the value above plus the times.

test_cases = int(input())
for _ in range(test_cases):
    TAs, Questions = map(int, input().split())
    elements = [int(x) for x in input().split(" ")]
    times = [int(x) for x in input().split(" ")]
    columns = TAs//Questions
    rows = Questions
    TAtimes = [[0] * columns for _ in range(rows)]
    second = 0
    for j in range(columns):
        for i in range(rows):
            TAtimes[i][j] = elements[second]
            second += 1
    TransferTimes = [[0] * columns for _ in range(rows - 1)]
    index = 0
    for j in range(columns):  # Iterate over rows
        for i in range(rows-1):  # Iterate over columns
            TransferTimes[i][j] = times[index]
            index += 1
    result = DynamicProgramming(TAtimes,TransferTimes)
    print(result)





