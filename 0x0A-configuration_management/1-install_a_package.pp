# Install flask from pip3, version is 2.1.0
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}