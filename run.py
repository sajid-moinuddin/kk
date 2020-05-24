
#!/usr/bin/env python

#shortcut to quickly try and test without doing full pyb (TODO: learn some python testcase! probably best do it with testcases)

import sys
import logging
import  pydash as _

sys.path.append('src/main/python')

from kk.kube_objects import KubeObjects
from kk.utils import Utils

kk = KubeObjects()

kk.refresh(use_cache = True)

# pod_nodes = kk.pod_nodes()
# for pn in pod_nodes:
#     # Utils.print_preety(pn, 'pod_name:70', 'app_name:50', 'namespace', 'pod_state', 'node_group', 'node_lifecycle')
#     Utils.print_preety(pn, 'pod.metadata.name:70', 'node.metadata.name:70')

kiam_pod = kk.get_pod() #kk.get_pod(field_selector = 'metadata.namespace=streamtech/content/commerce')

for kp in kiam_pod:
    # print(kp)
    Utils.print_preety(kp, 'metadata.name:60', 'metadata.namespace')
    break
# print(kiam_pod)
# Utils.print_preety(kiam_pod, 'metadata.name:90')
# print(_.get(kiam_pod, 'metadata'))

# kk.filter_pod(label_selector = '')