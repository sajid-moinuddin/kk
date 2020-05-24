from kubernetes import config, client, watch
import time
import json
import pickle
import pydash as _
from kk.utils import Utils
# import only system from os 
from os import system, name 


class KubeObjects:
    all_nodes = []
    all_pods  = []

    def __init__(self, config_file=None, file_store = '/tmp'):
        self._file_store = file_store
        self.config_file = config_file
        self.config = config.load_kube_config(config_file = self.config_file)
        self.kubectl = client.CoreV1Api()
        # self.refresh()

    def refresh(self, save = True, use_cache = False):
        if use_cache:
            with open(self._file_store + "/nodes.bin", 'rb') as f:
                self.all_nodes = pickle.load(f)
            with open(self._file_store + "/pods.bin", 'rb') as f:
                self.all_pods = pickle.load(f)
        else:
            self.all_nodes.clear()
            self.all_pods.clear()

            for node in self.kubectl.list_node().items:
                self.all_nodes.append(node)
                self.all_nodes.sort(key=lambda n: n.metadata.labels['nodegroup'])

            for pod in self.kubectl.list_pod_for_all_namespaces().items:
                self.all_pods.append(pod)

        if save and not use_cache:
            with open(self._file_store + "/nodes.bin", 'wb') as f:
                pickle.dump(self.all_nodes, f)
            with open(self._file_store + "/pods.bin", 'wb') as f:
                pickle.dump(self.all_pods, f)

    @staticmethod
    def name(kube_object):
        if kube_object is not None:
            return kube_object.metadata.name
        else:
            return 'NA'

    def pods_with_node(self, node):
        node_pods = []
        for pod in self.all_pods:
            if pod.spec.node_name == self.name(node):
                node_pods.append(pod)
        return node_pods
 
    def pod_node(self, pod):
        for node in self.all_nodes:
            if self.name(node) == pod.spec.node_name:
                return node

    @staticmethod
    def node_group(node):
        if node is None:
            return 'NA'

        return node.metadata.labels['nodegroup']
    
    @staticmethod
    def safe_value(k8s_object, expression):
        return 

    @staticmethod
    def label(k8s_object, key):
        if k8s_object is None or k8s_object.metadata is None or k8s_object.metadata.labels is None:
            return None

        if key in k8s_object.metadata.labels:
            return k8s_object.metadata.labels[key]
        else:
            return None
    
    def filter_pod(self, label_selector = None, exclude = None, field_selector = None):
        to_return = list(filter(lambda o: 
                                self.is_match(o, 
                                    label_selector=label_selector, 
                                    exclude=exclude, 
                                    field_selector=field_selector), self.all_pods))
        return to_return

    def get_pod(self, pod_name = None, label_selector = None, field_selector = None):
        pods = self.filter_pod(label_selector = label_selector, field_selector=field_selector)
        to_ret = []
        if pod_name is not None:
            for p in pods:
                if pod_name in self.name(p):
                    to_ret.append(p)
        else:
            to_ret = pods
        return to_ret

    @staticmethod
    def is_match(k8s_object, label_selector = None, exclude = None, field_selector = None):
        if label_selector is not None:
            label_key, label_value = Utils.parse_key_val(label_selector)
            if not KubeObjects.label(k8s_object, label_key) or not KubeObjects.label(k8s_object, label_key) in label_value:
                return False

        if exclude is not None:
            exclude_key, exclude_value = Utils.parse_key_val(exclude)
            if _.get(k8s_object, exclude_key) == exclude_value:
                return False

        if field_selector is not None:
            field_key, field_value = Utils.parse_key_val(field_selector)
            if not _.get(k8s_object, field_key) in field_value:
                return False

        return True

    def pod_nodes(self, pod_label_selector = None, node_label_selector = None, exclude = None):
        pod_nodes = []
        for pod in self.all_pods:
            pod_node = self.pod_node(pod)

            pod_match = self.is_match(pod, pod_label_selector, exclude)
            node_match = self.is_match(pod_node, node_label_selector, exclude)
            if pod_match or node_match:    
                pod_nodes.append({'namespace': pod.metadata.namespace, 
                                    'pod_name': self.name(pod), 
                                    'pod_state':  pod.status.phase,
                                    'app_name': self.label(pod, 'app'),
                                    'node_name': self.name(pod_node), 
                                    'node_group' : self.node_group(pod_node), 
                                    'node_lifecycle': self.label(pod_node, 'lifecycle'),
                                    'pod':pod,
                                    'node': pod_node
                                    })
        pod_nodes.sort(key= lambda n: str(n['app_name']))
        return pod_nodes
        
    def node_pods(self):
        to_ret = []
        for node in self.all_nodes:
            print(f"{self.name(node)} \t {node.metadata.labels['nodegroup']}")
            node_pods = self.pods_with_node(node)
            for pod in node_pods: 
                to_ret.append({'node_name': self.name(node), 
                    'node_group': node.metadata.labels['nodegroup'], 
                    'pod_name': self.name(pod), 
                    'pod_status': pod.status.phase})
        return to_ret

    @staticmethod
    def is_good_state(state):
        good_states = ['Running', 'Succeeded', 'Completed']
        if state in good_states:
            return True
        else:
            return False
  

