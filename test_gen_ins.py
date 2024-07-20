from optimize import *
from datetime import datetime


if __name__ == "__main__":
    job_size = [6, 10, 15, 20, 30, 40, 50]
    mch_size = [6, 10, 15, 20, 20, 20, 20]
    current_time = datetime.now().strftime("%m-%d-%H")
    print(current_time)
    # for n_j, n_m in zip(job_size, mch_size):

    opt_target = "makespan"
    opt_run(6, 6, opt_target, True)

    # opt_target = "mean_tardiness"
    # opt_run(10, 10, opt_target, True)

    # opt_target = "key_workload"
    # opt_run(10, 10, opt_target, True)