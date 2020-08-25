# kk
k(kubectl)++ ... only better

----------------------------
*my python learning by `doing something useful` project

(the basic concept here is joining the node data with the pod data (podnode object = {'pod': object, 'node': object}) and then searching / formatting output of the joined columns)

```
(venv) ➜  kk git:(master) ✗ kubectl pn -h
kubectl (podnode|pn) [options]

Options:
    -h --help    show this
    -l STRING    label selector
    -f STRING    field selector
    -e STRING    exclude
    -o output    pydash format plus padding info, ie. node.metadata.name:62
    --offline    do not fetch new data, work on the last fetched data
    --json       print the -o elements in json format
    -w           watch mode

Example:
#    kubectl podnode \
#    -l 'app=streamtech-ibms-service/streamtech-cdn-selection-service' \
#    -f 'metadata.namespace=streamtech/content/commerce' \
#    -e 'metadata.owner_references[0].kind=DaemonSet' \
#    -o 'pod_name:62,node.metadata.labels.lifecycle,namespace,node.metadata.name:62' \
#    -w 
```

```
kubectl podnode -f 'metadata.namespace=streamtech/content/commerce'  \
   -e 'metadata.owner_references[0].kind=DaemonSet'   \
   -o 'pod_name:62,node.metadata.labels.lifecycle,namespace,node.metadata.name:62' \
   -w
```   

```
kubectl podnode  \
    -l 'app=streamtech-ibms-service'   \
    -f 'metadata.namespace=streamtech/content/commerce'   \
    -e 'metadata.owner_references[0].kind=DaemonSet'   \
    -o 'pod_name:62,node.metadata.labels.lifecycle,namespace,node.metadata.name:62'  \
    -w
```

```
kubectl podnode  -e 'status.phase=Running/Succeeded'     -o 'pod_name:62,pod.status.phase,node.metadata.labels.lifecycle,namespace,node.metadata.name:15' -w 

stable-k8s-spot-termination-handler-6g27r                         Pending             spot                kube-system-exte    ip-10-100-61-19    
overprovisioner-pause-pod-857cb47476-kml8r                        Pending             spot                overprovisioner     ip-10-100-61-19    
kube-system-logging-fluentbit-to-kinesis-fluent-bit-4s852         Pending             spot                kube-system-logg    ip-10-100-61-19    
kiam-agent-cwbn9                                                  Pending             spot                kube-system-exte    ip-10-100-61-19 
```

```
kubectl podnode -f 'metadata.namespace=streamtech/content/commerce' -e 'metadata.owner_references[0].kind=DaemonSet' -o 'pod_name:62,pod.status.phase,node.metadata.labels.lifecycle,namespace,node.metadata.name:15,pod.spec.containers[0].resources.requests:30,pod.spec.containers[0].resources.limits:30'

psqlr-574867588f-wjx95                                            Running             spot                streamtech          ip-10-100-89-25    {'cpu': '100m', 'memory': '128Mi'}     {'cpu': '100m', 'memory': '128Mi'}
streamtech-pgadmin-dd7899d86-5lwl5                                Running             ondemand            streamtech          ip-10-100-91-19    {'cpu': '500m', 'memory': '512Mi'}     {'cpu': '1', 'memory': '512Mi'}
commerce-martian-auth0-service-59bdbf9967-85shw                   Running             ondemand            commerce            ip-10-100-83-22    {'cpu': '2', 'memory': '8Gi'}          {'cpu': '6', 'memory': '8Gi'}
commerce-martian-auth0-service-59bdbf9967-8qd29                   Running             ondemand            commerce            ip-10-100-103-2    {'cpu': '2', 'memory': '8Gi'}          {'cpu': '6', 'memory': '8Gi'}

```

```
kubectl podnode -f 'metadata.namespace=streamtech/content/commerce' -e 'metadata.owner_references[0].kind=DaemonSet' -o 'pod_name:62,pod.status.phase,node.metadata.labels.lifecycle,namespace,node.metadata.name:15,pod.spec.containers[0].resources.requests:35,pod.spec.containers[0].resources.limits:35,pod.status.container_statuses[0].restart_count' | sort -k3
```


##Installation

install pybuilder `pip3 install pybuilder`
run install.sh
