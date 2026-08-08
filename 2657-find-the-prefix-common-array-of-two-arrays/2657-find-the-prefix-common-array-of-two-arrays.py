class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if len(A) == len(B):
            C = []
            l = len(A)

            for i in range(l):
                A_new = A[:i+1]
                B_new = B[:i+1]

                n = self.check_similarity(A_new, B_new)

                C.append(n)

        return C

    def check_similarity(self,A,B):
        return len(set(A) & set(B))