#!/usr/bin/pup
# Ensure Python 3 and pip3 are installed
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
