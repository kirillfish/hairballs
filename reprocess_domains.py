"""
Humble attempt to avoid using argparse each time when calling get_pycluster_data
and to remove unwieldy use case handling from the single large
get_pycluster_data.py file. Now different ways to handle get_pycluster_data
will be written not by means of argparse subparsers,
but rather as small separate scripts.
If you need some new pipeline functionality
(for instance, not to repeat cumbersome
calculations, but load everything you need that have been stored previously, and
proceed from somewhere in the middle of the get_pycluster_data.py,
rather than from the very beginning), just write the logic in separate file.

This file: provided that user sessions and domain stats are already obtained,
load and preprocess domains file (e.g., in order to get smaller graph),
then conduct the rest of the pipeline.
"""

from get_pycluster_data import PyclusterGraphConstructor as PGC
power = 0.6

pgc = PGC()
pgc.users_count = 5527000
pgc.min_users = 500
pgc.min_aff = 20
pgc.users_file_path = './5527K/users_5527K'
pgc.sessions_file_path = './5527K/users_sessions_5527K'
pgc.dom_file_path='./5527K/domains_5527K'

pgc.reprocess_domains()
pgc.getaff(saveResults=True)
pgc.parallel_sim(cores=6, save_results=True)
pgc.sparsification(saveResults=True, power=power)
