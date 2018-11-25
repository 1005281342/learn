

class Solution:
    # u2takey2
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        s, i = [], 0
        for a in pushed:
            s.append(a)
            while s and s[-1] == popped[i]:
                s.pop()
                i += 1
        return len(s) == 0

    # @fishballLin
    # def validateStackSequences(self, pushed, popped):
    #     """
    #     :type pushed: List[int]
    #     :type popped: List[int]
    #     :rtype: bool
    #     """
    #     stack = list()
    #     appear_set = set()
    #     sequence_length = len(pushed)
    #     push_idx = 0
    #     pop_idx = 0
    #
    #     while pop_idx < sequence_length:
    #         if popped[pop_idx] in appear_set:
    #             if popped[pop_idx] == stack[-1]:
    #                 stack.pop(-1)
    #                 appear_set.remove(popped[pop_idx])
    #                 pop_idx += 1
    #             else:
    #                 return False
    #         else:
    #             if push_idx < sequence_length:
    #                 stack.append(pushed[push_idx])
    #                 appear_set.add(pushed[push_idx])
    #                 push_idx += 1
    #             else:
    #                 return False
    #
    #     return True
