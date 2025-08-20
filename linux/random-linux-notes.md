# Random linux notes

```
The following packages were automatically installed and are no longer required:
```

Is telling you that those packages that were automatically installed due dependency resolution, are no longer required, as the packages that depend on them has been removed or have other dependencies. You can remove them with a simple:

```
sudo apt-get autoremove
```

But you might want to upgrade your other packages too:

```
sudo apt-get upgrade
```







This doesn't work :

`sudo echo "10.10.144.110 webenum.thm" > /etc/hosts`



This works:&#x20;

`sudo -- sh -c "echo 10.10.144.110 webenum.thm >> /etc/hosts"`
