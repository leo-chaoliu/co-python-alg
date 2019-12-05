def continute_test():
    print('continute_test starting in vivocity!!')

    for i in range(0,10):
        if i%2 == 0:
            print('odd '+str(i))
        elif i == 1:
            return
            print("Leo")
        else:
            print('even '+str(i))

    print('finished')


continute_test()