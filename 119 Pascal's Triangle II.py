class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_arr = [[1] * (i+1) for i in range(rowIndex+1)]
        if rowIndex == 0:
            return pascal_arr[0]
        elif rowIndex ==1:
            return pascal_arr[1]
        else:
            for i in range(2,rowIndex+1):
                for j in range(1,i):
                    pascal_arr[i][j] = pascal_arr[i-1][j-1] + pascal_arr[i-1][j]
                           
        print("Pascal tri is:-", pascal_arr[i])
        return pascal_arr[i]

        