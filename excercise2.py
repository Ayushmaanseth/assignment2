
def thief_which(objects,max_weight,items):

    n = len(objects)
    weight = []
    for i in range(n):
        weight.append(objects[i][0])
    used_items = []
    w = max_weight
    
    for i in range(n):
        used_items.append(0)
    while w >= 0:
        
        if items[w] == -1:
            break
        used_items[items[w]] +=1
        w = w - weight[items[w]]
        
    return used_items    
    

def thief(objects,max_weight):
    
    weight = []
    values = []
    items = []
    items.append(-1)
    n = len(objects)
    
    for i in range(n):
        weight.append(objects[i][0])
        values.append(objects[i][1])
    
    dp = []
    for i in range(max_weight + 1):
        dp.append(0)
    
    for i in range(1,max_weight+1):
        items.append(items[i-1])
        ma = dp[i-1]
        for j in range(n):
            x = i - weight[j]
            if x >=0 and (dp[x] + values[j]) > ma:
                ma = dp[x] + values[j]
                items[i] = j
            dp[i] = ma
        
                
    return dp[max_weight],items

n,items = thief([(2,50),(3,100),(5,140)],17)

print(thief_which([(2,50),(3,100),(5,140)],17,items))
 

