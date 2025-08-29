

result = []
def solu(row, col, mat, visited, order):

    visited[row][col] = True
    if row == len(mat)-1 and col == len(mat)-1:
        result.append(order)
        visited[row][col] = False
        return

    if col-1 >= 0 and not visited[row][col-1] and mat[row][col-1] == 1:
        solu(row, col-1, mat, visited, order + "L")

    if row - 1 >= 0 and not visited[row - 1][col] and mat[row - 1][col] == 1:
        solu(row - 1, col, mat, visited, order + "U")

    if col + 1 < len(mat) and not visited[row][col+1] and mat[row][col+1] == 1:
        solu(row, col+1, mat, visited, order + "R")

    if row + 1 < len(mat) and not visited[row + 1][col] and mat[row + 1][col] == 1:
        solu(row + 1, col, mat, visited, order + "D")
    visited[row][col] = False

    return


if __name__ == '__main__':
    mat = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    visited = []
    order = ""
    for i in range(len(mat)):
        row = []
        for j in range(len(mat)):
            row.append(False)
        visited.append(row)

    solu(0, 0, mat, visited, order)

    print(result)


