# CRL_Flask

In this tutorial, we learn how to set up a flask environment in order to comply with the requirements and the needs of the file stated in the CPSP Level 2 docx.

So to set up we will start by installing choco, in order to make it easier to download and install packages

1. Open Start and type in Powershell, right click and run as administrator
2. Copy and paste `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
3. Wait for download to finish. If there are no errors, type `choco -?` and if there are no errors you're good to go
