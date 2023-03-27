# puppet manifest to install 7 configure nginx server,
# with a 301 redirect 
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  content => "
server {
  listen 80;
  root /var/www/html;
  index index.html;
  
  location / {
    add_header Content-Type text/plain;
    return 200 'Hello World!';
  }
  
  location /redirect_me {
    return 301 https://www.example.com/;
  }
}
",
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}
