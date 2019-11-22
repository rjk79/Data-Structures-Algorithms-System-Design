st = [ ([''], {}), 
       (['let', 'x', '2', ''], {'x': 2})
d = {'x': 2
tokens = ['add', ''

(1:3:2) i = 1

# (let x 2 (add (let x 3 (let x 4 x)) x))



def evaluate(self, expression):
    st, d, tokens = [], {}, ['']

    def getval(x):
        # 2nd arg is default val
        return d.get(x, x)

    def evaluate(tokens):
        # add or mult
        if tokens[0] in ('add', 'mult'):
            tmp = map(int, map(getval, tokens[1:]))
            return str(tmp[0] + tmp[1] if tokens[0] == 'add' else tmp[0] * tmp[1])
        else: #let is token[0]
            for i in xrange(1, len(tokens)-1, 2):
                # bounds check
                if tokens[i+1]:
                    # for every val (e.g x), assign it to the val that follows
                    d[tokens[i]] = getval(tokens[i+1])
            return getval(tokens[-1])

    for c in expression:
        # only do something special if: ( ) ''
        if c == '(':
            if tokens[0] == 'let':
                evaluate(tokens)
                # store state
            st.append((tokens, dict(d)))
            # reset tokens
            tokens =  ['']
        elif c == ' ':
            tokens.append('')
        elif c == ')':
            # on our 1st encounter of ')' there will be nothing in "tokens" except the chars after the most recent "("
            val = evaluate(tokens)
            # use our stored state (includes tokens and dict)
            tokens, d = st.pop()
            tokens[-1] += val
        else:
            tokens[-1] += c
    return int(tokens[0])