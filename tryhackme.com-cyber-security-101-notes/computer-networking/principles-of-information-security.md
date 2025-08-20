---
description: https://tryhackme.com/r/room/principlesofsecurity
---

# Principles of Information Security

## CIA Triad

<figure><img src="../../.gitbook/assets/5de96d9ca744773ea7ef8c00-1725781488612.png" alt=""><figcaption><p><a href="https://www.nccoe.nist.gov/">https://www.nccoe.nist.gov/</a></p></figcaption></figure>

## **C**onfidentiality, **I**ntegrity and **A**vailability (CIA)

### Confidentiality

This element is the protection of data from unauthorized access and misuse. To provide confidentiality is to protect this data from parties that it is not intended for.

### Integrity

The CIA triad element of integrity is the condition where information is kept accurate and consistent unless authorized changes are made. It is possible for the information to change because of careless access and use, errors in the information system, or unauthorized access and use. In the CIA triad, integrity is maintained when the information remains unchanged during storage, transmission, and usage not involving modification to the information. Steps must be taken to ensure data cannot be altered by unauthorised people (for example, in a breach of confidentiality).

### Availability

The main concern in the CIA triad is that the information should be available when authorised users need to access it.

For example, having 99.99% uptime on their websites or systems (this is laid out in Service Level Agreements). When a system is unavailable, it often results in damage to an organisations reputation and loss of finances. Availability is achieved through a combination of many elements, including:

* Having reliable and well-tested hardware for their information technology servers (i.e. reputable servers)
* Having redundant technology and services in the case of failure of the primary
* Implementing well-versed security protocols to protect technology and services from attack

## Principles of Priviliges

It is vital to administrate and correctly define the various levels of access to an information technology system individuals require.

The levels of access given to individuals are **determined** on two primary factors:

* The individual's role/function within the organisation
* The sensitivity of the information being stored on the system

**Privileged Identity Management** (PIM) and **Privileged Access Management** (PAM).

**PIM** is used to translate a user's role within an organisation into an access role on a system

**PAM** is the management of the privileges a system's access role has, amongst other things.

#### Principle of least privilige

Users should be given the minimum amount of privileges, and only those that are absolutely necessary for them to perform their duties.

## The Bell-laPadula Model

The Bell-La Padula Model is used to achieve confidentiality. This model has a few assumptions, such as an organisation's hierarchical structure it is used in, where everyone's responsibilities/roles are well-defined.

The **Bell-LaPadula Model** is a way to keep secrets safe in computer systems. It’s like a set of rules to make sure that sensitive information isn’t accidentally or intentionally leaked to people who shouldn’t see it.

Here’s how it works in simple terms:

1. **No Read Up (Simple Security Rule)**: If you don’t have the right clearance, you can’t read something secret. Imagine a spy who’s only allowed to know "Confidential" information—they can’t peek at "Top Secret" files.
2. **No Write Down (Star (\*) Property)**:\
   If you have access to secret info, you can’t save it somewhere less secure. For example, a spy with "Top Secret" clearance can’t write down secrets in a "Confidential" notebook that others might see.

It’s like a library where:

* Regular visitors can only read books in their section (no going to the "restricted" area).
* Librarians in the restricted section can read and work with books there but can’t leave secret books in the regular area.

This model is focused on **confidentiality**, ensuring secrets stay secret.

The Bell LaPadula Model is popular within organisations such as governmental and military. Because members of the organisation are presumed to have gone through vetting.

<figure><img src="../../.gitbook/assets/0e6e5d9d80785fc287b4a67e1453b295 (1).png" alt=""><figcaption></figcaption></figure>

## Biba Model

The **Biba Model** is all about keeping information **accurate** and **trustworthy**, rather than secret. It’s like the opposite of the Bell-LaPadula model, focusing on **integrity** instead of confidentiality.

Here’s how it works in simple terms:

1. **No Write Up**:\
   You can’t save your changes to something more important or trusted than your current level. For example, a junior employee can’t change the company’s official financial records because they’re not trustworthy enough for that task.
2. **No Read Down**:\
   You can’t read information from a less trusted source. For example, a senior manager wouldn’t rely on gossip from unverified sources when making big decisions.

