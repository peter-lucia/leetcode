from collections import defaultdict
from itertools import combinations
import heapq
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        """
        # step 1) find each of user and website timestamp
        # joe: [(1, home)]..
        user_time_site = dict()
        for user, time, site in zip(username, timestamp, website):
            if user not in user_time_site:
                user_time_site[user] = [(time, site)]
            else:
                user_time_site[user].append((time, site))
                
        # step 2) sorted site by time
        # joe: [(1, home)] => joe : [home, about]
        for user , time_site in user_time_site.items():
            time_site.sort(key = lambda x : x[0])
            user_time_site[user] = [site for time,site in time_site]
        
        user_site = user_time_site
        site_sequence_count = defaultdict(int)
        
        # step 3) find all 3 sequence cobinations of site for all users
        # ("home", "about","career"): 2 
        for user , sites in user_site.items():
            combs = set(combinations(sites,3))
            for comb in combs:
                site_sequence_count[comb] += 1
            
        three_seq_count = []
        # step 4) get the max site seq visit using heap
        for site,seq_count in site_sequence_count.items():
            heapq.heappush(three_seq_count, (-seq_count, site))
        
        return heapq.heappop(three_seq_count)[1]  