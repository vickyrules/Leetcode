class Solution:
    def countTime(self, time: str) -> int:
        
        ans = 1
        
        if time[4] == "?":
            ans *= 10
        
        if time[3] == "?":
            ans *= 6
        
        
        
        if time[1] == "?" and time[0] == "?":
            ans *= 24    
        else:
            if time[1] == "?":
                if time[0] == "2":
                    ans *= 4
                else:
                    ans *= 10
            
        
            if time[0] == "?":
                if time[1] < "4":
                    ans *= 3
                else:
                    ans *= 2
                
            
        return ans   
                    
        
        
            
        
            
            
            
        