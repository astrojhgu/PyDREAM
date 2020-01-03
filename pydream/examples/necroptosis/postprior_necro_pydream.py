'''
Generated by pydream_it
PyDREAM run script for necro.py
'''
from pydream.core import run_dream
from pysb.simulator import ScipyOdeSimulator
import numpy as np
from pydream.parameters import SampledParam
from pydream.convergence import Gelman_Rubin
from scipy.stats import norm,uniform
from necro import model
import seaborn as sns
from matplotlib import pyplot as plt
import random
sns.set()
random.seed(0)
# sns.set_color_codes()
# sns.set_context("paper")
# DREAM Settings
# Number of chains - should be at least 3.
#Plotting the prior distributions
model_params_start =np.array([])

logps_vals = np.array([3.304257e-05, 0.009791216, 0.006110069,4.319219e-05, 0.004212645,1.164332e-05,
         0.02404257,3.311086e-05,0.04280399,2.645815e-05,0.01437707,
         0.2303744, 2.980688e-05, 0.04879773, 1.121503e-05, 0.001866713, 0.7572178, 1.591283e-05,
         0.03897146, 3.076363, 3.73486, 3.2162e-06, 8.78243e-05, 0.02906341,5.663104e-05, 0.02110469, 0.1294086,
         0.3127598, 0.429849, 2.33291e-06, 0.007077505, 0.6294062, 0.06419313,
         0.0008584654, 8.160445e-05, 4.354384e-06, 4.278903])


nonlogps_vals = 10 ** logps_vals
# print(nonlogps_vals)
# quit()

scaling = [3] * 37
idx = list(range(14, 51,1))
row = 8
col = 5
counter = 0
n = 10000

# f, axes = plt.subplots(row, col, figsize=(15, 10), sharex=True)
# # f.suptitle("Posterior Distributions from PyDREAM calibration of Necroptosis Model", fontsize="x-large")
# # for dim, param in enumerate(sampled_params_list):
#
# for r in range(row):
#     for c in range(col):
#         # data_uniform = uniform.rvs(size=n, loc=logps_vals[counter], scale=scaling[counter])
#         sns.distplot(norm.rvs(size=n, loc=logps_vals[counter], scale=scaling[counter]),color='red', ax=axes[r,c])
#
#         # axes.hist(norm.stats(loc=logps_vals[counter], scale=scaling[counter]), density=True, histtype='stepfilled', alpha=0.2)
#         axes[r, c].set_title(model.parameters[idx[counter]].name, fontdict={'fontsize':8})
#         # axes[r, c].set_ylim(0.0,0.6)
#         counter += 1
#
#         if counter >= len(idx):
#             break
#
# f.add_subplot(111, frameon=False)
# f.subplots_adjust(wspace=0.4)
# f.subplots_adjust(hspace=0.5)
# # hide tick and tick label of the big axes
# plt.tick_params(labelcolor='none', top='off', bottom='on', left='off', right='off')
# plt.grid(False)
# plt.xlabel("Log(Parameter value)", fontsize=14)
# plt.ylabel("Probability", fontsize=14, labelpad=15)
# # plt.title('Posterior Distributions from PyDREAM calibration of Necroptosis Model', fontsize=14)
# # plt.savefig('pars_dist_plot_necropriors1.pdf', format='pdf', bbox_inches="tight")
# plt.show()
#
# quit()

nchains = 3
# Number of iterations
niterations = 1000

