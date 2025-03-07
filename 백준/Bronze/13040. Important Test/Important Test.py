import sys
input = sys.stdin.readline
def max_tasks_per_variant(n, t, t0, variants):
    results = []
    
    for variant in variants:
        m, *tasks = variant
        max_tasks = 0
        
        # Case 1: Solve tasks without copying
        time_spent = 0
        for i in range(m):
            if time_spent + tasks[i] <= t:
                time_spent += tasks[i]
                max_tasks += 1
            else:
                break
        
        # Case 2: Solve tasks with copying
        for j in range(m):
            if t0 > t:  # If copying itself exceeds the time limit, skip
                break
            
            time_spent = t0  # Copying time spent
            copied_tasks = 0
            
            for i in range(m):
                if i == j:  # Skip the copied task
                    continue
                
                if time_spent + tasks[i] <= t:
                    time_spent += tasks[i]
                    copied_tasks += 1
                else:
                    break
            
            max_tasks = max(max_tasks, copied_tasks + 1)  # Include copied task
        
        results.append(max_tasks)
    
    return results

# Input reading
n, t, t0 = map(int, input().split())
variants = [list(map(int, input().split())) for _ in range(n)]

# Processing and output
for result in max_tasks_per_variant(n, t, t0, variants):
    print(result)
