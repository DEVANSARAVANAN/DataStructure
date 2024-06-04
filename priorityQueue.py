
class priorityQUeue(object):

    def __init__(self):
        self.queue=[]
    
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def insert(self,data):
        self.queue.append(data)
    
    def isEmpty(self):
        return len(self.queue)==0

    
    def delete(self):
        try:
            max=0
            for i in range(len(self.queue)):
                if self.queue[i]>self.queue[max]:
                    max=i
            item=self.queue[max]
            del self.queue[max]
            return item

        except:
            print("Index error")
            exit()


if __name__== '__main__':
    
    queue=priorityQUeue()
    queue.insert(9)
    queue.insert(5)
    queue.insert(10)
    queue.insert(2)
    print(queue)
    while not queue.isEmpty():
        print(queue.delete())