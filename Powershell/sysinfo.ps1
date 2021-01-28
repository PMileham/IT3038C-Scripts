function getip {
 (get-netipaddress).IPv4Address | select-string "192"
}

write-host(getip)
$ip = getip
write-host("This machines IP Address is: $ip")