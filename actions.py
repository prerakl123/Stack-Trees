from tree import Tree, Branch, Leaf


class UndoLeaf(Leaf):
    pass


class UndoBranch(Branch):
    pass


class UndoStack(Tree):
    pass


class RedoLeaf(Leaf):
    pass


class RedoBranch(Branch):
    pass


class RedoStack(Tree):
    pass
