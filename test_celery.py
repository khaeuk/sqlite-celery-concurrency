from celery import group, chain
from tasks import add, mul


def main():
    # print("Single example result :")
    # result = add.delay(4,4)
    # print(result.ready())

    '''
    A group calls a list of tasks in parallel, and it 
    returns a special result instance that lets you inspect 
    the results as a group, and retrieve the return values in order.
    '''
    print("Parallele example result : ")
    parallele_result = group( chain(add.s(i, i) | mul.s(i)) for i in range(10))().get()
    print(parallele_result)

if __name__=="__main__":
    main()