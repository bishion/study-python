from collections import deque
queue = deque(['guo', 'fang', 'bi'])
queue.append('bishion')
print(queue)
top = queue.popleft()
print(top)
print(queue)

vec = [2, 4, 6]
print([3 * x for x in vec])

print([3 * x for x in vec if x >3])