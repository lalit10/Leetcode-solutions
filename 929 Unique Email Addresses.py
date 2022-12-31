class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        store = {}
        for email in emails:
            local_name, domain_name = email.split('@')            
            if "." in local_name:
                local_name = local_name.replace(".", "")
                #print("Local name is", local_name)
            if "+" in local_name:
                local_name = local_name.split("+")[0]
            updated_email = local_name + '@' + domain_name
            if updated_email not in store:
                store[updated_email] = 1
        return len(store)