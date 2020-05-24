
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

# kiam_pod = kk.get_pod(label_selector = 'app=streamtech-ibms-service/streamtech-cdn-selection-service', field_selector = 'metadata.namespace=streamtech/content/commerce')

pods = kk.get_pod(field_selector='metadata.owner_references[0].kind=DaemonSet')
print(len(pods))

for kp in pods:
    Utils.print_preety(kp, False, 'metadata.name:60', 'metadata.namespace')
    print(_.get(kp, 'metadata.owner_references[0].kind'))
    print(_.get(kp, 'metadata.labels.genre'))

# pod_nodes = kk.pod_nodes( pod_label_selector = 'app=streamtech-ibms-service/streamtech-cdn-selection-service', field_selector = 'metadata.namespace=streamtech/content/commerce')

# for pn in pod_nodes:
#     Utils.print_preety(pn,  False, 'pod_name:62', 'node.metadata.labels.lifecycle', 'namespace', 'node.metadata.name:62')

#     print(_.get(pn, 'node.metadata.labels.lifecycle'))





























# print(kiam_pod)
# Utils.print_preety(kiam_pod, 'metadata.name:90')
# print(_.get(kiam_pod, 'metadata'))

# kk.filter_pod(label_selector = '')