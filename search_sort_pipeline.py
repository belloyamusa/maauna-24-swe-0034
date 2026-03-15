import random

def generate_scores():
    """Generate 10 random integers between 1 and 100 representing candidate scores"""
    return [random.randint(1, 100) for _ in range(10)]

def merge_sort(arr):
    """Recursive merge sort algorithm"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def binary_search(sorted_arr, target):
    """Binary search to find the index of target value in sorted array"""
    left, right = 0, len(sorted_arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Score not found

def library_search(sorted_arr, target):
    """Search function that uses binary search to find the score's index"""
    return binary_search(sorted_arr, target)

def main():
    print("=== Event Judging Application ===\n")
    
    # 1. Generate random scores
    scores = generate_scores()
    print(f"Original scores: {scores}")
    
    # 2. Sort scores using recursive merge sort
    sorted_scores = merge_sort(scores)
    print(f"Sorted scores: {sorted_scores}")
    
    # 3. Get user input
    try:
        target_score = int(input("\nEnter a score to search for: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    # 4. Search and display result
    rank = library_search(sorted_scores, target_score)
    
    if rank != -1:
        print(f"Candidate with score = {target_score} found at rank = {rank}")
    else:
        print(f"Score {target_score} not found in the list.")

if __name__ == "__main__":
    main()
