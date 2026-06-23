# 1.	Student Marks Analyzer
# ⦁	Input marks of students in 5 subjects using NumPy.
# ⦁	Find average, topper, and subject-wise highest marks.

import numpy as np

subjects = ["Python","Math","DSA","Electronics","Java"]

marks = np.array([])
for i in subjects:
    subject_marks = int(input(f"Enter {i}'s mark:"))
    marks = np.append(marks,subject_marks)

avg = np.sum(marks)/5
sub_ws_hghst_mrk = np.sort(marks)
topper = sub_ws_hghst_mrk[4]

print("Average:",avg)
print("Topper:",int(topper))
print("subject-wise highest marks:",sub_ws_hghst_mrk)