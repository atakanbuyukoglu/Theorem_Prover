

class Set(set):
    """A set class to also include sets with infinite number of elements.
    """
    def __init__(self, seq=(), cond=None, parent_set=None, parent_cond=None, var_name=None):
        """

        :param seq: The sequence to define a set of this class. To be used for only finite sets.
        :param cond : The condition for an element to be an element of this set.
        :param parent_set: The parent set to define this set. Can be infinite.
        :param parent_cond: The condition imposed on the parent set to generate this set.
        """
        super().__init__(seq)
        self.var_name = var_name
        self.seq = seq
        self.cond = cond
        self.parent_set = parent_set
        self.parent_cond = parent_cond

    def __contains__(self, item):
        """Returns true if the item is in the set, false otherwise.

        :param item:
        :return: True if item is in the set, False otherwise
        """
        # If defined as a set, handle from the set class
        if self.seq != ():
            return super().__contains__(item)
        # Else, handle using condition
        return (item in self.parent_set) and self.parent_cond.check(item)

    def __str__(self):
        result = ''

        # If there is a name, add it
        if self.var_name:
            result += self.var_name
            result += ' = '

        # Defined by enumeration of elements
        if self.seq != ():
            result += super().__str__()
        # Defined on condition from another set
        else:
            result += '{ '   # Open the set definition
            result += 'x in '
            if self.parent_set.var_name:
                result += self.parent_set.var_name
            else:
                result += self.parent_set.__str__()
            result += ' : '
            result += self.parent_cond.__str__()
            result += ' }'   # Close the set definition
        return result
