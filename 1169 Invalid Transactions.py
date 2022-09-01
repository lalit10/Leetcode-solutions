class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        store = collections.defaultdict(list)   #Create a dictionary to store the names, transactions and indexes corresponding
        result = set()                    
        for i,t in enumerate (transactions):
            
            t_arr = t.split(",")
           
            name, time, amount, city = t_arr[0], int(t_arr[1]), int(t_arr[2]), t_arr[3]
            
            if amount > 1000:                  
                result.add((t,i))           #1st condition: if the amount is greater than 1000, add the transaction to the result set     
                 
            if name in store:                
                for tran, idx in store[name]: #Iterate through the transactions of the same name
                    t_arr = tran.split(",")
                    pname, ptime, pamount, pcity = t_arr[0], int(t_arr[1]), int(t_arr[2]), t_arr[3]  
                    if abs(time-ptime) <= 60 and pcity != city:  #2nd condition: if the time difference is less than 60 and the city is different, add the transaction to the result set
                        result.add((tran,idx))  #Keep indexes because of failing test cases
                        result.add((t,i))                    
            
            store[name].append((t,i))  
        return [ele[0] for ele in result]           #Return the transactions in the result set

#Another solution:

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        store = {}
        result = []
        for t in transactions:
            t_arr = t.split(",")
            name, time, amount, city = t_arr[0], int(t_arr[1]), int(t_arr[2]), t_arr[3]
            
            if time not in store:
                store[time] = {                      #Create a dictionary to store time, name and city
                    name: [city]
                }
            else:
                if name not in store[time]:
                    store[time][name]=[city]      #If name not in that time, add the name and city to the dictionary
                else:
                    store[time][name].append(city)  #If name in that time, add the city to the list
        
        for t in transactions:
            t_arr = t.split(",")
            #print("T_arr is:-", t_arr)
            name, time, amount, city = t_arr[0], int(t_arr[1]), int(t_arr[2]), t_arr[3]
            if amount > 1000:   #1st condition: if the amount is greater than 1000, add the transaction to the result set
                result.append(t)
                continue
            
            for i in range(time-60, time+61):  #Iterate over time - 60 to time + 61
                if i not in store:
                    continue
                if name not in store[i]:
                    continue
                if len(store[i][name]) > 1 or (store[i][name][0] != city):  #If number of cities more than 1 or the city is different, add the transaction to the result set
                    result.append(t)
                    break
            
        return result