#Initialize PySB solver object for running simulations.  Simulation timespan should match experimental data.
# tspan = np.linspace(0,1440, num=100)
# solver = ScipyOdeSimulator(model, tspan=tspan)
# parameters_idxs = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# rates_mask = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
# param_values = np.array([p.value for p in model.parameters])
#
# # USER must add commands to import/load any experimental data for use in the likelihood function!
# experiments_avg = np.load()
# experiments_sd = np.load()
# like_data = norm(loc=experiments_avg, scale=experiments_sd)
# # USER must define a likelihood function!
# def likelihood(position):
#     Y=np.copy(position)
#     param_values[rates_mask] = 10 ** Y
#     sim = solver.run(param_values=param_values).all
#     logp_data = np.sum(like_data.logpdf(sim['observable']))
#     if np.isnan(logp_data):
#         logp_data = -np.inf
#     return logp_data
#sampled priors
# logps0 = np.load('dreamzs_5chain_logps_chain2_0_50000.npy')
# logps1 = np.load('dreamzs_5chain_logps_chain2_0_50000.npy')
# logps2 = np.load('dreamzs_5chain_logps_chain2_0_50000.npy')
# logps3 = np.load('dreamzs_5chain_logps_chain2_0_50000.npy')
# logps4 = np.load('dreamzs_5chain_logps_chain2_0_50000.npy')
# print(logps0[45000:])
# quit()
#sampled params
#LOGPS
logps0 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_logps_chainnew_0_50000.npy')
logps1 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_logps_chainnew_1_50000.npy')
logps2 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_logps_chainnew_2_50000.npy')
logps3 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_logps_chainnew_3_50000.npy')
logps4 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_logps_chainnew_4_50000.npy')

p2logps0 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_logps_chainnew_0_50000.npy')
p2logps1 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_logps_chainnew_1_50000.npy')
p2logps2 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_logps_chainnew_2_50000.npy')
p2logps3 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_logps_chainnew_3_50000.npy')
p2logps4 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_logps_chainnew_4_50000.npy')

#CHAINS
chain0 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_sampled_params_chainnew_0_50000.npy')
chain1 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_sampled_params_chainnew_1_50000.npy')
chain2 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_sampled_params_chainnew_2_50000.npy')
chain3 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_sampled_params_chainnew_3_50000.npy')
chain4 = np.load('new_wseed_50000_6_29/newdreamzs_5chain_sampled_params_chainnew_4_50000.npy')

#CHAINS
p2chain0 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_sampled_params_chainnew_0_50000.npy')
p2chain1 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_sampled_params_chainnew_1_50000.npy')
p2chain2 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_sampled_params_chainnew_2_50000.npy')
p2chain3 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_sampled_params_chainnew_3_50000.npy')
p2chain4 = np.load('pydream_wvar_7_4_50000/p2newdreamzs_5chain_sampled_params_chainnew_4_50000.npy')

# print(logps0)
# print(logps0.shape)
# print(logps0.shape[0])
# quit()
# print(chain0)
# quit()
# print(chain0)
# print(logps0)
# quit()
# samples = np.concatenate(tuple([chain0, chain1, chain2]))

#CHAINS
logn0 = np.load('dreamzs_5chain_logps_chain_922_0_50000.npy')
logn1 = np.load('dreamzs_5chain_logps_chain_922_1_50000.npy')
logn2 = np.load('dreamzs_5chain_logps_chain_922_2_50000.npy')
logn3 = np.load('dreamzs_5chain_logps_chain_922_3_50000.npy')
logn4 = np.load('dreamzs_5chain_logps_chain_922_4_50000.npy')



total_iterations = chain0.shape[0]
iterations = logps0.shape[0]
burnin = int(total_iterations/2)
p2samples = np.concatenate((p2chain0[burnin:, :], p2chain1[burnin:, :], p2chain2[burnin:, :], p2chain3[burnin:, :], p2chain4[burnin:, :]))
samples = np.concatenate((chain0[burnin:, :], chain1[burnin:, :], chain2[burnin:, :], chain3[burnin:, :], chain4[burnin:, :]))
samples_nonlog = 10 ** samples

priors = np.concatenate((chain0[:, :], chain1[:, :], chain2[:, :], chain3[:, :], chain4[:, :]))
priors_nonlog = 10 ** priors
# print(len(chain0[:,0]))
# quit()


