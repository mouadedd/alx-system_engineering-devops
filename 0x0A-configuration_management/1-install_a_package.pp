# Ensure Python 3 and pip3 are installed
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3 with the specified version
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [Package['python3'], Package['python3-pip']],
}
