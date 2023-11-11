# Postmortem: Unplanned Service Disruption - Surviving the Glitchpocalypse

![oops](https://media.giphy.com/media/XGVXt08iHVArvIElcw/giphy.gif)

## Hold on to Your Digital Hats, Folks!
Greetings, fellow tech adventurers! Today, we embark on a journey through the treacherous terrains of unexpected service disruptions. Buckle up and get ready for a rollercoaster ride of errors, misconfigurations, and a dash of debugging drama.


## The Glitchy Odyssey: A Summary
* Duration:
	* Our unexpected detour unfolded from 14:30 to 17:45 (GMT) on November 11, 2023. Forget tea time; it was troubleshooting time.
* Impact:
	* Picture this: a quarter of our users tapping their fingers impatiently as the digital hamster powering our servers took a coffee break. Slow loading times, intermittent errors – it was like a cosmic game of hide and seek with our beloved platform.
* Root Cause:
	* Hold your laughter – the villain of our tale was a misconfigured load balancer. Yes, the unsung hero (or villain?) of the digital world, playing favorites with our servers and causing a traffic tantrum.


## The Epic Timeline:
* Detection Time:
	* 14:30 (GMT), November 11, 2023
* Detection Method:
	* Our automated watchdogs barked loudly, alerting us to the impending chaos.
* Actions Taken:
	* Initial investigation felt like searching for a needle in a haystack. Spoiler: the needle was a misconfigured load balancer.
* Misleading Paths:
	* We played detective, suspecting everything from a network conspiracy to code rebellion.
	* It turns out our servers aren't secret agents, just misunderstood misconfigurations.
* Escalation:
	* Called in the rescue team (DevOps and Infrastructure teams) when our Sherlock Holmes hats weren't cutting it.
* Resolution:
	* Load balancer misconfiguration was identified as the root cause.
	* Load balancing settings were adjusted to evenly distribute incoming traffic.
	* Normal service was restored by 17:45 (GMT).


## Root Cause and Resolution:
#### Cause:
The misconfiguration in the load balancing system led to an uneven distribution of traffic. Some servers were overwhelmed, causing degraded performance and eventual service disruption.

#### Resolution:
The load balancing settings were promptly adjusted to ensure an even distribution of traffic among the application servers. This corrected the performance issues and restored normal service.



## Corrective and Preventative Measures:
![server_down](https://github.com/TobiLight/alx-system_engineering-devops/assets/25378643/908b537d-e2a0-40bd-bb23-eff583c3abb2)

* Improvements:
	* Implement regular audits of load balancing configurations to detect anomalies proactively.
	* Enhance monitoring alerts to provide more granular insights into server performance and load distribution.

* Tasks:
	* Conduct a comprehensive review of load balancing configurations within the next week.
	* Schedule regular audits of critical system configurations to catch potential issues early.
	* Enhance automated monitoring to include real-time analysis of server load and response times.
	* Provide additional training for team members on rapid issue detection and effective escalation procedures.


## Conclusion:
This unplanned service disruption served as a valuable learning experience. By addressing the root cause and implementing corrective measures, we aim to fortify our system against similar incidents in the future. The identified tasks will be prioritized to enhance the resilience of our infrastructure, ensuring a more robust and reliable user experience moving forward.