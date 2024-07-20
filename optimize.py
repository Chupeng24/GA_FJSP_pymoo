from pymoo.core.problem import ElementwiseProblem
from uniform_instance import *
from Params import *
from FJSP_Problem import FJSP
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.rnsga2 import RNSGA2
from FJSP_operator import *
from pymoo.optimize import minimize
from pymoo.termination import get_termination
import copy
import time
import hvwfg
from pymoo.operators.selection.rnd import RandomSelection
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.algorithms.moo.unsga3 import UNSGA3
from pymoo.algorithms.moo.moead import MOEAD
from pymoo.algorithms.moo.age import AGEMOEA
from pymoo.indicators.hv import Hypervolume
import matplotlib.pyplot as plt
from pymoo.decomposition.tchebicheff import Tchebicheff
from pymoo.algorithms.moo.rvea import RVEA
from FJSP_initialization import FJSP_initial
from pymoo.algorithms.soo.nonconvex.ga import GA
import pandas as pd
from FJSP_operator import *
from utils import *
import matplotlib as mpl

mpl.use('Agg')



def setup_seed(seed):
    np.random.seed(seed)
    random.seed(seed)


def opt_run(n_j, n_m, opt_target, save):
    test_data = FJSPDataset(n_j, n_m, configs.low, configs.high, 1, 200)
    data_loader = iter(test_data)

    setup_seed(200)

    res_list = []
    spend_time_list = []

    for i in range(test_data.size):
        ins_data = next(data_loader)
        t1 = time.time()

        termination = get_termination("n_gen", 100)
        # termination = get_termination("time", f"00:00:20")
        problem = FJSP(ins_data, opt_target)

        Pop_size = 100
        # X = GS_initial(problem, Pop_size, problem.os_list)
        # X = FJSP_initial(problem, Pop_size, 0, 0, 1)
        # X = FJSP_initial(problem, Pop_size, 0.5, 0.3, 0.2)
        # X = FJSP_initial(problem, Pop_size, 0.1, 0, 0.9)
        X = FJSP_initial(problem, Pop_size, 0.5, 0.3, 0.2)

        algorithm = GA(pop_size=100,
                       sampling=X,
                       crossover=FJSP_Crossover(pc=0.8, problem=problem),
                       mutation=FJSP_Mutation(pm=0.05, problem=problem),
                       eliminate_duplicates=True)
        res = minimize(problem,
                       algorithm,
                       termination,
                       save_history=True,
                       verbose=False)

        hist = res.history
        n_iter = []  # corresponding number of function evaluations\
        hist_F = []  # the objective space values in each generation

        for idx, algo in enumerate(hist):
            n_iter.append(idx)
            opt = algo.opt
            hist_F.append(opt.get("F"))
        
        hist_res_list = [_F[0] for _F in hist_F]
        plt.figure(figsize=(7, 5))
        plt.plot(n_iter, hist_res_list, color='black', lw=0.7, label="best res of Pop")
        plt.title("Convergence")
        plt.xlabel("Function iteration")
        plt.ylabel(opt_target)
        plt.show()
        plt.savefig('1.png')

        F = res.F[0]
        t2 = time.time()

        res_list.append(F)
        spend_time_list.append(t2-t1)



    print("opt target:", opt_target)
    print("mean result:", np.mean(res_list))
    print("mean spend time:", np.mean(spend_time_list))

    return np.mean(spend_time_list)

    # if save == True:
        # save_dict = {}
        # save_dict["GA"] = res_list
        # save_dict["time"] = spend_time_list
        # df = pd.DataFrame(save_dict)
        # df.to_csv(f"GA_{opt_target}_{n_j}x{n_m}_result_new.csv")









def solve_ins(ins_data, opt_target='makespan'):

    t1 = time.time()
    problem = FJSP(ins_data, opt_target=opt_target, public=True)
    termination = get_termination("n_gen", 100)
    Pop_size = 100
    # X = FJSP_initial(problem, Pop_size, 0.5, 0.3, 0.2)
    X = FJSP_initial(problem, Pop_size, 0.1, 0, 0.9)
    algorithm = GA(pop_size=100,
                   sampling=X,
                   crossover=FJSP_Crossover(pc=0.8, problem=problem),
                   mutation=FJSP_Mutation(pm=0.05, problem=problem),
                   eliminate_duplicates=True)
    res = minimize(problem,
                   algorithm,
                   termination,
                   save_history=True,
                   verbose=False)

    t2 = time.time()
    spend_time = t2 - t1
    res =  res.F[0]
    return res, spend_time


def sovle_instance_set(ins_set_path, ins_name_list, save_dict, opt_target):
    for ins_name in ins_name_list:
        ins_path = os.path.join(ins_set_path, ins_name)
        ins_data = getdata(ins_path)

        list_name = f'{ins_name[:-4]}'
        if ins_set_path[16:22] == 'Hurink':
            list_name = f'{ins_set_path[23]}data_{list_name}'



        res, spend_time = solve_ins(ins_data, opt_target=opt_target)
        save_dict[f"GA-{opt_target}"].append(res)

        if opt_target == "makespan":
            save_dict['ins_name'].append(list_name)
            save_dict['spend_time'].append(spend_time)

        print(f'test on {ins_name} instance,', f'{opt_target} res: {res}', f'spend time is {spend_time}')





