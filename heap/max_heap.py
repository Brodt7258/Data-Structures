class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        print('starting:', self.storage)
        if not len(self.storage):
            return None
        
        elif len(self.storage) == 1:
            print('popped last:', self.storage[0])
            return self.storage.pop()
        
        else:
            removed, self.storage[0] = self.storage[0], self.storage.pop()
            print('popped off:', removed)
            self._sift_down(0)
            return removed

    def get_max(self):
        if not len(self.storage):
            return None
        
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = self._get_parent_index(index)
        if parent_index is None or self.storage[index] <= self.storage[parent_index]:
            return

        else:
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        left_index, right_index = self._get_children_indices(index)
        
        # if there are no children, then there is nowhere to sift down to, done
        if left_index is None:
            return

        left_val = self.storage[left_index]
        right_val = self.storage[right_index] if right_index is not None else None
        larger_child = (left_index, left_val) if right_index is None or left_val >= right_val else (right_index, right_val)

        # if both children are smaller than the current value, the heap is in order, done
        if larger_child[1] <= self.storage[index]:
            return

        else:
            self.storage[index], self.storage[larger_child[0]] = self.storage[larger_child[0]], self.storage[index]
            self._sift_down(larger_child[0])

    def _get_parent_index(self, index):
        return (index - 1) // 2 if index > 0 else None

    def _get_children_indices(self, index):
        left = 2 * index + 1 if 2 * index + 1 < len(self.storage) else None
        right = 2 * index + 2 if 2 * index + 2 < len(self.storage) else None

        return (left, right)
