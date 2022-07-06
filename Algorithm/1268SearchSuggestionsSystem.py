class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        x = []
        products.sort()
        for n in range(1, len(searchWord)+1):
            y = []
            # print(searchWord[0:n])
            for i in range(len(products)):
                # print(products[i])
                if searchWord[0:n] == products[i][0:n]:
                    y.append(products[i])
                    # print(y)
                    if len(y) == 3:
                        break
            x.append(y)
            # print(x)

        return x