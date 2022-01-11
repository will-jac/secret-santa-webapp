import random
from copy import deepcopy

# create the pairings

# second attempt: pool w/o own index
def do_pairing(size=10):
    pool = [i for i in range(size)]
    pairings = [None]*size
    for i in range(size):
        round_pool = deepcopy(pool)
        if i in round_pool:
            round_pool.remove(i)
        
        pairings[i] = random.sample(round_pool, 1)[0]
        pool.remove(pairings[i])
    
    return pairings

def check_for_loops(pairings):
    # start at 0, following the pairings (val->next index) 
    # until reach a value we've seen before
    size = len(pairings)
    seen = []
    i = 0
    while True:
        seen.append(i)
        i = pairings[i]
        if i in seen:
            # True if it's good
            return len(seen) == size

# just do the pairing and send the first good one w/o loops
def pair(size=10):
    for _ in range(100):
        try:
            p = do_pairing(size)
            if check_for_loops(p):
                return p
        except:
            continue
    return p


