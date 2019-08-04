class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Rules: 
        # - everything after + sign should be ignored before @ symbol
        #       plucia+123@gmail.com is the same as plucia@gmail.com
        # - docs in the local name are ignored 
        #       p.lucia@gmail.com is the same as plucia@gmail.com
        result = set([])        
        for idx, email in enumerate(emails):
            email_split = email.split("@")
            local_name = email_split[0]
            domain_name = email_split[1]
            local_name = local_name.replace(".", "")
            if "+" in local_name:
                local_name = local_name[0:local_name.index("+")]
            result.add("{0}@{1}".format(local_name, domain_name))

        return len(result)