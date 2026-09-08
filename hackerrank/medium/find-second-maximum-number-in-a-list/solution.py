if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    largest = None
    second = None 
    
    for i in arr:
        if largest is None or i > largest:
            second = largest
            largest = i
        elif i != largest:
            if second is None or i > second:
                second = i
    print(second)
        
                                    
    
                
            
  
