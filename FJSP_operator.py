import numpy as np
from pymoo.core.mutation import Mutation
from pymoo.core.crossover import Crossover
import random

class FJSP_Mutation(Mutation):

    def __init__(self, problem, pm=0.05):

        super().__init__()
        self.prob = pm
        self.FJSP_args = problem.args
        self.half_len_chromo = len(problem.os_list)
        self.J_site = problem.J_site

    def swap_mutation(self ,p):
        pos1 = random.randint(0, len(p) - 1)
        pos2 = random.randint(0, len(p) - 1)
        if pos1 == pos2:
            return p
        if pos1 > pos2:   # <柔性作业车间调度智能算法及应用>书中的互换变异
            pos1, pos2 = pos2, pos1
        offspring = p[:pos1] + [p[pos2]] + \
                    p[pos1 + 1:pos2] + [p[pos1]] + \
                    p[pos2 + 1:]
        return offspring

    def Mutation_Machine(self ,CHS):
        T_r = [j for j in range(self.half_len_chromo)]
        r = random.randint(1, self.half_len_chromo)  # 在区间[1,T0]内产生一个整数r
        random.shuffle(T_r)
        R = T_r[0:r]  # 按照随机数r产生r个互不相等的整数
        for i in R:
            O_site = self.J_site[i]
            pt = self.FJSP_args.Processing_Time[O_site[0]][O_site[1]]
            pt_find =pt[0]
            len_pt =len(pt ) -1
            k , m =1 ,0
            while k< len_pt:
                if pt_find > pt[k]:
                    pt_find = pt[k]
                    m = k
                k += 1
            CHS[i] = m
        return CHS

    def _do(self, problem, X, **kwargs):
        """
        TODO:
        :param problem:
        :param X: input sequence
        :param kwargs:
        :return: Y: sequence after mutation
        """
        Y = X.copy()
        for i, y in enumerate(X):
            if np.random.random() < self.prob:
                p11 = self.swap_mutation(list(y[0:self.half_len_chromo]))
                p12 = self.Mutation_Machine(list(y[self.half_len_chromo:]))
                p11.extend(p12)
                Y[i] = np.array(p11)
        return Y

class FJSP_Crossover(Crossover):

    def __init__(self, problem, pc, **kwargs):
        super().__init__(2, 2, **kwargs)
        self.pc = pc
        self.FJSP_args = problem.args
        self.half_len_chromo = len(problem.os_list)

    def POX(self ,p1, p2):
        jobsRange = range(0, self.FJSP_args.n)
        sizeJobset1 = random.randint(1, self.FJSP_args.n)
        jobset1 = random.sample(jobsRange, sizeJobset1)
        o1 = []
        p1kept = []
        for i in range(len(p1)):
            e = p1[i]
            if e in jobset1:
                o1.append(e)
            else:
                o1.append(-1)
                p1kept.append(e)
        o2 = []
        p2kept = []
        for i in range(len(p2)):
            e = p2[i]
            if e in jobset1:
                o2.append(e)
            else:
                o2.append(-1)
                p2kept.append(e)
        for i in range(len(o1)):
            if o1[i] == -1:
                o1[i] = p2kept.pop(0)
        for i in range(len(o2)):
            if o2[i] == -1:
                o2[i] = p1kept.pop(0)
        return o1, o2

    def Job_Crossover(self ,p1 ,p2):
        jobsRange = range(0, self.FJSP_args.n)
        sizeJobset1 = random.randint(0, self.FJSP_args.n)
        jobset1 = random.sample(jobsRange, sizeJobset1)
        jobset2 = [item for item in jobsRange if item not in jobset1]
        o1 = []
        p1kept = []
        for i in range(len(p1)):
            e = p1[i]
            if e in jobset1:
                o1.append(e)
                p1kept.append(e)
            else:
                o1.append(-1)
        o2 = []
        p2kept = []
        for i in range(len(p2)):
            e = p2[i]
            if e in jobset2:
                o2.append(e)
                p2kept.append(e)
            else:
                o2.append(-1)
        for i in range(len(o1)):
            if o1[i] == -1:
                o1[i] = p2kept.pop(0)
        for i in range(len(o2)):
            if o2[i] == -1:
                o2[i] = p1kept.pop(0)
        return o1 ,o2

    def Crossover_Machine(self, CHS1, CHS2):
        T_r = [j for j in range(self.half_len_chromo)]
        r = random.randint(1, self.half_len_chromo)  # 在区间[1,T0]内产生一个整数r
        random.shuffle(T_r)
        R = T_r[0:r]  # 按照随机数r产生r个互不相等的整数
        # 将父代的染色体复制到子代中去，保持他们的顺序和位置
        for i in R:
            K, K_2 = CHS1[i], CHS2[i]
            CHS1[i], CHS2[i] = K_2, K
        return CHS1, CHS2

    def _do(self, problem, X, **kwargs):
        """
            TODO:
            :param problem:
            :param X: input sequence
            :param kwargs:
            :return: Y: sequence after mutation
        """
        _, n_matings, n_var = X.shape
        Y = np.full((self.n_offsprings, n_matings, n_var), -1, dtype=int)

        for i in range(n_matings):
            p1, p2 = X[:, i, :]
            if random.random() < self.pc:
                p11, p21 = self.POX(p1[0:self.half_len_chromo], p2[0:self.half_len_chromo])
                p12, p22 = self.Crossover_Machine(p1[self.half_len_chromo:], p2[self.half_len_chromo:])
                p11.extend(p12)
                p1 = p11
                p21.extend(p22)
                p2 = p21

            Y[0, i, :] = np.array(p1)
            Y[1, i, :] = np.array(p2)

        return Y