# 1.	Student Marks Analyzer
# ⦁	Input marks of students in 5 subjects using NumPy.
# ⦁	Find average, topper, and subject-wise highest marks.

import numpy as np

subjects = ["Python","Math","DSA","Electronics","Java"]

marks = [int(input(f"Enter {sub}'s mark:")) for sub in subjects]

avg = np.mean(marks)
topper = np.max(marks)
top_sub = subjects[np.argmax(marks)]

print("Average mark:",round(avg,2))
print("Topper mark:",int(topper))
print("Top subject mark:",top_sub)