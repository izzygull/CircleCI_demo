"""
Random module for CircleCI tests
"""

class RandomModule:

    @staticmethod
    def adder(a=0,b=0):
        return a + b

if __name__ == "__main__":
    print('running...')
    print(RandomModule.adder(4,5))
    f = open('workspace/testfile.test', 'w')
    f.write("I am a file")
    f.close()
    print('ran...')
