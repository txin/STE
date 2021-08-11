# Default parameters
DEFAULT_par_lambda = 64 # operation capacity
DEFAULT_l = 512 # max tuple length
DEFAULT_k = 256 # label size: 32 bytes in bits
DEFAULT_N = 65536 # total number of values
DEFAULT_v = 64 # value size: 8 bytes in bits
DEFAULT_n = 8192 # total number of AVLH bins
DEFAULT_t = 256 # total number of labels
DEFAULT_N_lambda = 65600 # N for updated MM
DEFAULT_n_lambda = 8199 # n for update MM
DEFAULT_PAR_GATES = 2.5 # used as a constant to compute number of gates for oblivious sorting
DEFAULT_growth_factor = 25 # upper-bound EMM for ORAM simulation

def PrintParameters():
    print("lambda=%d, k=%d, N=%d" % (DEFAULT_par_lambda, DEFAULT_k, DEFAULT_N))
    print("v=%d, n=%d, t=%d" % (DEFAULT_v, DEFAULT_n, DEFAULT_t))
    print("N_lambda=%d, n_lambda=%d" % (DEFAULT_N_lambda, DEFAULT_n_lambda))
    