Think of it like a clean kitchen:

* If your hands are dirty, you can’t touch the fancy, clean utensils (no write up).
* If you’re using the clean utensils, you can’t use them to mess with the dirty dishes (no read down).

The Biba Model keeps systems safe from bad data and makes sure everything stays clean and trustworthy!

<figure><img src="../../.gitbook/assets/Screenshot 2025-06-11 at 06-53-39 Principles of Security-TryHackMe. Learn the principles of information… by DimigraS Medium.png" alt=""><figcaption></figcaption></figure>

## Threat Modelling & Incident Response

Threat modelling is the process of reviewing, improving, and testing the security protocols in place in an organisation's information technology infrastructure and services.

A critical stage of the threat modelling process is identifying likely threats

#### Threat Modelling process

<figure><img src="../../.gitbook/assets/aabdd83977336fd44b3645a86e5ba20e (1).png" alt=""><figcaption></figcaption></figure>

An effective threat model includes:

* Threat intelligence
* Asset identification
* Mitigation capabilities
* Risk assessment

To help with this, there are frameworks such as **STRIDE** (**S**poofing identity, **T**ampering with data, **R**epudiation threats, **I**nformation disclosure, **D**enial of Service and **E**levation of privileges)&#x20;

&#x20;**PASTA** (**P**rocess for **A**ttack **S**imulation and **T**hreat **A**nalysis).

&#x20;**STRIDE** includes six main principles, which I have detailed in the table below:\


<table><thead><tr><th width="149">Principle</th><th>Description</th></tr></thead><tbody><tr><td>Spoofing</td><td><p>This principle requires you to authenticate requests and users accessing a system. Spoofing involves a malicious party falsely identifying itself as another.</p><p>Access keys (such as API keys) or signatures via encryption helps remediate this threat.</p></td></tr><tr><td>Tampering</td><td><p>By providing anti-tampering measures to a system or application, you help provide integrity to the data. Data that is accessed must be kept integral and accurate.</p><p>For example, shops use seals on food products.</p></td></tr><tr><td>Repudiation</td><td>This principle dictates the use of services such as logging of activity for a system or application to track.</td></tr><tr><td>Information Disclosure</td><td>Applications or services that handle information of multiple users need to be appropriately configured to only show information relevant to the owner.</td></tr><tr><td>Denial of Service</td><td>Applications and services use up system resources, these two things should have measures in place so that abuse of the application/service won't result in bringing the whole system down.</td></tr><tr><td>Elevation of Privilege</td><td>This is the worst-case scenario for an application or service. It means that a user was able to escalate their authorization to that of a higher level i.e. an administrator. This scenario often leads to further exploitation or information disclosure.</td></tr></tbody></table>

A breach of security is known as an incident. Actions taken to resolve and remediate the threat are known as Incident Response (IR)&#x20;

Incidents are classified using a rating of urgency and impact. Urgency will be determined by the type of attack faced, where the impact will be determined by the affected system and what impact that has on business operations.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/ab0cc8478b0bce9a400187f559d36dd6.png)

An incident is responded to by a Computer Security Incident Response Team (**CSIRT**) which is prearranged group of employees with technical knowledge about the systems and/or current incident. To successfully solve an incident, these steps are often referred to as the six phases of Incident Response that takes place, listed in the table below:

<table><thead><tr><th width="148">Action</th><th>Description</th></tr></thead><tbody><tr><td>Preparation</td><td>Do we have the resources and plans in place to deal with the security incident?</td></tr><tr><td>Identification</td><td>Has the threat and the threat actor been correctly identified in order for us to respond to?</td></tr><tr><td>Containment</td><td>Can the threat/security incident be contained to prevent other systems or users from being impacted?</td></tr><tr><td>Eradication</td><td>Remove the active threat.</td></tr><tr><td>Recovery </td><td>Perform a full review of the impacted systems to return to business as usual operations.</td></tr><tr><td>Lessons Learned</td><td>What can be learnt from the incident? I.e. if it was due to a phishing email, employees should be trained better to detect phishing emails.</td></tr></tbody></table>

<figure><img src="../../.gitbook/assets/pentesting.png" alt=""><figcaption></figcaption></figure>