# plt.figure()
# plt.plot(iters, samples[:,0])
# plt.show()
# quit()
#
# plt.figure()
# plt.plot(iters, samples[:,0], color = 'b') #best
# plt.plot(iters, chain1[:,0], color = 'red')
# plt.plot(iters, chain2[:,0], color = 'k')
# plt.hist(chain0[:,0], bins = 25, color = 'b') # best
# plt.plot(iters, chain4[:,0], color = 'cyan')
# plt.xlabel("Likelihood", fontsize=14)
# plt.ylabel("Frequency", fontsize=14, labelpad=15)
# plt.show()
# quit()
#
iters = [i for i in range(50000)]
plt.figure()
plt.plot(iters, logn0[:,0], color = 'b')
# plt.figure()
plt.plot(iters, logn1[:,0], color = 'red')
# plt.xlabel("Iteration", fontsize=14)
# plt.ylabel("Likelihood", fontsize=14, labelpad=15)
# plt.figure()
plt.plot(iters, logn2[:,0], color = 'k')
# plt.xlabel("Iteration", fontsize=14)
# plt.ylabel("Likelihood", fontsize=14, labelpad=15)
# plt.figure()
plt.plot(iters, logn3[:,0], color = 'g') #best
# plt.xlabel("Iteration", fontsize=14)
# plt.ylabel("Likelihood", fontsize=14, labelpad=15)
# plt.figure()
plt.plot(iters, logn4[:,0], color = 'cyan')
# plt.xlabel("Iteration", fontsize=14)
# plt.ylabel("Likelihood", fontsize=14, labelpad=15)
plt.show()
quit()
# quit()
# print(priors)
# np.save('allchains50000neww.npy', priors)
# print(len(priors))
# quit()
# print(np.load('allchains10000new.npy'))

# quit()

# idx = list(range(14, 51,1))

# for dim, param in enumerate(sampled_params_list):
#     print(dim,param)
# quit()

ndims = len(idx)
# colors = sns.color_palette(n_colors=ndims)
# row = 8
# col = 5
# counter = 0

# fig, axs = plt.subplots(figsize=(10, 10), sharex=True, ncols = col, nrows = row)
# for dim, param in enumerate(sampled_params_list):
#     for r in range(row):
#         for c in range(col):
#
#             sns.distplot(samples[:, dim], color=colors[dim], norm_hist=True, ax=axs[row, col])
#             # fig.savefig('fig_PyDREAM_postprior_' + str(dim))
#
# f.add_subplot(111, frameon=False)
# f.subplots_adjust(wspace=0.4)
# f.subplots_adjust(hspace=0.5)
# # hide tick and tick label of the big axes
# plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
# plt.grid(False)
# plt.xlabel("Log(Parameter value)", fontsize=14)
# plt.ylabel("Probability", fontsize=14, labelpad=15)
# plt.savefig('pars_dist_plot_necro2_sns.pdf', format='pdf', bbox_inches="tight")
# quit()
# #
# plt.figure(figsize=(15, 10))
# for i in range(1,38):
#     plt.subplot(8, 5, i)
#     plt.plot(p2chain0[:, counter])
#     plt.title(model.parameters[idx[counter]].name, fontdict={'fontsize': 10})
#     plt.xlabel("Iteration", fontsize=10)
#     plt.ylabel("Log(10) PV", fontsize=9, labelpad=15)
#     counter += 1
# # plt.savefig('pydream_param_traceplot_629_chain0.pdf', format='pdf', bbox_inches="tight")
#
# plt.show()
# quit()

plt.figure(figsize=(15, 10))
for i in range(1,38):
    plt.subplot(8, 5, i)
    # plt.plot(samples[:, counter])
    sns.distplot(norm.rvs(size=n, loc=logps_vals[counter], scale=scaling[counter]), color='cyan')
    sns.distplot(samples[:, counter])
    plt.title(model.parameters[idx[counter]].name, fontdict={'fontsize': 10})
    counter += 1
    plt.xlabel("Log(10) Value", fontsize=10)
    plt.ylabel("Probability", fontsize=9, labelpad=15)
