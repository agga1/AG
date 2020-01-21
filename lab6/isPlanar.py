from typing import List
from lab6.TTNode import TTNode


def isPlanar(vs: List[int], T: List[TTNode]) -> bool:
    # vs - lista wierzcholkow w kolejnosci odwiedzenia przez DFS
    # T  - tablica zawierajaca wezly drzewa Tremaux odpowiadajace danemu wierzcholkowi

    # Initialize the constraints data structure for back edges
    CS = {}
    for v in vs:
        for u in T[v].back:
            e = (v, u)
            CS[e] = [([e], [])]

    # Auxiliary function putting all the empty stacks at specified index
    def putEmptyAt(c, at):
        for i, S in enumerate(c):
            Sa = S[1 - at]
            Sb = S[at]
            if not Sa and Sb:
                c[i] = (Sa, Sb) if at == 0 else (Sb, Sa)

    # Process vertices in reverse topological order - children before parents
    for v in reversed(vs[1:]):
        p = T[v].parent
        e = (p, v)

        if not T[v].out:
            CS[e] = []
            continue

        e1 = (v, T[v].out[0])
        CS[e] = CS[e1]

        def lowerInc(e):
            return T[e[1]].idx

        for u in T[v].out[1:]:
            f = (v, u)

            if not CS[f]:
                continue

            a = min(lowerInc(S[0]) for S in CS[e][0] if S)
            b = min(lowerInc(S[0]) for S in CS[f][0] if S)

            for j, c in enumerate(CS[e]):
                top = max(lowerInc(S[-1]) for S in c if S)
                if top > b:
                    break
            else:
                j += 1

            # Constraint satisfiability checks
            if j < len(CS[e]):
                (S0, S1) = CS[e][j]
                tops = [lowerInc(S[-1]) > b if S else False for S in CS[e][j]]

                # Only one of S0, S1 can have edges with lower incidence > b
                if all(tops):
                    return False

                # ... and we want that one to be first, flip the pair if necessary
                if tops == [False, True]:
                    (A, B) = CS[e][j]
                    CS[e][j] = (B, A)

                for (A, B) in CS[e][j + 1:]:
                    if A and B:
                        return False

                Sj0 = CS[e][j][0]
                for (A, _) in CS[e][j + 1:]:
                    Sj0 += A

                CS[e] = CS[e][:j + 1]

            bottom = [lowerInc(S[0]) for S in CS[f][0] if S]
            q = 1 if a in bottom else 0
            putEmptyAt(CS[f], at=0)

            for qq in range(q, len(CS[f])):
                (A, B) = CS[f][qq]
                if A and B:
                    return False

            if q < len(CS[f]):
                if j >= len(CS[e]):
                    CS[e].append(([], []))

                Sj1 = CS[e][j][1]
                for (_, B) in CS[f][q:]:
                    Sj1 += B

            if q == 1:
                (S0, S1) = CS[e][0]
                S = S0 or S1
                S += CS[f][0][1]

        # Deleting
        if CS[e]:
            (S0, S1) = CS[e][-1]
            while S0 and S0[-1][1] == p:
                S0.pop()
            while S1 and S1[-1][1] == p:
                S1.pop()
            if not S0 and not S1:
                CS[e].pop()

    return True
