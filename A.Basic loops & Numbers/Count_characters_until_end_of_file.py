#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Using seek/ tell method

with open(file_name) as f1:      # open file in default read mode
    f1.seek(0, 2)                # move cursor to the end of the file (offset 0 from end)
    length = f1.tell()           # get current cursor position = file size in bytes
print("The length of file:", length)

