from sacred import Experiment
ex = Experiment('jupyter_ex', interactive=True)

@ex.main
def my_main():
    pass

if __name__ == '__main__':
    ex.run_commandline()