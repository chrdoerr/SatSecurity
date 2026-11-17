import numpy as np, itertools
def kalpha(data, level='ordinal'):
    """data: list of units, each a list of values (None = missing). Returns Krippendorff's alpha."""
    units=[[v for v in u if v is not None] for u in data]
    units=[u for u in units if len(u)>=2]
    vals=sorted({v for u in units for v in u}); idx={v:i for i,v in enumerate(vals)}; k=len(vals)
    o=np.zeros((k,k))
    for u in units:
        m=len(u)
        for a,b in itertools.permutations(range(m),2):
            o[idx[u[a]],idx[u[b]]]+=1.0/(m-1)
    n_c=o.sum(1); n=n_c.sum()
    def delta(c,kk):
        if level=='nominal': return 0.0 if c==kk else 1.0
        if level=='interval': return (vals[c]-vals[kk])**2
        if level=='ordinal':
            lo,hi=min(c,kk),max(c,kk)
            s=n_c[lo:hi+1].sum()-(n_c[lo]+n_c[hi])/2.0
            return s**2
    Dm=np.array([[delta(c,kk) for kk in range(k)] for c in range(k)])
    Do=(o*Dm).sum()/n
    De=(np.outer(n_c,n_c)*Dm).sum()/(n*(n-1))
    return 1-Do/De
