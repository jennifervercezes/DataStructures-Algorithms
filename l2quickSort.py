
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]


    return quickSort(left) + [pivot] + quickSort(right)

array = [9, 2, 5, 1, 7, 3]
ordenado = quickSort(array)
print(f'\n Array original: {array} \n Array ordenado: {ordenado}')