# plt.savefig('pydream_priorpost_traceplot_629_all_chains.pdf', format='pdf', bbox_inches="tight")
plt.show()
quit()
#PLOTTING PARAM TRACEPLOTS
f, axes = plt.subplots(row, col, figsize=(15, 10), sharex=True)
# f.suptitle("Posterior Distributions from PyDREAM calibration of Necroptosis Model", fontsize="x-large")
# for dim, param in enumerate(sampled_params_list):
for r in range(row):
    for c in range(col):
        # for dim, param in enumerate(sampled_params_list):
        # sns.distplot(norm.rvs(size=n, loc=logps_vals[counter], scale=scaling[counter]), color='red', ax=axes[r, c])
        # weightss = np.ones_like(samples[:, counter])/float(len(samples[:, counter]))
        # weightsp = np.ones_like(priors[:, counter]) / float(len(priors[:, counter]))
        axes[r, c].plot(samples[:, counter], ax=axes[r, c])
        # sns.distplot(priors[:, counter], ax=axes[r, c])
            # axes[r, c].hist(samples[:, counter], bins=25, color=colors[counter])
        axes[r, c].set_title(model.parameters[idx[counter]].name, fontdict={'fontsize':8})
        f.add_subplot(111, frameon=False)
        f.subplots_adjust(wspace=0.4)
        f.subplots_adjust(hspace=0.5)
        # hide tick and tick label of the big axes
        plt.tick_params(labelcolor='none', top='off', bottom='on', left='off', right='off')
        plt.grid(False)
        plt.xlabel("Log(Parameter value)", fontsize=14)
        plt.ylabel("Probability", fontsize=14, labelpad=15)
        # axes.set_ylim([0.0, 1.0])
        # axes[r, c].set_ylim(0.0,0.2)
        # axes[r,c].set_ticks()
        # axes[r,c].grid()
        counter += 1

        if counter >= len(idx):
            break

    # f.add_subplot(111, frameon=False)
    # f.subplots_adjust(wspace=0.4)
    # f.subplots_adjust(hspace=0.5)
    # # hide tick and tick label of the big axes
    # plt.tick_params(labelcolor='none', top='off', bottom='on', left='off', right='off')
    # plt.grid(False)
    # plt.xlabel("Log(Parameter value)", fontsize=14)
    # plt.ylabel("Probability", fontsize=14, labelpad=15)
# plt.title('Posterior Distributions from PyDREAM calibration of Necroptosis Model', fontsize=14)
# plt.savefig('pars_dist_plot_necro_priorsposts_50000.pdf', format='pdf', bbox_inches="tight")
plt.show()

quit()

# #TSTING

f, axes = plt.subplots(row, col, figsize=(15, 10), sharex=True)
# f.suptitle("Posterior Distributions from PyDREAM calibration of Necroptosis Model", fontsize="x-large")
# for dim, param in enumerate(sampled_params_list):
for r in range(row):
    for c in range(col):
        # for dim, param in enumerate(sampled_params_list):
        sns.distplot(norm.rvs(size=n, loc=logps_vals[counter], scale=scaling[counter]), color='red', ax=axes[r, c])
        weightss = np.ones_like(samples[:, counter])/float(len(samples[:, counter]))
        # weightsp = np.ones_like(priors[:, counter]) / float(len(priors[:, counter]))
        sns.distplot(samples[:, counter], ax=axes[r, c])
        # sns.distplot(priors[:, counter], ax=axes[r, c])
            # axes[r, c].hist(samples[:, counter], bins=25, color=colors[counter])
        axes[r, c].set_title(model.parameters[idx[counter]].name, fontdict={'fontsize':8})
        # axes.set_ylim([0.0, 1.0])
        # axes[r, c].set_ylim(0.0,0.2)
        # axes[r,c].set_ticks()
        # axes[r,c].grid()
        counter += 1

        if counter >= len(idx):
            break

