from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink, TCIntf
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from mininet.util import dumpNodeConnections

class MyTopo(Topo):
    def build(self):
        # Add switches and hosts
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        
        host1 = self.addHost('h1', ip='10.0.0.1')
        host2 = self.addHost('h2', ip='10.0.0.200')  # Host to run the redirect server
        host3 = self.addHost('h3', ip='10.0.0.201')  # New host with new IP for HTML
        
        # Add links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(switch1, switch2)
        self.addLink(host3, switch2)  # Link new host to the network

def run():
    topo = MyTopo()
    net = Mininet(topo=topo, controller=RemoteController, link=TCLink)
    net.start()
    
    # Start the redirect server on host2
    h2 = net.get('h2')
    h2.cmd('python3 -m http.server 80 --bind 10.0.0.200 &')

    # Start a simple web server on the new host (host3) to serve the HTML file
    h3 = net.get('h3')
    h3.cmd('python3 -m http.server 80 --bind 10.0.0.201 &')
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()

