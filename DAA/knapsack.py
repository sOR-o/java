def knapsack(weights, values, maxweight, num):
    M = [[0] * (maxweight + 1) for _ in range(num + 1)]

    for i in range(1, num + 1):
        for w in range(1, maxweight + 1):
            if weights[i] > w:
                M[i][w] = M[i - 1][w]
            else:
                M[i][w] = max(M[i - 1][w], M[i - 1][w - weights[i]] + values[i])

    return M

def FindSolution(M, num, maxweight):
  included = []
  while num:
    if weights[num] <= maxweight and values[num] + M[num-1][maxweight-weights[num]] > M[num-1][maxweight]:
      included.append((weights[num],values[num]))
      maxweight -= weights[num]
    num -= 1
  return included

num = int(input('Enter the number of items: '))
weights = [0] * (num + 1)
values = [0] * (num + 1)

for i in range(1, num + 1):
    weights[i], values[i] = map(int, input(f"Enter the (weight, value) of item {i}: ").split())

maxweight = int(input('Enter the maximum weight: '))
M = knapsack(weights, values, maxweight, num)
print('Maximum value: ', M[num][maxweight])
print('Items included: ', FindSolution(M, num, maxweight))
