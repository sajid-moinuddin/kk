# kk
I am everything kubectl lacks (for sajid)

----------------------------
*my python learning by `doing something useful` project

```
(venv) ➜  kk git:(master) ✗ kk -h
k(kubectl)++ ... only better
Usage:
kk get (podnode|pn) [options]

Options:
    -h --help    show this
    -l STRING    label selector
    -f STRING    field selector
    -e STRING    exclude
    -o output    pydash format plus padding info, ie. node.metadata.name:62
    -w           watch mode

Example:
#    kk get pn \
#    -l 'app=streamtech-ibms-service/streamtech-cdn-selection-service' \
#    -f 'metadata.namespace=streamtech/content/commerce' \
#    -e 'metadata.owner_references[0].kind=DaemonSet' \
#    -o 'pod_name:62,node.metadata.labels.lifecycle,namespace,node.metadata.name:62' \
#    -w 
```

```
kk get podnode -f 'metadata.namespace=streamtech/content/commerce'  \
   -e 'metadata.owner_references[0].kind=DaemonSet'   \
   -o 'pod_name:62,node.metadata.labels.lifecycle,namespace,node.metadata.name:62' \
   -w
```   

```
kk get pn  \
    -l 'app=streamtech-ibms-service'   \
    -f 'metadata.namespace=streamtech/content/commerce'   \
    -e 'metadata.owner_references[0].kind=DaemonSet'   \
    -o 'pod_name:62,node.metadata.labels.lifecycle,namespace,node.metadata.name:62'  \
    -w
```

```
kk get pn  -e 'status.phase=Running/Succeeded'     -o 'pod_name:62,pod.status.phase,node.metadata.labels.lifecycle,namespace,node.metadata.name:15' -w 

stable-k8s-spot-termination-handler-6g27r                         Pending             spot                kube-system-exte    ip-10-100-61-19    
overprovisioner-pause-pod-857cb47476-kml8r                        Pending             spot                overprovisioner     ip-10-100-61-19    
kube-system-logging-fluentbit-to-kinesis-fluent-bit-4s852         Pending             spot                kube-system-logg    ip-10-100-61-19    
kiam-agent-cwbn9                                                  Pending             spot                kube-system-exte    ip-10-100-61-19 
```

##Installation

install pybuilder `pip3 install pybuilder`
run install.sh