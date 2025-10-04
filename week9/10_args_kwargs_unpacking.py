def kwargs(*args, **kwargs):
    print("name:", kwargs)


kwargs(galleons=100, sickles=50, knuts=25)


def args(*args, **kwargs):
    print("name:", args)


args(10, 20, 30)
