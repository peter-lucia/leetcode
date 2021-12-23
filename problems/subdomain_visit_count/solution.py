class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # 1. build hashmap
        
        # google.mail.com -> 900
        # mail.com -> 900 + 1
        # com -> 900 + 50 + 1
        # yahoo.com -> 50
        # intel.mail.com -> 1
        # wiki.org -> 5
        # org -> 5
        
        lookup = defaultdict(int)
        for cpdomain in cpdomains:
            count, url = cpdomain.split(" ")
            count = int(count)
            domains = url.split(".")
            for i in range(len(domains)):
                # Note:
                # >>> ".".join(['a'])
                # 'a'
                # google.mail.com -> 900
                # mail.com -> 900
                # com -> 900
                key = ".".join(domains[i:])
                lookup[key] += count
        
        result = [f"{v} {k}" for k,v in lookup.items()]
        return result
        
        
        
        