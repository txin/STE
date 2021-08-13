# python 3
# Implementing concrete bandwidth computation

import math # for log function
from Parameter import *

def Print(value, scheme_str, attribute, stage_str):
    print("%s %s %s: %.3f Mbits" % (scheme_str, attribute, stage_str, value))
    return value

def PrintInMbit(value, scheme_str, attribute, stage_str):
    result = value / 1000 / 1000
    print("%s %s %s: %.3f Mbits" % (scheme_str, attribute, stage_str, result))
    return result

# Why using t_star?
class StdEMM:
    def __init__(self, par_lambda = DEFAULT_par_lambda, l = DEFAULT_l, k = DEFAULT_k,
                 N = DEFAULT_N, v = DEFAULT_v, t = DEFAULT_t, N_lambda = DEFAULT_N_lambda):
        self.par_lambda = par_lambda
        self.l = l
        self.k = k
        self.N = N
        self.v = v
        self.t = t
        self.N_lambda = N_lambda
        self.l_lambda = self.l
        self.t_lambda = self.t
        self.t_star = self.t # ?
        
    def PrintClientState(self):
        state = (self.k + math.log2(self.t_star)) * self.t_lambda
        PrintInMbit(state, "StdEMM", "Client State", "Total")

    def PrintServerStorage(self):
        storage = self.N_lambda * (self.k + self.v)
        PrintInMbit(storage, "StdEMM", "Server State", "Total")
        
    def PrintBandwidth(self):
        bandwidth = self.par_lambda * self.l_lambda * (self.k + self.v)
        PrintInMbit(bandwidth, "StdEMM", "Bandwidth", "Total")

# Compute the bandwidth cost of blackbox simulation of Path ORAM
class BlackboxORAM:
    def __init__(self, growth_factor = DEFAULT_growth_factor,
                 par_lambda = DEFAULT_par_lambda, l = DEFAULT_l, k = DEFAULT_k, N = DEFAULT_N,
                 v = DEFAULT_v, t = DEFAULT_t):
        self.growth_factor = growth_factor
        self.par_lambda = par_lambda
        self.l = l
        self.k = k
        self.N = N
        self.v = v
        self.t = t
        self.l_star = self.l * growth_factor
        self.t_star = self.t * growth_factor
        self.N_star = self.N * growth_factor

    def PrintClientState(self):
        state = ((self.k + math.log2(self.t_star)) * self.t_star
                 + self.l_star * self.v * math.log2(self.t_star))
        PrintInMbit(state, "PathORAM", "Client State", "Total")

    def PrintServerStorage(self):
        storage = 5 * self.l_star * self.v * (2 * self.t_star - 1)
        PrintInMbit(storage, "PathORAM", "Server Storage", "Total")

    def PrintBandwidth(self):
        bandwidth = self.par_lambda * 10 * self.v * self.l_star * math.log2(self.t_star)
        PrintInMbit(bandwidth, "PathORAM", "Bandwidth", "Total")

