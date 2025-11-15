---
description: https://tryhackme.com/room/socfundamentals
---

# SOC Fundamentals

<figure><img src="../../.gitbook/assets/6645aa8c024f7893371eb7ac-1718954786769.png" alt=""><figcaption><p><a href="https://tryhackme.com/room/socfundamentals">https://tryhackme.com/room/socfundamentals</a></p></figcaption></figure>

## People

<figure><img src="../../.gitbook/assets/6645aa8c024f7893371eb7ac-1718872774537.png" alt=""><figcaption><p><a href="https://tryhackme.com/room/socfundamentals">https://tryhackme.com/room/socfundamentals</a></p></figcaption></figure>

* **SOC Analyst (Level 1):** Anything detected by the security solution would pass through these analysts first. These are the first responders to any detection. SOC Level 1 Analysts perform basic alert triage to determine if a specific detection is harmful. They also report these detections through proper channels.
* **SOC Analyst (Level 2):** While Level 1 does the first-level analysis, some detections may require deeper investigation. Level 2 Analysts help them dive deeper into the investigations and correlate the data from multiple data sources to perform a proper analysis.
* **SOC Analyst (Level 3):** Level 3 Analysts are experienced professionals who proactively look for any threat indicators and support in the incident response activities. The critical severity detection reported by Level 1 and Level 2 Analysts are often security incidents that need detailed responses, including containment, eradication, and recovery. This is where Level 3 analysts’ experience comes in handy.
* **Security Engineer:** All analysts work on security solutions. These solutions need deployment and configuration. Security Engineers deploy and configure these security solutions to ensure their smooth operation.
* **Detection Engineer:** Security rules are the logic built behind security solutions to detect harmful activities. Level 2 and 3 Analysts often create these rules, while the SOC team can sometimes also utilize the detection engineer role independently for this responsibility.
* **SOC Manager:** The SOC Manager manages the processes the SOC team follows and provides support. The SOC Manager also remains in contact with the organization’s C
* ISO (Chief Information Security Officer) to provide him with updates on the SOC team’s current security posture and efforts.

**Note:** The roles in the SOC team can increase or decrease depending on the size and criticality of the organizations.

## Process

### Alert Triage Reporting

The detected harmful alerts need to be escalated to higher-level analysts for a timely response and resolution. These alerts are escalated as tickets and assigned to the relevant people.

<figure><img src="../../.gitbook/assets/6645aa8c024f7893371eb7ac-1718872960352.png" alt=""><figcaption><p><a href="https://tryhackme.com/room/socfundamentals">https://tryhackme.com/room/socfundamentals</a></p></figcaption></figure>

<table><thead><tr><th width="84">5 Ws</th><th width="617">Answers</th></tr></thead><tbody><tr><td><strong>What?</strong></td><td>A malicious file was detected on one of the hosts inside the organization’s network.</td></tr><tr><td><strong>When?</strong></td><td>The file was detected at 13:20 on June 5, 2024.</td></tr><tr><td><strong>Where?</strong></td><td>The file was detected in the directory of the host: "GEORGE PC".</td></tr><tr><td><strong>Who?</strong></td><td>The file was detected for the user George.</td></tr><tr><td><strong>Why?</strong></td><td>After the investigation, it was found that the file was downloaded from a pirated software-selling website. The investigation with the user revealed that they downloaded the file as they wanted to use a software for free.</td></tr></tbody></table>

### Reporting

The detected harmful alerts need to be escalated to higher-level analysts for a timely response and resolution. These alerts are escalated as tickets and assigned to the relevant people.

### Incident Response and Forensics

Sometimes, the reported detections point to highly malicious activities that are critical. In these scenarios, high-level teams initiate an incident response. [unit-4-or-cyber-security-incident-response](../../ncfe-l3-cyber-assignments-and-feedback/unit-4-or-cyber-security-incident-response/ "mention")

## Technology

* **SIEM:** Security Information and Event Management (SIEM) is a popular tool used in almost every SOC environment. This tool collects logs from various network devices, referred to as log sources. Detection rules are configured in the SIEM solution, which contains logic to identify suspicious activity. The SIEM solution provides us with the detections after correlating them with multiple log sources and alerts us in case of a match with any of the rules. Modern SIEM solutions surpass this rule based detection analysis, providing us with user behavior analytics and threat intelligence capability. Machine learning algorithms support this to enhance the detection capabilities.

Note: The SIEM solution only provides the **Detection** capabilities in a SOC environment.

* **EDR:** Endpoint Detection and Response (EDR) provides the SOC team with detailed real-time and historical visibility of the devices’ activities. It operates on the endpoint level and can carry out automated responses. EDR has extensive detection capabilities for endpoints, allowing you to investigate them in detail and respond with a few clicks.
* **Firewall:** A firewall functions purely for network security and acts as a barrier between your internal and external networks (such as the Internet). It monitors incoming and outgoing network traffic and filters any unauthorized traffic. The firewall also has some detection rules deployed, which help us identify and block suspicious traffic before it reaches the internal network.

Several other security solutions play unique roles in a SOC environment, such as Antivirus, EPP, IDS/IPS, XDR, SOAR, and more. The decision on what Technology to deploy in the SOC comes after careful consideration of the threat surface and the available resources in the organization.

An endpoint protection platform (EPP) is a solution deployed on endpoint devices to prevent file-based malware attacks, detect malicious activity, and provide the investigation and remediation capabilities needed to respond to dynamic security incidents and alerts.

Intrusion Detection System (IDS) is a system that detects unauthorised network and system intrusions. Examples include detecting unauthorised devices connected to the local network and unauthorised users accessing a system or modifying a file.

Intrusion Prevention System (IPS) is a device or application that detects and stops intrusions attempts proactively. They are usually deployed in front of the protected asset and block any potential threat from reaching their target.

Extended detection and response (XDR) is a cybersecurity technology that monitors and mitigates cyber security threats.

SOAR stands for Security Orchestration, Automation, and Response. It is a solution that helps organisations to streamline and automate their security operations, including incident management, threat intelligence, and vulnerability response.
