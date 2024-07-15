
from optimize import *
from datetime import datetime

if __name__ == "__main__":

    job_size = [6, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    mch_size = [6, 10, 15, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    column_list = []
    for n_j, n_m in zip(job_size, mch_size):
        column_list.append(n_j * n_m)
    res_dict = {}
    res_dict["size"] = column_list
    opt_target = "makespan"
    time_list = []
    for n_j, n_m in zip(job_size, mch_size):
        mean_spend_time = opt_run(n_j, n_m, opt_target, True)
        time_list.append(mean_spend_time)

    res_dict["GA"] = time_list
    df = pd.DataFrame(res_dict)
    df.to_csv(f'GA_time_res.csv')


