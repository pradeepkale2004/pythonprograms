"https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python"

alphabet='abcdefghijklmnopqrstuvwxyz'
def is_pangram(st):
    st=st.lower()
    for char in alphabet:
        if char not in st:
            return False

    return True
pangram = "The quick brown fox jumps over the lazy dog."
print(is_pangram(pangram))