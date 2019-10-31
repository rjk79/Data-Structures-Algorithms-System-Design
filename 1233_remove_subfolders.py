# 1233. Remove Sub-Folders from the Filesystem

# Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it.

# The format of a path is one or more concatenated strings of the form: 
# / followed by one or more lowercase English letters. 
# For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

def removeSubfolders(folder):
# brute force?
# run .include? on each el
# if an el includes another then it should be deleted

# sort in alphabetical order
# 

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]