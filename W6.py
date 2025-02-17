# 1-3 Blastoff countdown conditions
x = int(input("Enter a number: "))
y = int(input("Enter a decrease: "))
while (x > 0):
    if (x % 2 == 0):
        print(x, "is even")
    else:
        print(x, "is odd")
    x = x - y
print("blastoff!!")

# 4.1.2 Word length checker"
word = input("5.1.2 Enter a word: ")
word_count = 1

while True:
    if len(word) < 5:
        print("goodbye")
        break
    elif word_count > 5:
        print("loser")
        break
    else:
        print(word, 'has', len(word), 'letters')
        word = input("Enter a word: ")
        word_count += 1

# 5.
print(" ")
num = 10
while num <= 100:
    print(f"{num} {bin(num)} {hex(num)}")
    num += 1


# 6.
def print_stars_iterative(n):
    while n > 0:
        print('*' * n)
        n -= 1


def print_stars_recursive(n):
    if n <= 0:
        return
    print('*' * n)
    print_stars_recursive(n - 1)


# If the main script says: squarex(5)
print("\nIterative:")
print_stars_iterative(5)
print("\nRecursive:")
print_stars_recursive(5)
