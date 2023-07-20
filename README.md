# Faiss Web Service

### Getting started
```sh
docker run --rm -it -p 9001:5000 123wowow123/faiss-web-service:[FAISS_RELEASE]
```

Once the container is running, you should be able to ping the service:
```sh
# Healthcheck
curl '34.168.105.198/ping'

# Faiss search
curl 'localhost:5000/faiss/search?q=%E2%80%98Demon%20Slayer%E2%80%99%20Season%203%20Gets%20An%20Exact%20Release%20Date%20And%20New%20English%20Trailer&k=20'

curl "http://34.168.105.198/faiss/search?q=war%20in%20ukraine%20food%20shortages%20twitter%20live%20scope&k=20"


# Faiss add
curl 'localhost:5000/faiss/add' -X POST -d '{"id": 9999, "title": "war in ukraine", "description": "food shortages", "media": [{"html": "<div>twitter live scope</div>"}]}'

# Faiss remove
curl 'localhost:5000/faiss/remove' -X DELETE -d '{"id": 9999}'

# Sentiment Get
curl 'localhost:5000/sentiment' -X POST -d '{"title": "war in ukraine", "description": "<div>food shortages</div>", "media": [{"html": "<div>twitter live scope</div>"}]}'

# Sentiment Get
curl 'localhost:5000/sentiment' -X POST -d '{"title": "Hollywood writers’ strike halts production of ‘Stranger Things,’ ‘Severance,’ Marvel’s ‘Blade’", "description": "<p class=\"paragraph\"> The&nbsp;<b>2023 Writers Guild of America strike</b>&nbsp;is an&nbsp;<a href=\"https://en.wikipedia.org/wiki/Strike_action\">labor dispute</a>&nbsp;between the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Writers_Guild_of_America\">Writers Guild of America</a>&nbsp;(WGA) — representing 11,500 screenwriters&nbsp;— and the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Alliance_of_Motion_Picture_and_Television_Producers\">Alliance of Motion Picture and Television Producers</a>&nbsp;(AMPTP). It began at 12:01&nbsp;a.m.&nbsp;<a href=\"https://en.wikipedia.org/wiki/Pacific_Time_Zone\">PDT</a>&nbsp;on May 2, 2023. </p><p class=\"paragraph\"> The strike is the largest interruption to American television and film production since the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_television_in_the_United_States\">COVID-19 pandemic</a>&nbsp;in 2020, as well as the largest labor stoppage the WGA has performed since the&nbsp;<a href=\"https://en.wikipedia.org/wiki/2007%E2%80%9308_Writers_Guild_of_America_strike\">2007–08 strike</a>. </p><h2>Issues in the strike</h2><p class=\"paragraph\"> One of the main focus points in the labor dispute is the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Residual_(entertainment_industry)\">residuals</a>&nbsp;from&nbsp;<a href=\"https://en.wikipedia.org/wiki/Streaming_media\">streaming media</a>;<a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-hollywoodreporter/1235404087-6\">[5]</a>&nbsp;the WGA claims that AMPTP's share of such residuals has cut much of the writers' average incomes compared to a decade ago.<a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-7\">[6]</a><a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-8\">[7]</a>&nbsp;Writers also wanted&nbsp;<a href=\"https://en.wikipedia.org/wiki/Artificial_intelligence\">artificial intelligence</a>&nbsp;such as&nbsp;<a href=\"https://en.wikipedia.org/wiki/ChatGPT\">ChatGPT</a>&nbsp;to be used only as a tool that can help with research or facilitate script ideas and not as a tool to replace them </p><p class=\"paragraph\"> On May&nbsp;2, 2020, the latest Minimum Basic Agreement (MBA) became the collective bargaining agreement that covered most of the work done by WGA writers.<a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-wga/contracts/mba-11\">[10]</a><a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-sagaftra/wgaamptp/strike-12\">[11]</a>&nbsp;The Minimum Basic Agreement was an agreement that established a minimum wage for television and film writers. In television, the Minimum Basic Agreement only applied to those who wrote for&nbsp;<a href=\"https://en.wikipedia.org/wiki/Television_broadcasting\">broadcast television</a>&nbsp;shows and not for&nbsp;<a href=\"https://en.wikipedia.org/wiki/Streaming_television\">streaming television</a>. This was very clear when comparing&nbsp;<a href=\"https://en.wikipedia.org/wiki/Late-night_talk_show\">late-night talk shows</a>&nbsp;that were produced for broadcast television, such as&nbsp;<i><a href=\"https://en.wikipedia.org/wiki/The_Late_Show_with_Stephen_Colbert\">The Late Show with Stephen Colbert</a></i>&nbsp;by&nbsp;<a href=\"https://en.wikipedia.org/wiki/CBS\">CBS</a>&nbsp;versus&nbsp;<i><a href=\"https://en.wikipedia.org/wiki/The_Problem_with_Jon_Stewart\">The Problem with Jon Stewart</a></i>&nbsp;produced for streaming by&nbsp;<a href=\"https://en.wikipedia.org/wiki/Apple_TV%2B\">Apple TV+</a>. The writers who worked for&nbsp;<i>The Problem</i>&nbsp;were not covered by the MBA and therefore had to negotiate individually with the streaming company for their pay, and as a result, they were paid less than writers who wrote for&nbsp;<i>The Late Show</i>&nbsp;while doing the same amount of work. This pattern held true with other shows in the two categories.&nbsp;The MBA expired on May&nbsp;1, 2023. </p><p class=\"paragraph\"> The WGA estimated that its proposals would yield writers about $429&nbsp;million a year, whereas the AMPTP's offer would yield $86&nbsp;million. </p><p class=\"paragraph\"> One disputed issue is the Guild wanting requirements for \"mandatory staffing\" and \"duration of employment\" terms to be added to their contract, which would require all shows to be staffed with a minimum number of writers for a minimum amount of time, \"whether needed or not\" per the AMPTP. </p><p class=\"paragraph\"> Another important proposal that the WGA is advocating for is to ensure each member of a writing team receives their own pension and their own health care funds. The AMPTP rejected this proposal and did not offer a counterproposal. At the same time, there was a tentative agreement between the WGA and AMPTP to have 0.5% of negotiated minimums for all WGA minimums shifted into pensions and health funds. </p><p class=\"paragraph\"> <chronohash class=\"chrono-hash-highlight\">#Strike</chronohash> </p>", "media": [{"html": "<blockquote class=\"twitter-tweet\"><p lang=\"en\" dir=\"ltr\">IF IT AN’T ON THE PAGE .. IT AN’T on the STAGE !! <br>Writing is the beginning and the end !</p>&mdash; Henry Winkler (@hwinkler4real) <a href=\"https://twitter.com/hwinkler4real/status/1653764896432050178?ref_src=twsrc%5Etfw\">May 3, 2023</a></blockquote>\n<script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>\n"}]}'

# Sentiment Get Long
curl 'localhost:5000/sentiment' -X POST -d '{"title": "war in ukraine", "description": "<p class=\"paragraph\"> &nbsp;Apple today announced&nbsp;<a href=\"https://www.apple.com/mac/m1/\" target=\"_blank\">M1</a>, the most powerful chip it has ever created and the first chip designed specifically for the Mac. M1 is optimized for Mac systems in which small size and power efficiency are critically important. As a system on a chip (SoC), M1 combines numerous powerful technologies into a single chip, and features a unified memory architecture for dramatically improved performance and efficiency. M1 is the first personal computer chip built using cutting-edge 5-nanometer process technology and is packed with an astounding 16 billion transistors, the most Apple has ever put into a chip. It features the world’s fastest CPU core in low-power silicon, the world’s best CPU performance per watt, the world’s fastest integrated graphics in a personal computer, and breakthrough machine learning performance with the Apple Neural Engine. As a result, M1 delivers up to 3.5x faster CPU performance, up to 6x faster GPU performance, and up to 15x faster machine learning, all while enabling battery life up to 2x longer than previous-generation Macs.With its profound increase in performance and efficiency, M1 delivers the biggest leap ever for the Mac.1 </p><p class=\"paragraph\"> “There has never been a chip like M1, our breakthrough SoC for the Mac. It builds on more than a decade of designing industry-leading chips for iPhone, iPad, and Apple Watch, and ushers in a whole new era for the Mac,” said Johny Srouji, Apple’s senior vice president of Hardware Technologies. “When it comes to low-power silicon, M1 has the world’s fastest CPU core, the world’s fastest integrated graphics in a personal computer, and the amazing machine learning performance of the Apple Neural Engine. With its unique combination of remarkable performance, powerful features, and incredible efficiency, M1 is by far the best chip we’ve ever created.” </p><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/9754f41c-66e7-4000-9550-8d4cc91025e9-chrono-lg.webp\" alt=\"M1 is the first personal computer chip built using cutting-edge 5-nanometer process technology and is packed with an astounding 16 billion transistors.\" height=\"551\" width=\"980\"><figcaption class=\"fig-cap\">M1 is the first personal computer chip built using cutting-edge 5-nanometer process technology and is packed with an astounding 16 billion transistors.</figcaption></figure><h2>First System on a Chip for the Mac</h2><p class=\"paragraph\"> Macs and PCs have traditionally used multiple chips for the CPU, I/O, security, and more. Now with M1, these technologies are combined into a single SoC, delivering a whole new level of integration for greater performance and power efficiency. M1 also features a unified memory architecture that brings together high-bandwidth, low-latency memory into a single pool within a custom package. This allows all of the technologies in the SoC to access the same data without copying it between multiple pools of memory, further improving performance and efficiency. </p><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/826dc90a-683c-4ef2-8372-fabeee610862-chrono-lg.webp\" alt=\"CPU performance vs. power\" height=\"551\" width=\"980\"><figcaption class=\"fig-cap\">CPU performance vs. power</figcaption></figure><h2>The World’s Best CPU Performance per Watt</h2><p class=\"paragraph\"> M1 features an 8-core CPU consisting of four high-performance cores and four high-efficiency cores. Each of the high-performance cores provides industry-leading performance for single-threaded tasks, while running as efficiently as possible. They are the world’s fastest CPU cores in low-power silicon, allowing photographers to edit high-resolution photos with lightning speed and developers to build apps nearly 3x faster than before. And all four can be used together for a huge boost in multithreaded performance.&nbsp; </p><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/e62b8f9b-96f6-41e2-931b-15c99c5af2cf-chrono-lg.webp\" alt=\"M1 chip features 8-core CPU\" height=\"551\" width=\"980\"><figcaption class=\"fig-cap\">M1 chip features 8-core CPU</figcaption></figure><p class=\"paragraph\"> The four high-efficiency cores deliver outstanding performance at a tenth of the power. By themselves, these four cores deliver similar performance as the current-generation, dual-core MacBook Air at much lower power. They are the most efficient way to run lightweight, everyday tasks like checking email or browsing the web, and preserve battery life like never before. And all eight cores can work together to provide incredible compute power for the most demanding tasks and deliver the world’s best CPU performance per watt. </p><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/3fd23829-5262-496e-8ee6-922eb9e4ba3c-chrono-lg.webp\" alt=\"M1 includes an 8-core CPU delivering incredible compute power and the world’s best performance per watt.\" height=\"646\" width=\"980\"><figcaption class=\"fig-cap\">M1 includes an 8-core CPU delivering incredible compute power and the world’s best performance per watt.</figcaption></figure><h2>The World’s Fastest Integrated Graphics</h2><p class=\"paragraph\"> M1 includes Apple’s most advanced GPU. It benefits from years of analysis of Mac applications, including everyday apps and challenging pro workloads. With industry-leading performance and incredible efficiency, the GPU in M1 is in a class by itself. Featuring up to eight powerful cores capable of running nearly 25,000 threads simultaneously, the GPU can handle extremely demanding tasks with ease, from smooth playback of multiple 4K video streams to rendering complex 3D scenes. With 2.6 teraflops of throughput, M1 has the world’s fastest integrated graphics in a personal computer. </p><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/a20dd2d8-8bf6-4d25-9e0c-5b540731b9ec-chrono-lg.webp\" alt=\"The GPU in M1 is the most advanced Apple has ever created and the world’s fastest integrated graphics in a personal computer.\" height=\"649\" width=\"980\"><figcaption class=\"fig-cap\">The GPU in M1 is the most advanced Apple has ever created and the world’s fastest integrated graphics in a personal computer.</figcaption></figure><h2>Blazing-Fast, On-Device Machine Learning</h2><p class=\"paragraph\"> The M1 chip brings the Apple Neural Engine to the Mac, greatly accelerating machine learning (ML) tasks. Featuring Apple’s most advanced 16-core architecture capable of 11 trillion operations per second, the Neural Engine in M1 enables up to 15x faster machine learning performance. In fact, the entire M1 chip is designed to excel at machine learning, with ML accelerators in the CPU and a powerful GPU, so tasks like video analysis, voice recognition, and image processing will have a level of performance never seen before on the Mac. </p><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/41068488-0076-444c-b4d5-5d30a5a70f45-chrono-lg.webp\" alt=\"Developers leveraging machine learning can take full advantage of the blazing-fast performance of the Apple Neural Engine in M1.\" height=\"646\" width=\"980\"><figcaption class=\"fig-cap\">Developers leveraging machine learning can take full advantage of the blazing-fast performance of the Apple Neural Engine in M1.</figcaption></figure><h2>More Innovative Technologies Packed into M1</h2><p class=\"paragraph\"> The M1 chip is packed with a number of powerful custom technologies, including: </p><ul><li>Apple’s latest image signal processor (ISP) for higher quality video with better noise reduction, greater dynamic range, and improved auto white balance.</li></ul><ul><li>The latest Secure Enclave for best-in-class security.</li></ul><ul><li>A high-performance storage controller with AES encryption hardware for faster and more secure SSD performance.</li></ul><ul><li>Low-power, highly efficient media encode and decode engines for great performance and extended battery life.</li></ul><ul><li>An Apple-designed Thunderbolt controller with support for USB 4, transfer speeds up to 40Gbps, and compatibility with more peripherals than ever.</li></ul><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/a8989b3b-9f4d-4c30-8b1d-e4e9829d467b-chrono-lg.webp\" alt=\"The Apple-designed ISP in M1 makes video calls on the Mac sharper and more vivid.\" height=\"646\" width=\"980\"><figcaption class=\"fig-cap\">The Apple-designed ISP in M1 makes video calls on the Mac sharper and more vivid.</figcaption></figure><h2>macOS Big Sur Optimized for M1</h2><p class=\"paragraph\"> macOS Big Sur is engineered, down to its core, to take full advantage of all the capability and power of M1, delivering a massive boost in performance, astonishing battery life, and even stronger security protections. With M1, things users do every day feel noticeably faster and smoother. Just like iPhone and iPad, the Mac now instantly wakes from sleep. Browsing with Safari — which is already the world’s fastest browser — is now up to 1.5x speedier at running JavaScript and nearly 2x more responsive. </p><p class=\"paragraph\"> With Big Sur and M1, Mac users can run a greater range of apps than ever before. All of Apple’s Mac software is now Universal and runs natively on M1 systems. Existing Mac apps that have not been updated to Universal will run seamlessly with Apple’s Rosetta 2 technology. And iPhone and iPad apps can now run directly on the Mac. Additionally, the foundations of Big Sur are optimized to unlock the power of M1, including developer technologies from Metal for graphics to Core ML for machine learning. </p><figure class=\"fig-img\"><img loading=\"lazy\" class=\"img   \" src=\"https://chronopin.blob.core.windows.net/thumb/a5a1f819-c8c7-4392-9e09-855483e75783-chrono-lg.webp\" alt=\"Mac users now have access to a greater range of apps than ever before.\" height=\"646\" width=\"980\"><figcaption class=\"fig-cap\">Mac users now have access to a greater range of apps than ever before.</figcaption></figure><h2>Start of a Two-Year Transition for the Mac</h2><p class=\"paragraph\"> M1 powers the new<a href=\"https://www.apple.com/newsroom/2020/11/introducing-the-next-generation-of-mac/\" target=\"_blank\">MacBook Air, 13-inch MacBook Pro, and Mac mini</a>. They join the rest of the Mac product line to form the strongest Mac lineup ever. This is the beginning of a transition to a new family of chips designed specifically for the Mac. The transition to Apple silicon will take about two years to complete, and these three systems are an amazing first step. </p>"}'

### Production
The application runs with Flask's build in server. Flask's documentation clearly states [it is not suitable for production](http://flask.pocoo.org/docs/1.1.x/deploying/).


#### Docker Commands
Build docker image
`make`

Upload docker image to repo
`make release`


#### Google Docker/Kubernetes Commands

https://cloud.google.com/sdk/docs/install
https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#cloud-shell

Create cluster and go-live
`gcloud container clusters create-auto chronopin-cluster`

`gcloud container clusters get-credentials chronopin-cluster --region us-west1`

`kubectl create deployment faiss-web-service --image=us-west1-docker.pkg.dev/chronopin-209507/faiss/faiss-web-service:latest`

`kubectl scale deployment faiss-web-service --replicas=1`

`kubectl autoscale deployment faiss-web-service --cpu-percent=100 --min=1 --max=1`

checks
`kubectl get pods`

`kubectl expose deployment faiss-web-service --name=faiss-web-lb --type=LoadBalancer --port 80 --target-port 5000`

checks
`kubectl get service`

#### Rolling update

eg: or better use `make gbuild` & `make grelease`

`make gupdate`

`watch kubectl get pods`

`curl '34.168.105.198/ping'`

For delete service read doc


#### pyenv

https://realpython.com/intro-to-pyenv/


Make sure you are in 3.x version
`python -V`

Check version installed on your system
`pyenv versions`

Intall pyenv
`brew install pyenv`

Install python 3
`pyenv install -v 3`

Use python 3
`pyenv global 3.<actual version>`

Check pip is at the same version
`pyenv which pip`

Setup virtualenv
`pip install virtualenv`
`virtualenv venv`
`source venv/bin/activate`
`deactivate venv `

Pip freeze requirments

`pip freeze > requirements.txt`