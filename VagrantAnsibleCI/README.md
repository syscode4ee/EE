# Install a CI environment with Vangrant and a ConfigManagement tool

## exercise
**Vagrant CI**
Using a configuration management language of your choosing (Ansible, Puppet, Salt) create a Vagrant setup that installs a Continuous Integration server of your choosing.

## assumptions
In this exercise i focused on trying to have a fully contained solution, in terms
of easiness to use and be flexible enough to be improved later.
I could have taken the route to install a basic install with a very simple playbook,
however I find this is more similar to real-world, and also this setup
I picked up Jenkins even if it's **NOT** the easiest one, but one of the most widespread for sure.
Also it's quite difficult to install including all the components needed to be a proficient ci/cd modern
solution, hence the challenge :)
The Vagrantfile
Again, I use OSX for the test.

## Version fixing
I have a fixation about versions, meaning that we should declare the version we use in playbooks and configuration, not just the latest. This is simply because there's a dependency chain of library that has been tested with and can lead to problems with upgrades and such.

## scripted soluton
```
cd VagrantAnsibleCI
vagrant up
```
Sometimes jenkins mirrors timeout (as there's noone local to the UK). This is not due to this solution and would require a local rsync copy of jenkins plugins to be performant.
if it fails to to timeout, simply do a `vagrant up --provision` to recover.

## improvements
This can be easily wrapped up into packer to create a ready to use vagrant box.
Also, this is a very basic jenkins install (rather than blueocean), for example it could benefit from scm checkout (backups) or shared storage for HA.
