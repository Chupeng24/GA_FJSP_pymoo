from instance_hv_ref import *
import numpy as np
import random
import os
from optimize import *


if __name__ == "__main__":
    data_path_list = []
    # data_path_list.append(KHB_data_path)
    data_path_list.append(BR_data_path)
    data_path_list.append(Be_data_path)
    # data_path_list.append(DP_data_path)
    # data_path_list.append(HU_Rdata_path)
    # data_path_list.append(HU_Edata_path)
    # data_path_list.append(HU_Vdata_path)
    # data_path_list.append(Fat_data_path)

    target_list = ["makespan", "mean_tardiness", "key_workload"]
    # target_list = ["mean_tardiness", "key_workload"]

    save_res_dict = {'ins_name': [], 'spend_time': []}
    save_res_file_name = f'GA_benchmark_result_ls_0.1.csv'

    for target in target_list:
        print('=' * 60, f'optimize for {target}', '=' * 60)
        save_res_dict[f"GA-{target}"] = []
        np.random.seed(200)
        random.seed(200)

        for data_path in data_path_list:
            data_name_list = [f for f in os.listdir(data_path)]
            data_name_list.sort()
            sovle_instance_set(ins_set_path=data_path, ins_name_list=data_name_list, save_dict=save_res_dict, opt_target=target)



    df = pd.DataFrame(save_res_dict)
    df.to_csv(save_res_file_name)



