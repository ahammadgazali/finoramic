class Solution:
    
    def pow(self, a, b, d):
        if b == 0:
            return (1 % d)
        if b == 1:
            return (a % d)
        net = self.pow(a,int(b/2), d)
        if (b % 2) == 0:
            return ((net % d) * (net % d)) % d
        else:
            if b > 0:
                return ((a % d) * (net % d) * (net % d)) % d
            else:
                return ((net % d) * (net % d)/x) % d