f.add_subplot(111, frameon=False)
f.subplots_adjust(wspace=0.4)
f.subplots_adjust(hspace=0.5)
# hide tick and tick label of the big axes
plt.tick_params(labelcolor='none', top='off', bottom='on', left='off', right='off')
plt.grid(False)
plt.xlabel("Log(Parameter value)", fontsize=14)
plt.ylabel("Probability", fontsize=14, labelpad=15)
# plt.title('Posterior Distributions from PyDREAM calibration of Necroptosis Model', fontsize=14)
# plt.savefig('pars_dist_plot_necro_priorsposts_50000.pdf', format='pdf', bbox_inches="tight")
plt.show()

quit()
# plt.savefig('pars_dist_plot_necrosns7.pdf', format='pdf', bbox_inches="tight")
# #TESTING

#FROM JARM OSCAR
f, axes = plt.subplots(row, col, figsize=(15, 10),sharex=True, sharey=True)
# axes.tick_params(labelcolor='w', top='on', bottom='on', left='on', right='on')
# for dim, param in enumerate(sampled_params_list):
for r in range(row):
    for c in range(col):
        # for dim, param in enumerate(sampled_params_list):
        weights = np.ones_like(samples[:, counter])/float(len(samples[:, counter]))
        axes[r, c].hist(samples[:, counter], bins = 20, weights=weights)
            # axes[r, c].hist(samples[:, counter], bins=25, color=colors[counter])
        axes[r, c].set_title(model.parameters[idx[counter]].name, fontdict={'fontsize':8})
        # axes.set_ylim([0.0, 1.0])
        axes[r, c].set_ylim(0.0,0.25)
        # axes[r,c].tick_params(labelcolor='w', top='on', bottom='on', left='on', right='on')
        # axes[r,c].set_major_locator(plt.MaxNLocator(3))
        # axes[r,c].grid()
        counter += 1

        if counter >= len(idx):
            break

