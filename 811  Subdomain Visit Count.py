class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = {}
        for i in cpdomains:
            n, domains = i.split()
            #print("N domains is:-", n, domains)
            n, domains = int( n ), domains.split( '.' )
            
            for j in range(len(domains)):
                temp = '.'.join( domains[j:] )
                if temp in store:
                    store[temp] = store[temp] + n 
                else:
                    store[temp] = n
        #print(store)
        result =[]
        for i in store:
            result.append(str(store[i]) + " " + i)
        return result