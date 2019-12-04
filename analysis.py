import sem
import numpy as np

NS3_FOLDER = 'ns-3'
SCRIPT = 'wifi-multi-tos'
RESULTS_FOLDER = 'results'
campaign = sem.CampaignManager.new(NS3_FOLDER, SCRIPT, RESULTS_FOLDER)

params = {
    'channelWidth': [20],
    'distance': list(range(0, 60, 5)),
    'mcs': list(range(0, 7, 2)),
    'nWifi': [1],
    'simulationTime': [5],
    'useRts': [False],
    'useShortGuardInterval': [False],
}
runs = 10

campaign.run_missing_simulations(params, runs)


def get_throughput(result):
    return float(result['output']['stdout'].split(" ")[-2])


results = campaign.get_results_as_numpy_array(params, get_throughput,
                                              runs).squeeze()
results_avg = np.mean(results, -1)

conc = np.concatenate((np.array(params['distance'])[:, None], results_avg),
                      axis=1)

# TODO Compute confidence intervals
np.savetxt("report/figures/data/throughput.txt", conc)
