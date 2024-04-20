def min_holes_to_block(n, A, B, sizes):
    
    sorted_sizes = sorted(sizes[1:], reverse=True)
    
    
    total_size = sum(sizes)
    

    holes_blocked = 0
    
    
    for size in sorted_sizes:
        if sizes[0] * A / total_size >= B:
            
            break
        total_size -= size
        holes_blocked += 1

    if sizes[0] * A / total_size < B:
        return -1  
    
    return holes_blocked

n, A, B = map(int, input().split())
sizes = list(map(int, input().split()))
print(min_holes_to_block(n, A, B, sizes))
