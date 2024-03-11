import random
import string

def generate_random_string(length):
    """Generate a random string of given length."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_isomorphic_pair(length, mapping=None):
    """Generate an isomorphic pair of strings of given length with manual mapping."""
    str1 = generate_random_string(length)
    if mapping is None:
        mapping = {}
        for char in str1:
            # Generate a random character for each unique character in str1
            random_char = random.choice(string.ascii_lowercase.replace(char, ''))
            mapping[char] = random_char
    str2 = ''.join(mapping.get(char, random.choice(string.ascii_lowercase.replace(char, ''))) for char in str1)
    return str1, str2, mapping

# Manual Mapping
manual_mapping = {
    'a': 'r',
    'b': 'z',
    'c': 'h',
    'd': 'e',
    'e': 'n',
    'f': 'g',
    'g': 'x',
    'h': 'p',
    'i': 'v',
    'j': 'j',
    'k': 'm',
    'l': 'd',
    'm': 'o',
    'n': 'f',
    'o': 'c',
    'p': 'l',
    'q': 'i',
    'r': 's',
    's': 'k',
    't': 'y',
    'u': 'u',
    'v': 'a',
    'w': 'w',
    'x': 'q',
    'y': 'b',
    'z': 't'
}


# Generate isomorphic pair with manual mapping
length = 10**4
# str1, str2, mapping = generate_isomorphic_pair(length, manual_mapping)
str1=generate_random_string(length)
str2=generate_random_string(length)

# Write to text file
filename = "testcase11.txt"
with open(filename, 'w') as file:
    file.write(f"{len(str1)} {len(str2)}\n")
    file.write(f"{str1} {str2}\n")
