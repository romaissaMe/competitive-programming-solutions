class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
            
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
    
        max_count = sum(1 for task in task_counts if task_counts[task] == max_freq)
    
        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_freq * max_count
        idles = max(0, empty_slots - available_tasks)
        
        return len(tasks) + idles
