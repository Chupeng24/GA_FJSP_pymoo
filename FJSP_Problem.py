import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist
import argparse
from Env_JSP_FJSP.Job_Shop import Job_shop
from pymoo.core.problem import ElementwiseProblem



class FJSP(ElementwiseProblem):

    def __init__(self, ins_data, opt_target, public=False, **kwargs):
        """
        TODO: Initialize MOFJSP 1. Put public things here
        """
        # n_cities, _ = cities.shape
        #
        # self.cities = cities
        # self.D = cdist(cities, cities)
        if public == True:
            n, m, PT, MT, ni, mm = self.data_trans_benchmark(input_data=ins_data)
        else:
            n, m, PT, MT, ni, mm = self.data_trans(input_data=ins_data)
        args = self.get_args(n, m, PT, MT, ni, mm)
        self.args = args
        self.JS = Job_shop(args)
        self.PT = PT
        self.MT = MT
        self.num_ope = sum(ni)
        self.m = m
        self.n = n
        self.nums_ope = ni
        self.mm = mm
        self.opt_target = opt_target

        self.os_list = []
        for i in range(len(self.nums_ope)):
            self.os_list.extend([i for _ in range(self.nums_ope[i])])

        self.ms_list = []
        self.J_site = []  # 方便后面的位置查找
        for i in range(len(self.MT)):
            for j in range(len(self.MT[i])):
                self.ms_list.append(len(self.MT[i][j]))
                self.J_site.append((i, j))  # 保存工件序号和工序相对序号

        self.l1 = self.num_ope

        super(FJSP, self).__init__(
            n_var=self.num_ope*2,
            n_obj=1,
            vtype=int,
            **kwargs
        )

    def _evaluate(self, x, out, *args, **kwargs):
        """
        TODO:
        :param x:  FJSP code
        :param out: three obj value, makespan, total machine load, key machine load
        :param args:
        :param kwargs:
        :return:
        """
        # out['F'] = self.get_route_length(x)
        fitness = self.decode(x)
        out['F'] = fitness

    def decode(self, CHS):
        self.JS.reset()
        for i in range(self.l1):
            O_num=self.JS.Jobs[CHS[i]].cur_op
            m_idx=self.J_site.index((CHS[i], O_num))
            self.JS.decode(CHS[i], CHS[m_idx+self.l1])

        tardiness_list = []
        for i in range(self.n):
            job_end_time = max(self.JS.Jobs[i].end)
            tardiness = job_end_time - self.JS.Jobs[i].due_date
            tardiness = tardiness if tardiness > 0 else 0
            tardiness_list.append(tardiness)
        tardiness_array = np.array(tardiness_list)

        if np.any(tardiness_array) == True:
            mean_tardiness = np.mean(tardiness_array)
        else:
            mean_tardiness = 0

        # if type(mean_tardiness) == 'NoneType':
        #     print("sssss")
        # if mean_tardiness == np.array(None):
        #     print("sssss")

        if self.opt_target == "makespan":
            return self.JS.C_max
        elif self.opt_target == "mean_tardiness":
            return mean_tardiness
        elif self.opt_target == "key_workload":
            return self.JS.max_load

    def data_trans(self, input_data):
        n = input_data.shape[0]
        m = input_data.shape[2]
        ni = []
        for i in range(n):
            ni.append(input_data.shape[1])

        PT = [[[] for _ in range(ni[i])] for i in range(n)]
        MT = [[[] for _ in range(ni[i])] for i in range(n)]
        for i in range(n):
            for j in range(ni[i]):
                for k in range(m):
                    if input_data[i][j][k] > 0:
                        MT[i][j].append(k + 1)
                        PT[i][j].append(input_data[i][j][k])

        mm = 2
        return n, m, PT, MT, ni, mm

    def get_args(self, n, m, PT, MT, ni, means_m=1):
        parser = argparse.ArgumentParser()
        # params for FJSPF:
        parser.add_argument('--n', default=n, type=int, help='job number')
        parser.add_argument('--m', default=m, type=int, help='Machine number')
        parser.add_argument('--O_num', default=ni, type=list, help='Operation number of each job')
        parser.add_argument('--Processing_Machine', default=MT, type=list, help='processing machine of operations')
        parser.add_argument('--Processing_Time', default=PT, type=list, help='processing machine of operations')
        parser.add_argument('--means_m', default=means_m, type=float, help='avaliable machine')

        args = parser.parse_args()
        return args

    def data_trans_benchmark(self, input_data):
        n = input_data['n']
        m = input_data['m']
        ni = []
        for i in range(n):
            ni.append(len(input_data['OJ'][i + 1]))

        PT = [[[] for _ in range(ni[i])] for i in range(n)]
        MT = [[] for i in range(n)]

        for i in range(n):
            for j in range(ni[i]):
                MT[i].append(input_data['operations_machines'][(i + 1, j + 1)])

        for i in range(n):
            for j in range(ni[i]):
                for idx, k in enumerate(MT[i][j]):
                    PT[i][j].append(input_data['operations_times'][(i + 1, j + 1, k)])
        mm = 2
        return n, m, PT, MT, ni, mm
