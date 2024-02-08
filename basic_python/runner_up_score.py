if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = set(arr)
    scores_list = sorted(list(unique_scores))
    print(scores_list[-2])
