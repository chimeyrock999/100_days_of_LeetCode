class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for sw in sandwiches:
            if counter[sw] == 0:
                break
            else:
                counter[sw] -= 1
        return counter[0] + counter [1]
        