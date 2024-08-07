class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for sw in sandwiches:
            i = 0
            while i < len(students) and sw != students[i]:
                i +=1
            if i == len(students):
                return len(students)
            else:
                students.pop(i)
        return len(students)