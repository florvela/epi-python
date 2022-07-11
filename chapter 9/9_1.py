## Test if a binary tree is balanced
import collections


def is_balanced_binary_tree(tree):
    BalanceWithHeight = collections.namedtuple(
        'BalanceWithHeight', ('balanced','height')
    )

    def check_balanced(tree):
        if not tree:
            return BalanceWithHeight(balanced=True, height=-1)

        left_res = check_balanced(tree.left)
        if not left_res.balanced:
            return left_res

        right_res = check_balanced(tree.right)
        if not right_res.balanced:
            return right_res

        is_balanced = abs(left_res.height - right_res.height) <= 1
        height = max(left_res.height, right_res.height)
        return BalanceWithHeight(balanced=is_balanced, height=height)

    return check_balanced(tree).balanced


def is_balanced_binary_tree_2(tree):

    def check_balanced(tree):
        if not tree:
            balanced = True
            height = -1
            return balanced, height

        left_res = check_balanced(tree.left)
        if not left_res[0]:
            return left_res

        right_res = check_balanced(tree.right)
        if not right_res[0]:
            return right_res

        is_balanced = abs(left_res[1] - right_res[1]) <= 1
        height = max(left_res[1], right_res[1])
        return is_balanced, height

    return check_balanced(tree)[0]