# Puppet script that installs nginx

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {"printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://x.com/0xTobii;
    }
}" > /etc/nginx/sites-available/default":
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}