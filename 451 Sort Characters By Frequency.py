class Solution:
    def frequencySort(self, s: str) -> str:
        store = Counter(s)
        store_sorted = sorted(store, key=store.get, reverse=True)
        result = ""
        #print("Store is:-", store_sorted)
        for i in store_sorted:
            result = result + i*store[i]
        #print("Result is:", result)
        return result
       