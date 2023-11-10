import time
import User
import Graph

def main():
    print('test')
    g=Graph.Graph()
    g.printtest()
    u=User.User()
    u.printtest()

if __name__ == "__main__":
    start=time.process_time()
    main()
    print(time.process_time()-start)
