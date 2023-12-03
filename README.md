# mekno-apis
Repo for the API's of Mekano


## Istio service mesh
1. Start a minikube cluster
    - With the Docker service enabled, run the next command `minikube start`.
2. Download & install Istio
    - Go to [Getting Started](https://istio.io/latest/docs/setup/getting-started/), clone the istio repository in your desired folder and follow the `Download istio` steps.
    - Install istio with the next command `istioctl install`, this command create a new namespace in your cluster, and deploy the respective istio services.

3. Configure Envoy Proxy Injection
    - To instruct istio to automatically inject Envoy sidecar proxies on every deploy, add the label `istio-injection=enabled` at your respetive namespace, with the next command `kubectl label namespace <namespace-name> istio-injection=enabled`.

4. Deploy your application
    - Apply your respective kubernetes deployments and services.

5. Install Istio Integrations
    - Relocate a bash session into your istio folder (downloaded in step 2) and deploy the istio addons with the next command `kubectl apply -f samples/addons`.

6. Enable Kiali
    - Finally enable the port forwarding for kiali with `kubectl port-forward svc/kiali -n istio-system 20001`.

