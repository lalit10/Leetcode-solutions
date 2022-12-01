class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #Store losers in a dictionary with key as user value as no of loss
        store , win_store = {}, {}
        loss_1,loss_0 =[], []
        for win,loss in matches:
            if win in win_store:
                win_store[win]+=1
            else:
                win_store[win] =1
            if loss in store:
                store[loss] +=1
            else:
                store[loss] =1
        for key, value in store.items():
            if value ==1:
                loss_1.append(key)
        #print("Loss 1 is:", loss_1)
        win_keys = win_store.keys()
        loss_keys = store.keys()
        res = list(set(win_keys) - set(loss_keys))
        #print("Win keys are:-", res)
        return [sorted(res),sorted(loss_1)]
        