# 1. Verify that the aws-node pod is in Running status on each worker node
#
# To verify that the aws-node pod is in Running status on a worker node, command is :
# "kubectl get pods -n kube-system -l k8s-app=aws-node -o wide"
# If the command output shows that the RESTARTS count is 0, then the aws-node pod is in Running status.
#
#
# 2. To verify that the kube-proxy pod is in Running status on each worker node, command is :
# "kubectl get pods -n kube-system -l k8s-app=kube-proxy -o wide"

