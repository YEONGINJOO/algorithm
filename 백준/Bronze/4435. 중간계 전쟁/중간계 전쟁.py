T = int(input())
for i in range(1, T+1):
    hobitt, human, elf, dwaf, eagle, magic = map(int, input().split())
    oak, human_1, wog, gobblin, woorughigh, troll, magic_1 = map(int, input().split())
    gandalf = hobitt + human * 2 + elf * 3 + dwaf * 3 + eagle * 4 + magic * 10
    sauron = oak + human_1 * 2 + wog * 2 + gobblin * 2 + woorughigh * 3 + troll * 5 + magic_1 * 10
    if gandalf > sauron:
        print(f'Battle {i}: Good triumphs over Evil')
    elif gandalf == sauron:
        print(f'Battle {i}: No victor on this battle field')
    else:
        print(f'Battle {i}: Evil eradicates all trace of Good')