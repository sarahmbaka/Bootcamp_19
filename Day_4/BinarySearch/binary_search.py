class BinarySearch(list):
    
    """Binary Search class that has search method implemented in binary search."""

    def __init__(self, a, b):
        # Initialise the list
        list.__init__(self)
        self.items_length = a
        self.step = b

        end = self.items_length * self.step
        for i in range(self.step, end + 1, self.step):  # upper limit is a(length of the list) + 1
            self.append(i)

    @property
    def length(self):
        # Return the length of this list
        return len(self)

    def search(self, element, low=0, high=None, count=0):
        # Perform an element search using recursive binary search
        if not high:
            high = self.length - 1

        # checks if input value is equal to the first index or last index
        if element == self[low]:
            return {'index': low, 'count': count}
        elif element == self[high]:
            return {'index': high, 'count': count}

        mid = (low + high) // 2
        if element == self[mid]:
            return {'index': mid, 'count': count}
        elif element > self[mid]:
            low = mid + 1
        elif element < self[mid]:
            high = mid - 1

        # if return is null
        if low >= high:
            return {'index': -1, 'count': count}

        count += 1 
        return self.search(element, low, high, count)
