from typing import Any, List, Optional


class Leaf:
    data:      Any | None = None
    data_desc: Any | None = None

    def __init__(self, data: Any = None, data_desc: Optional = None):
        self.data = data
        self.data_desc = data_desc

    def get_data(self):
        return self.data

    def get_data_desc(self):
        return self.data_desc

    def reset(self):
        self.data = None

    def set_data(self, newdata: Any):
        self.data = newdata

    def set_data_desc(self, newdesc: Any):
        self.data_desc = newdesc


class Branch:
    left                      = None
    right                     = None
    leaves: List[Leaf] | None = None

    def __init__(self, left: Any = None, right: Any = None, leaves: List = None):
        self.left = left
        self.right = right
        self.leaves = leaves

    def get_leaves(self):
        return self.leaves

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def reset(self):
        self.left, self.right, self.leaves = None, None, None

    def set_left(self, newleft):
        self.left = newleft

    def set_right(self, newright):
        self.right = newright


class Tree:
    left:           Branch | None = None
    right:          Branch | None = None
    branches: List[Branch] | None = None

    def __init__(self, left: Branch = None, right: Branch = None, branches: List = None):
        self.left = left
        self.right = right
        self.branches = branches

    def get_branches(self):
        return self.branches

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def reset(self):
        self.left, self.right, self.branches = None, None, None

    def set_left(self, newleft: Branch | None):
        self.left = newleft

    def set_right(self, newright: Branch | None):
        self.right = newright
