## Verify the pre-reqs for an IBM Cloud private installation

### Prerequisites:

This procedure requires you to have one computer with the following software:

1. Centos 7
2. Python


### Deployment:
Just run this command, at your linux, to install the inception server:

```
curl -l https://raw.githubusercontent.com/jmbarros/icp_inception/master/inception.py | /usr/bin/python
```

Simple, no?

## Automation Process 

Inline-style: 
![alt text](https://github.com/jmbarros/icp_inception/blob/master/images/coe-icp.png "Automation Model")

## Testing the environment

We recommend running the Guestbook application to test your environment.
Log on to the kube master and follow these steps:

    mkdir guestbook
    cd guestbook
    git clone https://github.com/kubernetes/kubernetes.git
    cd kubernetes
    git reset --hard 6a657e0bc25eafd44fa042b079c36f8f0413d420
    kubectl create -f examples/guestbook/all-in-one/guestbook-all-in-one.yaml

You can monitor the progress of the deployment by typing the following command:

    kubectl get pods

After a few seconds (or minutes), you should see the following result:

    [root@kube-master-1 guestbook]# kubectl get pods
    NAME                 READY     STATUS    RESTARTS   AGE
    frontend-3ibiv       1/1       Running   0          15m
    frontend-yg8ci       1/1       Running   0          15m
    frontend-yj0ca       1/1       Running   0          15m
    redis-master-p8tqa   1/1       Running   0          15m
    redis-slave-c0ydz    1/1       Running   0          15m
    redis-slave-erlp0    1/1       Running   0          15m

## Other scripts

Take a look at the following scripts too:

* `display-kubernetes.sh`
* `destroy-kubernetes.sh`
* `remove_api_key.sh`

### Reference links
* [Disabling GNOME Keyring](https://chrisjean.com/ubuntu-ssh-fix-for-agent-admitted-failure-to-sign-using-the-key/) - Causes interference with some SSH-based actions
* [sshpass man page](http://manpages.ubuntu.com/manpages/trusty/man1/sshpass.1.html)
* [sshpass return code 6](http://stackoverflow.com/questions/33961214/docker-run-fails-with-returned-a-non-zero-code-6) - When host key checking causes errors in SSH scripting
