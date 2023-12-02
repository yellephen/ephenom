#!/usr/bin/env pwsh  

param($content)
$bytes = [System.Text.Encoding]::Unicode.GetBytes($content)
return [Convert]::ToBase64String($bytes)