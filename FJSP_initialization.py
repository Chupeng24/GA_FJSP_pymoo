
import numpy as np
import random
import copy

def random_initial(problem, Pop_size):
    Pop = []
    for i in range(int(Pop_size)):
        Pop_i =[]
        random.shuffle(problem.os_list)
        Pop_i.extend(copy.copy(problem.os_list))
        ms =[]
        for i in problem.ms_list:
            ms.append(random.randint(0 , i -1))
        Pop_i.extend(ms)
        # Pop_i =Popi(self.args ,Pop_i ,self.J_site ,self.half_len_chromo)

        Pop.append(Pop_i)

    return Pop

def GS_initial(problem, Pop_size):
    Pop = []
    for i in range(int(Pop_size)):
        Machine_load =[0] * problem.args.m
        Job_op =[0] * problem.args.n
        Pop_i = []
        random.shuffle(problem.os_list)
        Pop_i.extend(copy.copy(problem.os_list))
        ms =[0] *len(Pop_i)
        for pi in Pop_i:
            MLoad_op =[Machine_load[problem.args.Processing_Machine[pi][Job_op[pi]][_] - 1] +
                      problem.args.Processing_Time[pi][Job_op[pi]][_]
                      for _ in range(len(problem.args.Processing_Machine[pi][Job_op[pi]]))]
            m_idx =MLoad_op.index(min(MLoad_op))
            ms[problem.J_site.index((pi ,Job_op[pi])) ] =m_idx
            Machine_load[m_idx] =min(MLoad_op)
            Job_op[pi]+=1
        Pop_i.extend(ms)

        Pop.append(Pop_i)
    return Pop

def LS_initial(problem, Pop_size):
    ms =[]
    for PTi in problem.PT:
        for PTj in PTi:
            ms.append(PTj.index(min(PTj)))
    Pop = []
    for i in range(int(Pop_size)):
        Pop_i = []
        random.shuffle(problem.os_list)
        Pop_i.extend(copy.copy(problem.os_list))
        Pop_i.extend(ms)

        Pop.append(Pop_i)
    return Pop
def FJSP_initial(problem, pop_size, p_GS, p_LS=0, p_RS=None):
    if p_RS == None:
        p_RS = 1 - (p_GS + p_LS)
    assert p_GS + p_LS + p_RS == 1, "init ratio is wrong"

    pop_GS = int(pop_size * p_GS) if (pop_size * p_GS) % 1 == 0 else int(pop_size * p_GS) + 1
    pop_LS = int(pop_size * p_LS) if (pop_size * p_LS) % 1 == 0 else int(pop_size * p_LS) + 1
    pop_RS = pop_size - (pop_GS + pop_LS)

    assert pop_GS + pop_LS + pop_RS >= pop_size, "init ratio is wrong"

    Pop = []
    Pop_GS = GS_initial(problem, pop_GS)
    Pop_LS = LS_initial(problem, pop_LS)
    Pop_RS = random_initial(problem, pop_RS)
    Pop.extend(Pop_GS)
    Pop.extend(Pop_LS)
    Pop.extend(Pop_RS)

    return np.array(Pop)



