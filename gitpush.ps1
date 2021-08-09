git add .
[string]$commitMessage = Read-Host -Prompt "Enter the commit message"
git commit -m $commitMessage
git push