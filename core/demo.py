# _cfg.federate.sampler: uniform, group, responsiveness
# client_info=join_in_info=[],
# client_num: 100

# if 'client_resource' in self._cfg.federate.join_in_info:
#                 client_resource = [
#                     self.join_in_info[client_index]['client_resource']
#                     for client_index in np.arange(1, self.client_num + 1)
#                 ]
#             else:
#                 if self._cfg.backend == 'torch':
#                     try:
#                         model_size = sys.getsizeof(pickle.dumps(
#                             self.models[0])) / 1024.0 * 8.
#                     except Exception as error:
#                         model_size = 1.0
#                         logger.warning(f'Error {error} in calculate model '
#                                        f'size.')
#                 else:
#                     # TODO: calculate model size for TF Model
#                     model_size = 1.0
#                     logger.warning(f'The calculation of model size in backend:'
#                                    f'{self._cfg.backend} is not provided.')
#
#                 client_resource = [
#                     model_size / float(x['communication']) +
#                     float(x['computation']) / 1000.
#                     for x in self.client_resource_info
#                 ] if self.client_resource_info is not None else None
#
#             if self.sampler is None:
#                 self.sampler = get_sampler(
#                     sample_strategy=self._cfg.federate.sampler,
#                     client_num=self.client_num,
#                     client_info=_cfg.federate.sampler)