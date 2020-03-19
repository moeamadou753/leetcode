class Solution:
    def groupThePeople(self, G: List[int]) -> List[List[int]]:
        """ Optimized solution 1:
            - Convert list to a set to remove duplicates of group sizes
            -
        """
        S, D = set(G), collections.defaultdict(list)
        for i, g in enumerate(G): D[g].append(i)
        return [D[i][i * j:i * (j + 1)] for i in S for j in range(G.count(i) // i)]

        """ Proposed solution:
            - The i'th element belongs to a group of size n
            - We will arrive at a solution by grouping together all of the indices with the same group size
            - Assuming valid input, we will always be able to evenly divide this into groups
        """
        # Optionally start by putting indices into a dictionary for clarity
#         size_index_mapping = {}
#         for i, item in enumerate(groupSizes):
#                 size_index_mapping[item].append(i)

#         res = []

#         for key in size_index_mapping:
#             for i in range (0, len(size_index_mapping[key]), key):
#                 group = []
#                 for j in range (i, i + key):
#                     print(f"j:{j} i:{i} key:{key}")
#                     group.append(size_index_mapping[key][j])
#                 res.append(group)

#         return res