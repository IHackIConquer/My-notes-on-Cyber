# Disabling Widgets and Search Bar Across Multiple Users in Windows 11

> **Disclosure**:  
> This whole writeup was generated based on an interactive conversation with an AI (ChatGPT/GPT-5). It reflects the step-by-step process I followed to configure a fresh Windows 11 install with multiple user accounts.

---

## Overview
After installing Windows 11, I wanted to remove unwanted UI clutter (Widgets and the Search bar) **across all 4 user accounts** on the system. Below is a summary of the steps I performed, using a combination of **Group Policy**, **Registry Edits**, and **Explorer restarts**.

---

## 1. Disable Widgets Across All Users

### Option 1 – Group Policy (Pro/Enterprise/Education editions)
1. Press `Win + R`, type `gpedit.msc`, and press **Enter**.  
2. Navigate to:  

Computer Configuration → Administrative Templates → Windows Components → Widgets

3. Double-click **Allow widgets**.  
4. Set it to **Disabled**, click **Apply**, then **OK**.  
5. Run `gpupdate /force` or restart the system.

This disables widgets for **all users**.

### Option 2 – Registry Edit (works on Home too)
1. Press `Win + R`, type `regedit`, and hit Enter.  
2. Navigate to:

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft

3. Right-click `Microsoft` → **New → Key** → name it `Dsh`.  
4. Inside `Dsh`, create a **DWORD (32-bit)** value:  
- Name: `AllowNewsAndInterests`  
- Value: `0`  
5. Restart the system.

This forces widgets **off system-wide**.

---

## 2. Disable the Search Bar on the Taskbar

### Option 1 – Taskbar Settings (per-user)
1. Right-click on the taskbar.  
2. Select **Taskbar settings**.  
3. Under **Taskbar items**, set **Search** to **Hidden** or **Icon only**.  

This applies **only to the logged-in user**.

### Option 2 – Registry Edit (system-wide)
The Group Policy editor doesn’t offer a way to fully hide the search box, only to remove search highlights (trending doodles, Bing content, etc.). To completely hide the search UI, I used the registry:

1. Press `Win + R`, type `regedit`, press Enter.  
2. For **per-user settings**:

HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Search

3. For **system-wide (all users)**:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Search

- If the `Search` key doesn’t exist under `CurrentVersion`, create it.  
4. Inside the `Search` key, create/modify a **DWORD (32-bit)** value:  
- Name: `SearchboxTaskbarMode`  
- Values:  
  - `0` = Hidden  
  - `1` = Show icon only  
  - `2` = Show search box  
5. Restart Explorer (see below) or reboot.

---

## 3. Restarting Explorer to Apply Changes

To avoid a full reboot, I restarted **Windows Explorer**:

1. Press `Ctrl + Shift + Esc` to open **Task Manager**.  
2. Under the **Processes** tab, locate the **parent Windows Explorer process** (folder icon, may have child processes).  
3. Right-click → **Restart**.  

This reloads the desktop, taskbar, and Start menu, applying registry changes immediately.

Alternatively, from PowerShell:
```powershell
Stop-Process -Name explorer -Force
Start-Process explorer.exe

Notes

    Group Policy works best for Pro/Enterprise/Education editions of Windows 11.

    Registry edits are required for Home editions and for system-wide enforcement.

    Some registry keys (like Search) may not exist until created manually.

    Restarting Explorer or rebooting is required for changes to take effect.

    Disclosure:
    This document was created by turning an interactive Q&A session with an AI (ChatGPT/GPT-5) into a structured write-up. It reflects the troubleshooting and steps I personally followed to configure my Windows 11 system.
