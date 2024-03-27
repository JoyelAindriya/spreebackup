class a:
    def __init__(self) -> None:
        
        print(self.valiidate_data)

class b(a):
    def __init__(self) -> None:
        self.validated_data=[2,3,4]
        super().__init__()

ob=b()
