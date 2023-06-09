import cv2

class Search:
    def __init__(self, img: list[list[list[int]]]) -> None:
        self.image = img
        [self.rows, self.cols] = img.shape
        
        
    def build(self, not_wall):
        self.graph = {}
        # not_wall = 150
        for row in range(len(self.image)):
            for column in range(len(self.image[row])):
                if  not_wall - 20 > self.image[row][column] or self.image[row][column] > not_wall + 20: 
                    t = (row, column)
                    if t in self.graph.keys():
                        if column-1 >= 0 and  (not_wall - 20 > self.image[row][column-1] or self.image[row][column-1] > not_wall + 20):
                            self.graph[t].append((row, column-1))  
                            
                        if column+1 < self.cols and  (not_wall - 20 > self.image[row][column+1] or self.image[row][column+1] > not_wall + 20):
                            self.graph[t].append((row, column+1))  
                            
                        if row-1 >= 0 and (not_wall - 20 > self.image[row-1][column] or self.image[row-1][column] > not_wall + 20):
                            self.graph[t].append((row-1, column))  
                                
                        if row+1 < self.rows and (not_wall - 20 > self.image[row+1][column] or self.image[row+1][column] > not_wall + 20):
                            self.graph[t].append((row+1, column))  
                                
                    else:
                        self.graph[t] = []
                        if column-1 >= 0 and (not_wall - 20 > self.image[row][column-1] or self.image[row][column-1] > not_wall + 20):
                            self.graph[t].append((row, column-1))  
                            
                        if column+1 < self.cols and (not_wall - 20 > self.image[row][column+1] or self.image[row][column+1] > not_wall + 20):
                            self.graph[t].append((row, column+1))  
                            
                        if row-1 >= 0 and (not_wall - 20 > self.image[row-1][column] or self.image[row-1][column] > not_wall + 20):
                            self.graph[t].append((row-1, column))  
                                
                        if row+1 < self.rows and (not_wall - 20 > self.image[row+1][column] or self.image[row+1][column] > not_wall + 20):
                            self.graph[t].append((row+1, column))  

                
                
    def has_path(self, source, dest):
        previous = {};
        found = False
        queue = [source]
        visited = set()
        
        if source[0] < 0 or source[1] < 0:
            print("No")
            return
        
        while len(queue) > 0:
            cur = queue.pop(0)
            
            if cur == dest:
                print("yes")
                found = True
                break
            
            for neighbour in self.graph[cur]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    previous[neighbour] = cur; 
        
        path = []
        if found:
            current = dest;
            while current != source:
                path.insert(0, current);
                current = previous[current];
            path.insert(0, source);
        
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        
        for i in path:
            self.image[i[0]][i[1]] = [252, 186, 3]
            for n in range(1,2):
                self.image[i[0]-n][i[1]] = [252, 186, 3]
                self.image[i[0]+n][i[1]] = [252, 186, 3]
                self.image[i[0]][i[1]-n] = [252, 186, 3]
                self.image[i[0]][i[1]+n] = [252, 186, 3]

        return self.image
        