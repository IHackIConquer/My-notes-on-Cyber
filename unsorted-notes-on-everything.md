# Unsorted notes on everything

`wget IP_ADDRESS:PORT` will download the specified webpage&#x20;

`md5sum file.ext` to get MD5 hash value

`Exiftool file.ext` to get loads of info on images, audio and more&#x20;

`head -n 20 file.txt`  will print the first 20 lines of the file ([https://www.geeksforgeeks.org/head-command-linux-examples/](https://www.geeksforgeeks.org/head-command-linux-examples/))

keep detailed notes of **all** experimentations on THM

Look at Nessus

Look at OpenVAS

idea for phishing email: "Updated privacy statement" email . The unsubscribe button would lead to unsubscribe form where you'd have to fill out details like name phone etc&#x20;

<pre><code><strong>meterpreter > cd 'c:\Program Files (x86)\Windows Multimedia Platform\'
</strong></code></pre>

## Random Windows Notes

To quickly open the Command Prompt, press **Win + R**, type **cmd**, and then press **Enter**. This will open a standard Command Prompt window. Alternatively, you can hold **Ctrl +** **Shift** while pressing **Enter** after typing cmd in the Run dialog to open it as an **administrator**.

### Powershell

To get everything about the machine you can call

{% code overflow="wrap" %}
```powershell
commandlet | findstr # works similar to grep. It's case sensitive
```
{% endcode %}

```powershell
wmic CPU GET /format:list
```

```powershell
# Local System Information v3
# Shows details of currently running PC
# Thom McKiernan 11/09/2014

Clear-Host
$computerSystem = Get-CimInstance CIM_ComputerSystem
$computerMotherboard = Get-CimInstance -ClassName Win32_BaseBoard -Property *
$computerOS = Get-CimInstance CIM_OperatingSystem
$key = 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform'
$computerCPU = Get-CimInstance CIM_Processor
$computerGPU = Get-WmiObject Win32_VideoController
$computerHDD_C = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID = 'C:'"
$computerHDD_D = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID = 'D:'"
$windowsInstallDate = gcim Win32_OperatingSystem | select InstallDate
Clear-Host

Write-Host "System Information for: " $computerSystem.Name -BackgroundColor red
"Manufacturer: " + $computerSystem.Manufacturer
"Motherboard: " + $computerMotherboard.Product
"CPU: " + $computerCPU.Name
"GPU: " + $computerGPU.Description
"C: Capacity: "  + "{0:N2}" -f ($computerHDD_C.Size/1GB) + "GB"
"D: Capacity: "  + "{0:N2}" -f ($computerHDD_D.Size/1GB) + "GB"
"RAM: " + "{0:N2}" -f ($computerSystem.TotalPhysicalMemory/1GB) + "GB"
"Operating System: " + $computerOS.caption + ", Service Pack: " + $computerOS.ServicePackMajorVersion
"Windows Product Key: " + (Get-ItemProperty -Path $key -Name BackupProductKeyDefault).BackupProductKeyDefault
"Install date: " + $windowsInstallDate.InstallDate
"User logged In: " + $computerSystem.UserName
"Last Reboot: " + $computerOS.LastBootUpTime
```

`Systeminfo|more`

```powershell
# In Powershell
winget upgrade         # To see a list of all apps that can be updated
winget upgrade --all   # To update all the apps
```

```powershell
Get-WmiObject win32_operatingsystem | select osarchitecture # To see if 32 or 64bit
```

<pre class="language-powershell" data-overflow="wrap"><code class="lang-powershell">Measure-Object  # counts how many lines in the output as well as other counts.
                # example: "wevtutil.exe el | measure-object" will output: 
<strong>#Count    : 1071
</strong>#Average  :
#Sum      :
#Maximum  :
#Minimum  :
#Property :
</code></pre>

## windowseventlogs

Filter by Event ID: `*/System/EventID=<ID>`

Filter by XML Attribute/Name: `*/EventData/Data[@Name="<XML Attribute/Name>"]`

Filter by Event Data: `*/EventData/Data=<Data>`

#### Wevtutil.exe

<figure><img src=".gitbook/assets/event-ids-1.png" alt=""><figcaption><p><a href="https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/580595db9f745688bc7477f6/1476761074992/Windows+Logging+Cheat+Sheet_ver_Oct_2016.pdf">https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/580595db9f745688bc7477f6/1476761074992/Windows+Logging+Cheat+Sheet_ver_Oct_2016.pdf</a></p></figcaption></figure>

{% file src=".gitbook/assets/Spotting-the-Adversary-with-Windows-Event-Log-Monitoring.pdf" %}



{% file src=".gitbook/assets/Windows+Logging+Cheat+Sheet_ver_Oct_2016.pdf" %}

[https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)

{% code overflow="wrap" %}
```powershell
# Breakdown of the command
wevtutil qe Application /c:3 /rd:true /f:text

# wevutil - Enables you to retrieve information about event logs and publishers
# qe - Tells wevtutil to query events from a specified log.
# Application - The name of the log to query (in this case, the Application log
# /c:3  c = Count, Limits the output to 3 events.
# rd:true  = Reverse Direction, True means show the newest event first

```
{% endcode %}

#### Get-WinEvent

[https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-5.1](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-5.1)

<pre class="language-powershell" data-overflow="wrap"><code class="lang-powershell">Get-WinEvent -ListLog *      # get all event logs locally

Get-WinEvent -Path "C:\Users\Administrator\Desktop\merged.evtx" # To see all logs from a file=merged.evtx

Get-WinEvent -Path "C:\Users\Administrator\Desktop\merged.evtx" | Where-Object { $_.Id -eq 400 } # find events in the merged.evtx file with id 400

Get-WinEvent -ListProvider * # event log providers and their associated logs. The Name is the provider, and LogLinks is the log that is written to.

Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -Match 'WLMS' } # Log filtering allows you to select events from an event log

Get-WinEvent -ListLog *smb* # to find log names contating the word"smb". This isn't case sensitive

(Get-WinEvent -ListProvider Microsoft-Windows-Powershell).Events |
>>     Format-Table Id, Description | Measure-Object
# Displays how many different event IDs there are for Powershell

Get-WinEvent -Path D:\Downloads\Investigation-1.evtx -FilterXPath '*/EventData/Data[@Name="Image"] and */EventData/Data="C:\Windows\System32\svchost.exe"' |Format-List         # 


# "Image" is a technical term for a compiled binary file like an EXE or DLL. Also, it can match just the filename, or entire path. 


Format-List - Property * # Format-List uses the Property parameter with the asterisk (*) wildcard to display each property.

-MaxEvents  # To specify the number of events to display




<strong>https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.5&#x26;viewFallbackFrom=powershell-7.1
</strong><strong># Syntax and examples of usage
</strong></code></pre>

#### Xpath Queries

{% code overflow="wrap" %}
```powershell
https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100) # Syntax and functions

Get-WinEvent -LogName Application -FilterXPath '*/System/EventID=100' # This will filter events from the Windows Logs > Application with the tag of System, with event id 100
Get-WinEvent -Path "C:\Users\Administrator\Desktop\merged.evtx" -FilterXPath '*/System/EventID=4104' # this will find event Ids in the supplied file

Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"]' #  This will filter events from the Windows Logs > Application with the tag of System, with Provider name of "WMLS" (Not case sensitive)

Get-WinEvent -LogName Application -FilterXPath '*/System/EventID=101 and */System/Provider[@Name="WLMS"]' # This will combine the first cmdlet of showing events with id of 100 and providername of WLMS 

Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="System"' -MaxEvents 1 # This will get the logs from Security with username=System, it will only show 1 event.
 
Format-List # Add at the end of a command to displays all properties of each object in a vertical, readable list, rather than a horizontal table (which often cuts off long values like event messages
 
 Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam"' # To see all Security events for the user=Sam
 
Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4720' # To see when user account was created
 
Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"] and */System/TimeCreated[@SystemTime="2020-12-15T01:09:08.940277500Z"]' # will display events with provider name WLMS and specific this time 2020-12-15T01:09:08.940277500Z
 
 
```
{% endcode %}

<figure><img src=".gitbook/assets/xpath-7b.png" alt=""><figcaption><p>Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="System"' -MaxEvents 1</p></figcaption></figure>

[https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES)&#x20;

#### TotalCommander

run the internal command **cm\_OpenDrives** from TC's command line, and see if you device turns up in the list.

### Command Line

To see your public IP

in CMD type: `nslookup myip.opendns.com resolver1.opendns.com`&#x20;
