def bubble_sort(array):
    """
    Sorts an array using the bubble sort algorithm.
    
    Parameters:
        array (list): The array to be sorted.
        
    Returns:
        list: The sorted array.
    """
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # Swap if the element found is greater than the next element
                array[j], array[j+1] = array[j+1], array[j]
    return array

# if __name__ == "__main__":
#     # Example usage
#     data = [64, 34, 25, 12, 22, 11, 90]
#     print("Unsorted array:", data)
#     sorted_data = bubble_sort(data)
#     print("Sorted array:", sorted_data)