# How to compute the number of gates used for oblivious sorting?
class ZAVLH:
    def __init__(self, par_gates = DEFAULT_PAR_GATES, par_lambda = DEFAULT_par_lambda, 
                 l = DEFAULT_l, k = DEFAULT_k, N = DEFAULT_N, v = DEFAULT_v, n = DEFAULT_n,
                 t = DEFAULT_t, N_lambda = DEFAULT_N_lambda, n_lambda = DEFAULT_n_lambda):
        self.par_gates = par_gates
        self.par_lambda = par_lambda
        self.l = l
        self.k = k
        self.N = N
        self.v = v
        self.n = n
        self.t = t
        self.N_lambda = N_lambda
        self.n_lambda = n_lambda
        self.l_lambda = self.l
        self.t_lambda = self.t
    
    def NumGates(self, x):
        num = x  * math.log2(x) * (math.log2(x) + 1) / 4.0
        return num
    
    def ClientStateOPS(self):
        state = (2 * self.k * (self.t + self.par_lambda)
                 + (self.k + math.log2(self.par_lambda)) * self.par_lambda
                 + (self.l + self.par_lambda) * self.v * math.log2(self.par_lambda))
        return state

    def ClientStateEandT(self):
        state = (self.k + math.log2(self.l_lambda)) * (self.t_lambda + self.par_lambda)
        return state

    def ClientStateSandS(self):
        state = 0
        return state

    def ClientStateUP(self):
        state = (2 * self.k * (self.t_lambda + self.par_lambda)
                 + (self.k + math.log2(self.par_lambda)) * self.par_lambda
                 + (self.l_lambda + self.par_lambda) * self.v * math.log2(self.par_lambda))
        return state

    def PrintClientState(self):
        state_OPS = PrintInMbit(self.ClientStateOPS(), "ZAVLH", "Client State", "OPS")
        state_EandT = PrintInMbit(self.ClientStateEandT(), "ZAVLH", "Client State", "E&T")
        state_SandS = PrintInMbit(self.ClientStateSandS(), "ZAVLH", "Client State", "S&S")
        state_UP = PrintInMbit(self.ClientStateUP(), "ZAVLH", "Client State", "UP")
        state_total = max(state_OPS, state_UP) + state_EandT + state_SandS
        Print(state_total, "ZAVLH", "Client State", "Total")
        return state_total

    def ServerStorageOPS(self):
        storage = (((self.N + self.par_lambda) * self.v + self.k * self.n)
                   + 5 * self.v * (2 * self.par_lambda - 1) * (self.l + self.par_lambda))
        return storage
    
    def ServerStorageEandT(self):
        storage = ((self.t + 2 * self.par_lambda) *
                   (2 * self.k + (self.l + self.par_lambda) * self.v))
        return storage

    def ServerStorageSandS(self):
        storage = 0
        return storage
    
    def ServerStorageUP(self):
        storage = (((self.N_lambda + self.par_lambda) * self.v
                    + self.k * self.n_lambda) + 5 * self.v * (2 * self.par_lambda - 1)
                   * (self.l_lambda + self.par_lambda))
        return storage

    def PrintServerStorage(self):
        storage_OPS = PrintInMbit(self.ServerStorageOPS(),
                                  "ZAVLH", "Server Storage", "OPS")
        storage_EandT = PrintInMbit(self.ServerStorageEandT(),
                                    "ZAVLH", "Server Storage", "E&T")
        storage_SandS = PrintInMbit(self.ServerStorageSandS(),
                                    "ZAVLH", "Server Storage", "S&S")
        storage_UP = PrintInMbit(self.ServerStorageUP(),
                                 "ZAVLH", "Server Storage", "UP")
        storage_total = max(storage_OPS, storage_UP) + storage_EandT + storage_SandS
        Print(storage_total, "ZAVLH", "Server Storage", "Total")
    
    def BandwidthOPS(self):
        bandwidth = (self.l * self.k + self.l
                     * ((self.N + self.par_lambda) * self.v / self.n)
                     + 10 * self.v * (self.l + self.par_lambda) * math.log2(self.par_lambda))
        bandwidth_total = self.par_lambda * bandwidth
        return bandwidth_total

    def BandwidthEandT(self):
        bandwidth = (self.l * (self.t + self.par_lambda)
                     * (self.k + (self.N + self.par_lambda) * self.v / self.n)
                     + 5 * self.v * (self.l + self.par_lambda) * self.par_lambda
                     * math.log2(self.par_lambda) + self.ServerStorageEandT())
        return bandwidth

    def BandwidthSandS(self):
        bandwidth = 4 * (2 * self.k + (self.l + self.par_lambda) * self.v)
        term_S_pow = self.NumGates(self.t + 2 * self.par_lambda)
        bandwidth_total = bandwidth * term_S_pow
        return bandwidth_total

    def BandwidthUP(self):
        bandwidth = (self.k * self.n_lambda +
                     math.log2((self.N_lambda + self.par_lambda) / self.n_lambda)
                     + 2 * self.l_lambda * (self.t_lambda + self.par_lambda)
                     * (self.k + (self.N_lambda + self.par_lambda) * self.v / self.n_lambda)
                     + self.ServerStorageEandT())
        return bandwidth

    def PrintBandwidth(self):
        bandwidth_OPS = PrintInMbit(self.BandwidthOPS(), "ZAVLH", "Bandwidth", "OPS")
        bandwidth_EandT = PrintInMbit(self.BandwidthEandT(), "ZAVLH", "Bandwidth", "E&T")
        bandwidth_SandS = PrintInMbit(self.BandwidthSandS(), "ZAVLH", "Bandwidth", "S&S")
        bandwidth_UP = PrintInMbit(self.BandwidthUP(), "ZAVLH", "Bandwidth", "UP")
        bandwidth_total = bandwidth_OPS + bandwidth_EandT + bandwidth_SandS + bandwidth_UP
        Print(bandwidth_total, "ZAVLH", "Bandwidth", "Total")

if __name__ == "__main__":
    growth_factor = DEFAULT_growth_factor

    PrintParameters()
    print("Growth Factor for ORAM Simulation=%.2f" % growth_factor)
    print("------------------------------------------------------------")
    
    zavlh = ZAVLH()
    zavlh.PrintClientState()
    zavlh.PrintServerStorage()
    zavlh.PrintBandwidth()
    print("------------------------------------------------------------")
    
    oram = BlackboxORAM()
    oram.PrintClientState()
    oram.PrintServerStorage()
    oram.PrintBandwidth()
    print("------------------------------------------------------------")
    
    std_emm = StdEMM()
    std_emm.PrintClientState()
    std_emm.PrintServerStorage()
    std_emm.PrintBandwidth()
