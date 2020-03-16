class node:
    def __init__(self):
        self.keys=[]
        self.children=[]
        self.leaf=True
        self.parent=None
class BTree:
    def __init__(self):
        self.root=node()
    def search(self,data1):
        return(self._search(data1,self.root))
    def _search(self,data2,curr):
        for i in curr.keys:
            if i<data2:
                if curr.keys[-1]<data2:
                    return(self._search(data2,curr.children[-1]))
            elif i==data2:
                return(curr,curr.keys.index(i))
            else:
                return(self._search(data2,curr.children[curr.keys.index(i)]))
    def _ins_srch(self,data4,curr):
        if curr.leaf is True:
            return(curr)
        for i in curr.keys:
            if i<data4:
                if curr.keys[-1]<data4:
                    return(self._ins_srch(data4,curr.children[-1]))
            else:
                return(self._ins_srch(data4,curr.children[curr.keys.index(i)]))
    def insert(self,data5):
        curr=self._ins_srch(data5,self.root)
        self._insert(data5,curr)
    def _insert(self,data6,curr):
        if len(curr.keys)<3:
            curr.keys.append(data6)
            curr.keys.sort()
        else:
            curr.keys.append(data6)
            curr.keys.sort()
            self.split(curr)
    def split(self,curr):
        if curr.parent is None:
            curr.parent=node()
            curr.parent.keys.append(curr.keys[2])
            left=node()
            left.keys+=curr.keys[0:2]
            left.parent=curr.parent
            right=node()
            right.keys.append(curr.keys[3])
            right.parent=curr.parent
            left.keys.sort()
            right.keys.sort()
            curr.parent.children.append(left)
            curr.parent.children.append(right)
            curr.parent.leaf=False
            self.root=curr.parent
        else:
            i=curr.parent.children.index(curr)
            curr.parent.children.pop(i)
            self._insert(curr.keys[2],curr.parent)
            left=node()
            left.keys+=curr.keys[0:2]
            left.parent=curr.parent
            right=node()
            right.keys.append(curr.keys[3])
            right.parent=curr.parent
            curr.parent.children.insert(i,left)
            curr.parent.children.insert(i+1,right)
            curr.parent.leaf=False
    def succ(self,data7):
        curr,i=self.search(data7)
        if curr.leaf is not True:
            x=curr.children[i+1]
            return(x.keys[0])
        else:
            if i<len(curr.keys):
                return(curr.parent.keys[curr.parent.children.index(curr)])
            else:
                return(curr.keys[i+1])
    def pred(self,data8):
        curr,i=self.search(data8)
        if curr.leaf is not True:
            x=curr.children[i]
            return(x.keys[-1])
        else:
            if i>0:
                return(curr.keys[i-1])
            else:
                return(curr.parent.keys[curr.parent.children.index(curr)-1])
    def delete(self,data9):
        curr,i=self._search(data9)
        if curr.leaf is True:
            if len(curr.keys)>1:
                curr.keys.pop(i)
            else:
                if curr.parent.children[i]
b1=BTree()
b1.insert(1)
b1.insert(3)
b1.insert(5)
b1.insert(7)
b1.insert(-5)
b1.insert(-10)
b1.insert(10)
b1.insert(4)
b1.insert(0)
b1.insert(11)
b1.insert(4.5)
b1.insert(12)
#print(b1.root.keys)
#x=b1.root.children[0]
#y=b1.root.children[1]
#z=b1.root.children[2]
#w=b1.root.children[3]
#print(x.keys+['/']+y.keys+['/']+z.keys+['/']+w.keys)
print(b1.succ(12))
