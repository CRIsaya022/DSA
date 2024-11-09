ans = [] # to store valid states, Note: This can be a set() as well

def is_valid_state(state):
    # check if current state is a valid solution
    return True

# generate all possible candidates from the current state
def get_candidates(state):
    return []

# recursively explore all possible states
def backtrack(state):
    if is_valid_state(state):
        ans.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.append(candidate)
        backtrack(state)
        state.remove(candidate)

state = []
backtrack(state)

