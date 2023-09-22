# This manuscript enables the useer holberton to login and open files without error

#Incresase hard file limit for user hlberton
exec { 'increase-hard-file-limit-for-holberton-user':
command => 'sed-i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
path => '/usr]/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-hlberton-user':
command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
path => '/usr/local/bin/:/bin/'
}
