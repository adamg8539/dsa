class MyQueue(object):

    def __init__(self):
        self.stack = []        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        val = self.stack[0]
        self.stack = self.stack[1:]
        return val

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack:
            return False
        return True
      