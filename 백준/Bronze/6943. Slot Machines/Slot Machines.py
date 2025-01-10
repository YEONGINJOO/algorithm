def martha_slots(quarters, plays1, plays2, plays3):
    total_plays = 0
    
    while quarters > 0:
        # 첫 번째 머신
        total_plays += 1
        quarters -= 1
        plays1 += 1
        if plays1 == 35:
            quarters += 30
            plays1 = 0
        
        if quarters <= 0:
            break
        
        # 두 번째 머신
        total_plays += 1
        quarters -= 1
        plays2 += 1
        if plays2 == 100:
            quarters += 60
            plays2 = 0
        
        if quarters <= 0:
            break
        
        # 세 번째 머신
        total_plays += 1
        quarters -= 1
        plays3 += 1
        if plays3 == 10:
            quarters += 9
            plays3 = 0
            
    return total_plays

quarters = int(input())
plays1 = int(input())
plays2 = int(input())
plays3 = int(input())

total_plays = martha_slots(quarters, plays1, plays2, plays3)
print(f"Martha plays {total_plays} times before going broke.")