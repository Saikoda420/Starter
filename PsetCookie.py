class jar:
    def __init__(self):
        self.set = False
        self.n=0


    def deposit(self,num):
        self.n += num

    def capacity(self):
        print(f"90 cookies can be filled there and {90-self.n} more can be filled")

    def withdraw(self,how):
        self.n-=how

    def size(self):
        print(f"{self.n} cookies are filled there")
    
    def __str__(self):
        return "🍪"*self.n
    
    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, alu):
        if self.set:
            raise ValueError("No change pls cookie")
        self._n = alu
        self.set = True



def main():
    cookiejar = jar()
    cookiejar.deposit(7)
    cookiejar.withdraw(5)
    cookiejar.capacity()
    cookiejar.size()
    print(cookiejar)

main()