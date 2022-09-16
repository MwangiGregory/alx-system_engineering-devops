# Server Configuration management 

Configuration management is the mechanism of managing a single or a group of servers\
to reach a desired state, that has been previously defined in a provisioning script \
using a tool specific language and features.

In this project, I learnt the basics of using Puppet.\
Puppet is a tool used to automate and orchestrate deployment and \
administration of servers. I learnt how to use Puppet's \
declarative language, to declare resources and trigger chnages in their states.
There are five types of resources in Puppet:

* File
* Package
* User
* Command
* Services

Instructions on how different parts of server system should be updated are \
written in a file called a Manifest. 

Puppet uses the Master/Agent configuration, where a Master Puppet, that is \
centralized, controls or manages master agents. 