f.add_subplot(111, frameon=False)
f.subplots_adjust(wspace=0.4)
f.subplots_adjust(hspace=0.5)
# hide tick and tick label of the big axes
plt.ylim(top=1.0)
plt.tick_params(labelcolor='none', top='on', bottom='on', left='on', right='on')
plt.grid(False)
plt.xlabel("Log(Parameter value)", fontsize=14)
plt.ylabel("Probability", fontsize=14, labelpad=15)
constrained_layout=True
plt.show()
# plt.savefig('pars_dist_plot_necro10.pdf', format='pdf', bbox_inches="tight")
quit()
# obs_names = ['MLKLa_obs']
#
# # Defining a few helper functions to use
# def normalize(trajectories):
#     """even though this is not really needed, if the data is already between 1 and 0!"""
#     """Rescale a matrix of model trajectories to 0-1"""
#     ymin = trajectories.min(0)
#     ymax = trajectories.max(0)
#     return (trajectories - ymin) / (ymax - ymin)
#
# t = np.array([0., 30,  60,   120,  180, 270,  480,  960, 1440])
# data = np.array([0., 0., 0., 0., 0.01, 0.05, 0.5, 0.99, 1.])
# solver = ScipyOdeSimulator(model, tspan=t) #, rtol=1e-6, # rtol : float or sequence relative tolerance for solution
#                             #atol=1e-6) #atol : float or sequence absolute tolerance for solution
#
# rate_params = model.parameters_rules() # these are only the parameters involved in the rules
# param_values = np.array([p.value for p in model.parameters]) # these are all the parameters
# rate_mask = np.array([p in rate_params for p in model.parameters])  # this picks the element of intersection
#
# def likelihood(position):
#     params_tmp = np.copy(position)  # here you pass the parameter vector; the point of making a copy of it is in order not to modify it
#     param_values[rate_mask] = 10 ** params_tmp  # see comment above *
#     result = solver.run(param_values=param_values)
#     ysim_norm = normalize(result.observables['MLKLa_obs'])
#     error = np.sum((data - ysim_norm) ** 2)
#     return -error
#
#
#
# # converged = False
# # sampled_params, log_ps = run_dream(parameters=sampled_params_list,
# #                                    likelihood=likelihood,
# #                                    niterations=niterations,
# #                                    nchains=nchains,
# #                                    multitry=False,
# #                                    gamma_levels=4,
# #                                    adapt_gamma=True,
# #                                    history_thin=1,
# #                                    model_name='dreamzs_5chain',
# #                                    verbose=True)
# # total_iterations = niterations
# # # Save sampling output (sampled parameter values and their corresponding logps).
# # for chain in range(len(sampled_params)):
# #     np.save('dreamzs_5chain_sampled_params_chain_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
# #     np.save('dreamzs_5chain_logps_chain_' + str(chain)+'_'+str(total_iterations), log_ps[chain])
# # GR = Gelman_Rubin(sampled_params)
# # print('At iteration: ',total_iterations,' GR = ',GR)
# # np.savetxt('dreamzs_5chain_GelmanRubin_iteration_'+str(total_iterations)+'.txt', GR)
# # old_samples = sampled_params
# # if np.any(GR>1.2):
# #     starts = [sampled_params[chain][-1, :] for chain in range(nchains)]
# #     while not converged:
# #         total_iterations += niterations
# #         sampled_params, log_ps = run_dream(parameters=sampled_params_list,
# #                                            likelihood=likelihood,
# #                                            niterations=niterations,
# #                                            nchains=nchains,
# #                                            start=starts,
# #                                            multitry=False,
# #                                            gamma_levels=4,
# #                                            adapt_gamma=True,
# #                                            history_thin=1,
# #                                            model_name='dreamzs_5chain',
# #                                            verbose=False,
# #                                            restart=True)
# #         for chain in range(len(sampled_params)):
# #             np.save('dreamzs_5chain_sampled_params_chain_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
# #             np.save('dreamzs_5chain_logps_chain_' + str(chain)+'_'+str(total_iterations), log_ps[chain])
# # old_samples = [np.concatenate((old_samples[chain], sampled_params[chain])) for chain in range(nchains)]
# #         GR = Gelman_Rubin(old_samples)
# #         print('At iteration: ',total_iterations,' GR = ',GR)
# #         np.savetxt('dreamzs_5chain_GelmanRubin_iteration_' + str(total_iterations)+'.txt', GR)
# #         if np.all(GR<1.2):
# #             converged = True
# try:
#     #Plot output
#     import seaborn as sns
#     from matplotlib import pyplot as plt
#     # total_iterations = len(old_samples[0])
#     # burnin = total_iterations/2
#     # #samples = np.concatenate((old_samples[0][burnin:, :], old_samples[1][burnin:, :], old_samples[2][burnin:, :],old_samples[3][burnin:, :], old_samples[4][burnin:, :]))
#     # samples = np.concatenate(tuple([old_samples[i][int(burnin):, :] for i in range(nchains)]))
#     ndims = len(sampled_params_list)
#     colors = sns.color_palette(n_colors=ndims)
#     # for dim in range(ndims):
#     #     fig = plt.figure()
#     #     sns.distplot(samples[:, dim], color=colors[dim], norm_hist=True)
#     # fig.savefig('fig_PyDREAM_dimension_'+str(dim))
#
#     for dim, param in enumerate(sampled_params_list):
#         fig = plt.figure()
#         sns.distplot(samples[:, dim], color=colors[dim], norm_hist=True)
#         fig.savefig('fig_PyDREAM_postprior_%s' + str(dim), )
# except ImportError:
#     pass