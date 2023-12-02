# Usage of Local Cluster & GNU/Linux
In a local cluster & with the `GNU/Linux` usage as host OS, the IPs exposed by the services should be ClusterIP kind, and it will need to manually exposed by the next command: 
```sh
kubectl port-forward service/mekno-api-service 5000:5000
```
Finally use the custom `yml` file (mekno_deploy_minikube.yml).

---
If something is not working propertly, take a look at your Firewall rules and IP tables defined by your OS.

See more information:
* https://opensource.com/article/18/9/linux-iptables-firewalld
* https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/

