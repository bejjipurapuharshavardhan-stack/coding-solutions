from itertools import product

def maximize_equation():
    K, M = map(int, input().split())
    
    lists = []
    for _ in range(K):
        elements = [int(x)**2 % M for x in input().split()[1:]]
        lists.append(elements)
        
    max_value = max(sum(combo) % M for combo in product(*lists))
    
    print(max_value)

if __name__ == '__main__':
    maximize_equation()
