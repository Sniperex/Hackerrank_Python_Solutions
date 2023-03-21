if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
scores=list(arr)
new_scores=set(scores)
new_scores1=sorted(new_scores, reverse= True)
print(new_scores1[1])