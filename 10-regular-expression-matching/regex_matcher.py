from string import ascii_lowercase

class _Node:
    def __init__(self, is_accepting: bool):
        self.is_accepting = is_accepting
        self.edges = []

class regex_matcher:
    def isMatch(self, s: str, p: str) -> bool:
        possible_states = []
        possible_states.append((self.construct_regex(p), 0))
        
        # loop through all possible states (is is a NFA, so multiple states are possible)
        while len(possible_states) > 0:
            state, index = possible_states.pop()
            # test if we reached the input end and are in an accepting state
            if index == len(s) and state.is_accepting:
                return True
            
            # progress through the states
            for edge in state.edges:
                if index < len(s) and s[index] in edge['pattern']:
                    # this edge accepts the pattern, so add it to the next possible states
                    possible_states.append((edge['node'], index+1))
                if '_' in edge['pattern']:
                    possible_states.append((edge['node'], index))
            
        return False

    def construct_regex(self, pattern: str) -> _Node:
        start = _Node(is_accepting=False)
        prev = start
        
        for i in range(len(pattern)):
            n = _Node(is_accepting=False)
            edge = {"node": n, "pattern": []}
            if pattern[i] == "*":
                edge['pattern'].append('_') # create an epsilon edge to the new node
            elif pattern[i] == ".":
                edge['pattern'].extend(list(ascii_lowercase))
            else:
                edge['pattern'].append(pattern[i])
                
            if (i+1) < len(pattern) and pattern[i+1] == '*':
                edge['node'] = prev
                n = prev
                
            prev.edges.append(edge)
            prev = n
            
        prev.is_accepting = True
        return start
