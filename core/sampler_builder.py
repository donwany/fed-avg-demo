from core.sampler import ResponsivenessRealtedSampler, UniformSampler, GroupSampler
import logging

logger = logging.getLogger(__name__)


def get_sampler(sample_strategy='uniform',
                client_num=None,
                client_info=None,
                bins=10):
    """
    This function builds a sampler for sampling clients who should join the \
    aggregation per communication round.

    Args:
        sample_strategy: Sampling strategy of sampler
        client_num: total number of client joining the FL course
        client_info: client information
            argument in the context of the code you provided is a parameter that represents information about individual clients in a federated learning (FL) setting.
            It's a piece of data or a feature associated with each client that can be used to guide the process of selecting clients for participation in a particular round of FL aggregation.
            For example, client_info could include:
            `Responsiveness`: It might indicate how responsive a client has been in the past to FL requests or updates. Clients that have been more responsive could be prioritized.

            `Performance Metrics`: Information about the accuracy of the model on a client's local data. Clients with better-performing models could be given higher weight.

            `Device Type`: If clients are mobile devices or edge devices, you might want to consider their processing power or energy constraints when selecting them.

            `Location`: Geographical information about the clients, which could be useful if the FL system wants to distribute the load geographically.

    Other Client Characteristics: Any other features or attributes that are relevant to the FL problem you are working on.
        bins: size of bins for group sampler

    Returns:
        An instantiated Sampler to sample during aggregation.

    Note:
      The key-value pairs of built-in sampler and source are shown below:
        ===================================  ==============================
        Sampling strategy                    Source
        ===================================  ==============================
        ``uniform``                          ``core.sampler.UniformSampler``
        ``group``                            ``core.sampler.GroupSampler``
        ===================================  ==============================
    """
    if sample_strategy == 'uniform':
        return UniformSampler(client_num=client_num)
    elif sample_strategy == 'responsiveness':
        return ResponsivenessRealtedSampler(client_num=client_num, client_info=client_info)
    elif sample_strategy == 'group':
        return GroupSampler(client_num=client_num, client_info=client_info, bins=bins)
    else:
        raise ValueError(
            f"The sample strategy {sample_strategy} has not been provided.")