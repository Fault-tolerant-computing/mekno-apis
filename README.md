# mekno-apis
Repo para las API's de Mekano


## Malla de servicios Istio
1. Iniciar un cluster minikube
    - Con el servicio Docker habilitado, ejecuta el siguiente comando `minikube start`.
2. Descarga e instala Istio
    - Ve a [Getting Started](https://istio.io/latest/docs/setup/getting-started/), clona el repositorio de istio en la carpeta que desees y sigue los pasos de `Download istio`.
    - Instala istio con el siguiente comando `istioctl install`, este comando crea un nuevo espacio de nombres en tu cluster, y despliega los respectivos servicios de istio.

3. Configurar la inyección de proxy Envoy
    - Para indicar a istio que inyecte automáticamente proxies Envoy sidecar en cada despliegue, añada la etiqueta `istio-injection=enabled` en su espacio de nombres respetivo, con la siguiente orden `kubectl label namespace <namespace-name> istio-injection=enabled`.

4. Despliegue su aplicación
    - Aplica tus respectivos despliegues y servicios de kubernetes.

5. Instale las integraciones de Istio
    - Reubica una sesión bash en tu carpeta istio (descargada en el paso 2) y despliega los addons de istio con el siguiente comando `kubectl apply -f samples/addons`.

6. Habilitar Kiali
    - Por último, habilite el reenvío de puertos para kiali con `kubectl port-forward svc/kiali -n istio-system 20001`.
