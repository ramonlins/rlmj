import numpy as np

# TODO: Clean code, create a start state-acttion function, add docstring
class QL:
    def __init__(self):
        self.Q = {}
        self.df = 0.99
        self.lr = 0.01
        self.A = 4

    def _get_state(self, s):
        return (s[0], s[1])

    def _init_Q(self, s, r, a):
        self.Q[s] = self.Q.get(s, [r if i == a else 0.0 for i in range(self.A)])

    def action(self, o):
        s = self._get_state(o)

        p = np.random.random()

        if p >= 0.3 and s in self.Q:
            if self.Q[s] == [0.0, 0.0, 0.0, 0.0]:
                a = np.random.randint(0, self.A)
            else:
                a = np.argmax(self.Q[s])
        else:
            a = np.random.randint(0, self.A)

        return a

    def update(self, o, a, r, o_):
        s = self._get_state(o)
        s_ = self._get_state(o_)

        if s not in self.Q:
            self._init_Q(s, r, a)

        if s_ not in self.Q:
            self._init_Q(s_, r, a)

        self.Q[s][a] = self.Q[s][a] + self.lr * (r + self.df * max(self.Q[s_]) - self.Q[s][a])
