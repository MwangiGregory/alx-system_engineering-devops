# Install flask from pip3. 
# Requirements:Intall flask and version must be 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
