class HashItem:
    """
    Linked list item that contains key, value and link to the next item
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashList:
    """
    Linked list
    """

    def __init__(self):
        self.head = None
        self.end = None

    def __iter__(self):
        # if list is empty
        if not self.head:
            raise StopIteration

        item = self.head
        # return first item
        yield item

        # return next items
        while True:
            # if end of list
            if not item.next:
                break

            item = item.next
            yield item

    def append(self, item):
        """
        Add new list item to the end of list
        """
        # if list is empty
        if not self.head:
            self.head = item
            self.end = item
        else:
            self.end.next = item
            self.end = item


class HashTable:
    """
    Hash-Table that handle collisions with LinkedList
    """

    def __init__(self):
        # 26 - the number of letters in the alphabet
        self.arr = [None] * 26

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError('Key must be a string')

        item_index = self.get_item_index(key)
        if not self.arr[item_index]:
            hashlist = HashList()
            hashlist.append(HashItem(key, value))
            self.arr[item_index] = hashlist
        else:
            self.arr[item_index].append(HashItem(key, value))

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise KeyError('Key must be a string')

        item_index = self.get_item_index(key)
        item = self.arr[item_index]
        if not item:
            raise KeyError('No value for this key')

        # for item in HashList
        for i in item:
            if i.key == key:
                return i.value

        raise KeyError('No value for this key')

    def __repr__(self):
        string = '{'
        for item in self.arr:
            if item:
                for i in item:
                    if len(string) > 1:
                        string += f", '{i.key}': {i.value}"
                    else:
                        string += f"'{i.key}': {i.value}"

        string += '}'
        return string

    def get_item_index(self, key):
        """
        Return an index for key
        """
        # get order of letter (ord('a') = 97)
        return ord(key.lower()[0]) - 97
