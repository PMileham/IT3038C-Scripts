function getip {
 (get-netipaddress).IPv4Address | select-string "192"
}

write-host(getip)
$ip = getip
write-host("This machines IP Address is: $ip")

$Vers = Get-Host | select-object version

$hostname = hostname

$date = Get-Date

$Body = "This machines IP is $ip. User is $env:username. Hostname is $hostname. Powershell version is $Vers. Today's date is $date"

write-host($Body)

Send-MailMessage -To "milehapk@mail.uc.edu" -From "natthekiddd@gmail.com" -Subject "IT3038C windows Sysinfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-credential)