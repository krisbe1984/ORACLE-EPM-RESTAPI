$username = Read-Host -Prompt 'Enter the Username:'
$password = Read-Host -Prompt 'Enter the Password:'
$base64AuthInfo = [convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("${username}:${password}")))
$base64AuthInfo