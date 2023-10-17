def print_numbers(start, stop, step):
    current = start
    while current < stop:
        print(current)
        current += step

def thanos(queue_size, target_size):
    snap_count = 0
    while queue_size > target_size:
        queue_size //= 2
        snap_count += 1
    return snap_count