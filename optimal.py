def read_input_from_file(filename):
    with open(filename, 'r') as file:
        # Read the lengths of str1 and str2 from the first line
        str_lengths = file.readline().strip().split()
        len_str1, len_str2 = map(int, str_lengths)
        # Read str1
        str1,str2 = file.readline().strip().split()
    return len_str1, len_str2, str1, str2


# Example usage:
len_str1, len_str2, str1, str2 = read_input_from_file("testcase11.txt")
n,m=len_str1,len_str2
s,t=str1,str2
map1 = []
map2 = []
for idx in s:
       map1.append(s.index(idx))
for idx in t:
       map2.append(t.index(idx))
if map1 == map2:
      print(True)
else:
      print(False)
