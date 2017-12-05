
A = [4, 6, 2, 2, 6, 6, 1]

def get_max(A):
    # A is the list
    N = len(A)
    mindic = {}
    maxdic = {}

    for num in range (0, N):
        value = A[N]

        if value not in mindic:
            mindic.update({value : N})


def main():
    print(get_max(A))

if __name__ == "__main__":
    main()