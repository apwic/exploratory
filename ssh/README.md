# Setting up my other laptop as SSH host

Currently, I have two laptops, Macbook for my current daily use and my gaming laptop which I dont use right now. So, rather than keeping my other laptop unused I have an idea to use that as a remote server for keeping file and using it for development. My gaming laptop does have a lot of resource so that I can keep my mac clean.

Reference:

- <https://www.goto.com/blog/how-to-set-up-remote-access-to-servers#:~:text=Open%20the%20Server%20Manager%20from,in%20the%20System%20Properties%20window>.

It doesn't even require SSH or something like that, the correct term is using **remote desktop** and it works! Now I can code from remote desktop, but I think it is better to use SSH? Might have to explore a bit more for development purposes.

Apparently, after many attempts I've succeeded at connecting through SSH but **only in local network** , yet to achieve that I need to disable antivirus in my gaming laptop which is a security risk. It is a bit hard to expose my local IP to the internet using Port Forwading as it is stated that there are many bots that is maybe harmful.

**IT WORKSSS!!!**

## How I did it

### Setting up the laptop as SSH Host

To be honest, it is the easiest part as it's only require me to download the OpenSSH server. Just follow the guideline activate the SSH and enable it through the firewall and then done. My laptop can become an SSH Host.

### Getting Local IP Address

It is stupid of me to not knowing the IP Address. It's not that I don't know how to get the IP, it is as simple as:

```zsh
ipconfig /all
```

BUT, I struggle to find out of the tutorial that it is only works in local network. Hence, I can't find my device IP Address. It turns out that I just need to get the IP assigned from the WiFi. Once I get that I could access ssh from my mac to my laptop.

### How to make the SSH Secure

Based on the tutorial that I watched in here <https://www.youtube.com/watch?v=Bd5rdLzb5GM&ab_channel=TroubleChute>, thumbs up to that guy the tutorial is really clear and easy to follow!

I need to create a public and private key and disable using password authentication to make it more secure. And it works! not as smooth as I imagine though turns out that you need to add the private key to ssh in mac, not just the key file.

```zsh
chmod 600 <YOUR_PRIVATE_KEY_FILE>
ssh-add --apple-use-keychain <YOUR_PRIVATE_KEY_FILE>
```

You need to change the access to file and then you can add the key to ssh, notes that '--apple-use-keychain' only works on macOS 11+ if I'm not mistaken.

### Expose your ssh port to the Internet

This is truly the hardest part. What make this part hard is because of many answer in the internet suggesting that I need to port forward my ssh port from the router. Sounds easy, right?

While it is easy IF YOU HAVE ACCESS TO THE ROUTER. I am living in dorm currently and I do not have access to configure the router. I tried many things, resetting the router, but not work. Finding the router interface is a bit tedious too. I even asked my dorm owner for the access to the router, but He doesn't answer. I nearly gave up. But I just discovered that there is **tunneling**. I think there is more than one way to do that, but what worked for me is just that easy. Just use **ngrok**. It can expose your port to the internet just by using this command:

```zsh
ngrok tcp 22
```

Voila!!! Your port is now exposed to the internet. You can just change your SSH config to that URL from ngrok.
