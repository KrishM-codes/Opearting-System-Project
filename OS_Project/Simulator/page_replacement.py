def removefarthest(frame,pgn):
    position=[]
    for i in frame:
        for j in pgn:
            if(i==j):
                position.append(pgn.index(j))
                break
    
    index = position.index(max(position))
    frame.pop(index)
    return frame

def optimalPageReplacement(pg,fn):
    np = len(pg)
    frame=[]
    frames= []
    hit = 0
    for i in range(np):
        if pg[i] in frame:  # check if page is in frame
            hit += 1        # if page found, hit count increases
        
        elif (len(frame)<fn):     #check if frame is not full
            frame.append(pg[i])   # if not full, add page to frame

        else:
            for j in frame:
                if j not in pg[i+1:]:
                    frame.remove(j)
                    break
            
            if(len(frame)<fn):
                frame.append(pg[i])
            else:
                frame = removefarthest(frame,pg[i+1:])
                frame.append(pg[i])
        
        frames.append(frame.copy())
    
    for i in frames:
        for j in range(fn-len(i)):
            i.append('-')

    return hit,frames

# pg = [4 , 7, 6, 1, 7, 6, 1, 2, 7, 2]
# fn = 3
# print(optimalPageReplacement(pg, fn))